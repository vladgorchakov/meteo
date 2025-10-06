class MonitoringSystem:
    def __init__(self):
        self.wlan = None
        self.router = WiFiRouter(26)

        # Датчики
        self.sensors = SensorManager()
        self.data_sender = DataSender()

        # Серверы для проверки
        self.servers = [
            ('mqtt', ('mqtt.broker.com', 1883)),
            ('api', ('api.telemetry.com', 443)),
        ]

        self.connection_checker = ConnectionChecker(self.wlan, self.servers)
        self.telegram_bot = TelegramBot(Config.TELEGRAM_BOT_TOKEN, Config.TELEGRAM_CHAT_ID)
        self.display = StatusDisplay()
        self.button = StatusButton(Config.BUTTON_PIN, self.display, self)

        # Буфер для данных при отсутствии связи
        self.data_buffer = []

    def collect_and_send_data(self):
        """Сбор и отправка данных с датчиков"""
        print("🔄 Collecting sensor data...")

        # Чтение датчиков
        sensor_data = self.sensors.read_all_sensors()
        sensor_data['timestamp'] = time()

        # Проверяем соединение
        result = self.connection_checker.check()

        if result is False or not result[1][0]:  # Нет связи или MQTT недоступен
            # Буферизуем данные
            self.data_buffer.append(sensor_data)
            print(f"📦 Data buffered. Buffer size: {len(self.data_buffer)}")

            # Ограничиваем размер буфера
            if len(self.data_buffer) > Config.MAX_BUFFER_SIZE:
                self.data_buffer.pop(0)

            return False

        # Пытаемся отправить данные
        success = self.data_sender.send_mqtt(Config.MQTT_TOPIC, sensor_data)

        if success:
            # Пытаемся отправить буферизованные данные
            self._send_buffered_data()

            # Дублируем в HTTP (опционально)
            if result[1][1]:  # HTTP API доступен
                self.data_sender.send_http(Config.HTTP_API_URL, sensor_data)

            return True
        else:
            self.data_buffer.append(sensor_data)
            return False

    def _send_buffered_data(self):
        """Отправка буферизованных данных"""
        if not self.data_buffer:
            return

        print(f"🔄 Sending buffered data ({len(self.data_buffer)} records)")

        successful_sends = 0
        for data in self.data_buffer[:]:  # Копируем для безопасного удаления
            if self.data_sender.send_mqtt(Config.MQTT_TOPIC, data):
                self.data_buffer.remove(data)
                successful_sends += 1
            else:
                break  # Прерываем при первой неудаче

        print(f"✅ Sent {successful_sends} buffered records")

    def run_monitoring(self):
        """Основной цикл мониторинга"""
        self.router.start()

        if self.router.state:
            self.wlan = WiFiConnection(Config.WiFi_SSID, Config.WiFi_PASSWORD).create_wlan()
            self.connection_checker = ConnectionChecker(self.wlan, self.servers)

            self.display.show_message("System Starting...")
            self.check_and_report()

            last_data_send = 0
            start_time = time()

            while time() - start_time < Config.MONITORING_DURATION:
                # Проверяем кнопку
                self.button.check_button()

                current_time = time()

                # Периодическая отправка данных
                if current_time - last_data_send >= Config.DATA_SEND_INTERVAL:
                    self.collect_and_send_data()
                    last_data_send = current_time

                # Периодическая проверка соединения
                if int(current_time - start_time) % Config.CHECK_INTERVAL == 0:
                    self.check_and_report()

                sleep(0.1)
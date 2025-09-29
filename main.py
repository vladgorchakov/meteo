from time import sleep


# Инициализация микроконтроллера и самоблокировка питания


# Включение питания маршрутизатора


# Подключение к маршрутизатору 
#   Периодические осуществляется проверка состояния (есть ли соединение)

# Проверка доступа в Интернет (сделать пинг, проверить статус)
#   При условии, что активен маршрутизатор

class WifiRouter:
    def __init__(self, pin, name, password):
        self.pin = pin
        self.name = name
        self.password = password

    def on(self):
        self.pin.on()

    def off(self):
        self.pin.off()

    def hard_reset(self):
        self.on()
        sleep(5)
        self.off()

    def check_wifi_status(self):
        print(f"wifi status -> {"OK"}")

    def check_internet_status(self):
        pass

    def connect(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass
        
        
# Опрос датчиков 

# Запоковка данных с датчиков в необходимый формат

# Отправка информации на веб-сервер MQTT, HTTPS
#   Если активна сеть и активен доступ в интернет
#   Проверка, что данные были получены (по возможности)

# Опрос кнопок 
#   Если кнопка активна, то осуществить вывод запрашиваемой информации на OLED дисплей


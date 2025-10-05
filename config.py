class Config:
    # Pin configuration ESP32-WROOM-USB-C development board
    # Конфигурация выводов контроллера

    # Выводы управления питанием
    POWER_MAIN_PIN = 5 # Выход самоблокировки питания устройства
    POWER_LOAD_PIN = 6 # Выход разрешения питания остальных устройств

    # LED
    LED_PIN = 2 # Светодиод для отладки

    # I2C_1 interface configuration
    # Hardware I2C, аппаратный I2C
    SDA_PIN = 0 # Вывод SDA
    SCL_PIN = 0 # Вывод SCL

    # Temperature sensor 1-Wire DS18B20
    DS18B20_1_PIN = 0 # Датчик температуры DS18B20 №1
    DS18B20_2_PIN = 0 # Датчик температуры DS18B20 №2
    DS18B20_3_PIN = 0 # Датчик температуры DS18B20 №3

    # SPI interface configuration
    # Hardware? SPI for SD-card
    nCS_PIN = 0 # Вывод выбора устройства nCS
    MISO_PIN = 0 # Вывод выход данных MISO
    MOSI_PIN = 0 # Вывод входа данных MOSI
    SCK_PIN = 0 # Вывод тактирования SCK

    # UART_0 interface configuration and RS-485 EN_PIN
    TX0_PIN = 0 # Выход TX
    RX0_PIN = 0 # Вход RX
    EN_PIN = 0 # Выход управления прием/передача для RS-485
    UART0_BAUDRATE = 9600 # Скорость передачи информации
    UART0_STOPBIT = 1 # Количество стоповых бит: 1, 1.5, 2
    UART0_PARITY = "N" # Бит четности: N, ODD, EVEN
    # RS-485 configuration
    # Device 1 MODBUS SLAVE
    DEVICE1_MODBUS_ADRESS = 1 # Адрес устройства 1 на шине
    DEVICE1_MODBUS_TIMEOUT = 1000 # Максимальное время ожидания ответа в миллисекундах

    # Device 2 MODBUS SLAVE
    DEVICE2_MODBUS_ADRESS = 2 # Адрес устройства 2 на шине
    DEVICE2_MODBUS_TIMEOUT = 1000 # Максимальное время ожидания ответа в миллисекундах

    # Buttons configuration
    BTN0_PIN = 0 # Кнопка 0
    BTN1_PIN = 0 # Кнопка 1
    BTN2_PIN = 0 # Кнопка 2
    BTN3_PIN = 0 # Кнопка 3
    BTN_DEBOUNCE_TIME = 100 # Время в миллисекундах для устраниения дребезга контактов

    # ADC input configuration
    Vin_PIN = 0 # Вход АЦП для измерения напряжения на входе устройства (проверка уровня заряда аккумулятора)

    # Wi-Fi configuration
    WiFi_SSID = "339-1" # SSID Wi-Fi Имя сети, к которой подключаемся
    WiFi_PASSWORD = "51048563" # Password Wi-Fi пароль доступа к сети, к которой подключаемся
    WiFi_CONNECT_DELAY = 100 # Время ожидания перед подключением к сети в секундах (время для загрузки маршрутизатора)
    WiFi_CONNECT_TIMEOUT = 20 # Время ожидания подключения к сети в секундах
    WiFi_CONNECT_COUNT = 3 # Количество попыток подключения к сети
    WiFi_CONNECT_ATTEMPTS_DELAY = 1 # Время задержки между попытками подключения в секундах

    # 3G/4G configuration
    MODEM_CONNECT_DELAY = 100 # Время ожидания перед подключением к сети 3G/4G в секундах (время для установления связи)
    MODEM_CONNECT_TIMEOUT = 500 # Время ожидания подключения к сети в секундах
    MODEM_CONNECT_COUNT = 3 # Количество попыток подключения к сети

    # Internet test server 1
    TEST_SERVERS = [
        ("dns", ("8.8.8.8", 53)),
        ("thingspeak mqtt api", ("mqtt3.thingspeak.com", 8883)),
        ("thingspeak https api", ("api.thingspeak.com",  443)),
        ("telegram api", ("api.telegram.org", 443)),
    ]

    # Time configuration
    TIME_ON_LIMIT = 300 # Время работы в секундах с момента включения питания
    TIME_ON_DISPLAY = 15 # Время работы OLED индикатора с момента нажатия любой кнопки
    TIME_POWERUP = 3600 # Время в секундах между пробуждениями устройства

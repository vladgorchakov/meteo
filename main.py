# Инициализация микроконтроллера и самоблокировка питания

# Включение питания маршрутизатора
# Подключение к маршрутизатору 

# Периодические осуществляется проверка состояния (есть ли соединение)
# Проверка доступа в Интернет (сделать пинг, проверить статус)
# При условии, что активен маршрутизатор

# Опрос датчиков 

# Запаковка данных с датчиков в необходимый формат

# Отправка информации на веб-сервер MQTT, HTTPS
#   Если активна сеть и активен доступ в интернет
#   Проверка, что данные были получены (по возможности)

# Опрос кнопок 
#   Если кнопка активна, то осуществить вывод запрашиваемой информации на OLED дисплей

from time import time, sleep, sleep_ms
from config import Config
from router import WiFiRouter
from connection import WiFiConnection
from checker import ConnectionChecker
from ssd1306.ssd1306 import SSD1306_I2C
from keyboard import KeyBoard
from machine import Pin, I2C

'''
i2c = I2C(scl=Pin(22), sda=Pin(21))
print(i2c.scan())

oled_width = 128
oled_height = 64

try:
    oled = SSD1306_I2C(oled_width, oled_height, i2c)
except OSError:
    print("Display: can not connect")

wlan = WiFiConnection(Config.WiFi_SSID, Config.WiFi_PASSWORD).create_wlan()
net_checker = ConnectionChecker(wlan, Config.TEST_SERVERS)

'''

'''
start_time = time()

router = WiFiRouter(26)

router.start()
if router.state:
    wifi_connection = WiFiConnection(Config.WiFi_SSID, Config.WiFi_PASSWORD)
    wlan = wifi_connection.create_wlan()
    connection_state = ConnectionChecker(wlan, Config.TEST_SERVERS)

    while time() - start_time < 60: #Config.TIME_ON_LIMIT:
        state_buf = connection_state.check()
        print("\n\nwifi: ", "yes" if state_buf else "no")
        if state_buf:
            print("services:")
            for i in range(len(Config.TEST_SERVERS)):
                print(f"{Config.TEST_SERVERS[i][0]}: ", "yes" if state_buf[1][i] else "no")

        sleep(5)
'''
keyword = KeyBoard((34,35))
while True:
    keyword.update()
    key_state = keyword.get_pressed_state()
    for i in range(len(key_state)):
        if key_state[i]:
            print(f"key {i} pressed")

    sleep_ms(50)

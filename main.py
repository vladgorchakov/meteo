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

from time import time, sleep
from config import Config
from router import WiFiRouter
from connection import WiFiConnection
from checker import ConnectionChecker

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

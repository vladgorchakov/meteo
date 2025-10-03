from time import sleep
import socket
import network
from machine import Pin
from config import Config as conf


# Инициализация микроконтроллера и самоблокировка питания


# Включение питания маршрутизатора
# Подключение к маршрутизатору 
class WiFiRouter:
    def __init__(self, pin: int):
        self.switch = Pin(pin, Pin.OUT)

    def start(self):
        self.switch.on()

    def stop(self):
        self.switch.off()

    def hard_reset(self):
        self.switch.on()
        sleep(2)
        self.switch.off()

    @property
    def state(self):
        return self.switch.value()


# Периодические осуществляется проверка состояния (есть ли соединение)
# Проверка доступа в Интернет (сделать пинг, проверить статус)
# При условии, что активен маршрутизатор
class ConnectionChecker:
    def __init__(self, wlan, ip="8.8.8.8", port=53):
        self.ip = ip  # Можно список IP для проверки в виде кортежа ((ip:port), (ip:port))
        self.port = port
        self.__wlan = wlan
        self.__external_is_connect = False
        self.__internal_is_connect = False

    def __check_internal_network(self):
        self.__internal_is_connect = False
        for i in range(15):
            if self.__wlan.isconnected():
                self.__internal_is_connect = True
                break
            sleep(1)

    def __check_external_network(self):
        # Установить таумаут для ожидания ответа от сервера
        # Можно больше, так как канал связи через GSM
        if not self.__internal_is_connect:
            self.__external_is_connect = False
        else:
            client = socket.socket()
            try:
                client.connect((self.ip, self.port))
            except:
                self.__external_is_connect = False
            else:
                self.__external_is_connect = True

    @property
    def internal_is_connect(self):
        self.__check_internal_network()

        return self.__internal_is_connect

    @property
    def external_is_connect(self):
        self.__check_internal_network()
        self.__check_external_network()

        return self.__external_is_connect


class WiFiConnection:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.__wlan = None

    @property
    def wlan(self):
        return self.__wlan

    def create_wlan(self):
        self.__wlan = network.WLAN()
        self.__wlan.active(True)
        if not self.__wlan.isconnected():
            self.__wlan.connect(self.user, self.password)

        return self.__wlan


# Опрос датчиков 

# Запаковка данных с датчиков в необходимый формат

# Отправка информации на веб-сервер MQTT, HTTPS
#   Если активна сеть и активен доступ в интернет
#   Проверка, что данные были получены (по возможности)

# Опрос кнопок 
#   Если кнопка активна, то осуществить вывод запрашиваемой информации на OLED дисплей

router = WiFiRouter(26)
wifi_connection = WiFiConnection(conf.wifi_ssid, conf.wifi_password)
conn_status = ConnectionChecker(wifi_connection)

router.start()
if router.state:
    wlan = wifi_connection.create_wlan()
    conn_status = ConnectionChecker(wlan)
    print(conn_status.internal_is_connect)
    print(conn_status.external_is_connect)




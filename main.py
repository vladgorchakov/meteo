from time import sleep
#import requests
import socket
import network
from machine import Pin


# Инициализация микроконтроллера и самоблокировка питания


# Включение питания маршрутизатора
# Подключение к маршрутизатору 
class WifiRouter:
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
    def __init__(self, ip="8.8.8.8", port=53):
        self.ip = ip #Можно список IP для проверки в виде кортежа ((ip:port), (ip:port))
        self.port = port
        self.__external_is_connect = False
        self.__internal_is_connect = False

    def check_internal_network(self, wlan):
        for i in range(15): 
            if wlan.isconnected():
                self.__external_is_connect = True
                return True
            print('.', end='')
            sleep(1)
        
        self.__external_is_connect = False
        print("error: internal wifi connection does not exist")
        
        return False

    
    def check_external_network(self):
        # Установить таумаут для ожидания ответа от сервера
        # Можно больше, так как канал связи через GSM
        client = socket.socket()
        try:
            client.connect((self.ip, self.port))
        except Exception as e:
            self.__external_is_connect = False
            print(f"error: external wifi connection does not exist\n details: {e}")
        else:
            self.__external_is_connect = True

        return self.__external_is_connect
    
    def check(self, wlan):
        if self.check_internal_network(wlan):
            if self.check_external_network():
                return True
        return False


class wifiConnection:
    def __init__(self, user, password, conn_checker):
        self.user = user
        self.password = password
        self.conn_checker = conn_checker
        self.__wlan = None

    @property
    def wlan(self):
        return self.__wlan

    def create_wlan(self):
        self.__wlan = network.WLAN()
        self.__wlan.active(True)
        if not self.__wlan.isconnected():
            print('connecting to network:', end=' ')
            self.__wlan.connect(self.user, self.password)
        self.conn_checker.check_internal_network(self.__wlan)
        
        return self.__wlan

        
# Опрос датчиков 

# Запаковка данных с датчиков в необходимый формат

# Отправка информации на веб-сервер MQTT, HTTPS
#   Если активна сеть и активен доступ в интернет
#   Проверка, что данные были получены (по возможности)

# Опрос кнопок 
#   Если кнопка активна, то осуществить вывод запрашиваемой информации на OLED дисплей

router = WifiRouter(26)
conn_status = ConnectionChecker()
wifi_connection = wifiConnection('b76lop', 'chirp339', conn_status)

router.start()
if router.state:
    wifi_connection.create_wlan()
    if conn_status.check(wifi_connection.wlan):
        print("Соединение установлено!")

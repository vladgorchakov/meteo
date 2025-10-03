import socket
from time import sleep
from config import Config

'''
    Методы класса реализуют проверку доступности внутренней и внешней сети
'''
class ConnectionChecker:
    def __init__(self, wlan, ip:str = "8.8.8.8", port:int = 53):
        self.ip = ip  # Можно список IP для проверки в виде кортежа ((ip:port), (ip:port))
        self.port = port
        self.__wlan = wlan
        self.__external_is_connect = False
        self.__internal_is_connect = False

    def __check_internal_network(self) -> bool:
        for i in range(Config.WiFi_CONNECT_DELAY):
            if self.__wlan.isconnected():
                return True
            sleep(Config.WiFi_CONNECT_ATTEMPTS_DELAY)

        return False

    def __check_external_network(self) -> bool:
        # Установить таймаут для ожидания ответа от сервера
        if not self.__internal_is_connect:
            return False
        else:
            client = socket.socket()
            try:
                client.connect((self.ip, self.port))
            except:
                return False
            else:
                return True

    def check(self) -> tuple:
        self.__internal_is_connect = False
        self.__external_is_connect = False

        if self.__check_internal_network():
            self.__internal_is_connect = True
            if self.__check_external_network():
                self.__external_is_connect = True

        return self.__internal_is_connect, self.__external_is_connect

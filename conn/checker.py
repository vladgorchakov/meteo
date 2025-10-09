import socket
from time import sleep
from config import Config

'''
    Методы класса реализуют проверку доступности внутренней и внешней сети
'''
class ConnectionChecker:
    def __init__(self, wlan, servers:list):
        self.__services = servers
        self.__wlan = wlan
        self.__internal_is_connect = False
        self.__total_services = len(self.__services)
        self.__services_is_available = [False for i in range(self.__total_services)]

    #написать сеттер для замены серверов

    def __check_internal_network(self) -> bool:
        for i in range(Config.WiFi_CONNECT_DELAY):
            if self.__wlan.isconnected():
                return True
            sleep(Config.WiFi_CONNECT_ATTEMPTS_DELAY)

        return False

    def __check_network_service(self, service:tuple) -> bool:
        # Установить таймаут для ожидания ответа от сервера
        if not self.__internal_is_connect:
            return False
        else:
            client = socket.socket()
            try:
                client.connect(service)
            except:
                return False
            else:
                return True
            finally:
                try:
                    client.close()
                except:
                    pass

    def check(self):
        self.__internal_is_connect = self.__check_internal_network()

        if not self.__internal_is_connect:
            return False

        for i in range(self.__total_services):
            self.__services_is_available[i] = True if self.__check_network_service(self.__services[i][1]) else False

        return self.__internal_is_connect, tuple(self.__services_is_available)


def test():
    state = ConnectionChecker(Config.TEST_SERVERS)


if __name__ == "__main":
    test()
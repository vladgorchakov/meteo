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

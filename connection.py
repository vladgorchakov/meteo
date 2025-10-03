import network

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

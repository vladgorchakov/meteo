from time import time, sleep
from config import Config

class MonitoringSystem:
    def __init__(self, display, wlan, servers, router, net_checker):
        self.__display = display
        self.__servers = servers
        self.__router = router
        self.__net_checker = net_checker

    def send_to_display(self, data, x, y, update=False):
        if update:
            self.__display.fill(0)
        self.__display.text(data, x, y)
        self.__display.show()


    def run(self):
        self.__router.start()
        start_time = time()
        if self.__router.state:
            while time() - start_time < 60:  # Config.TIME_ON_LIMIT:
                state_buf = self.__net_checker()
                print("\n\nwifi: ", "yes" if state_buf else "no")
                if state_buf:
                    print("services:")
                    for i in range(len(Config.TEST_SERVERS)):
                        print(f"{Config.TEST_SERVERS[i][0]}: ", "yes" if state_buf[1][i] else "no")

                sleep(5)

from machine import Pin
from time import sleep


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

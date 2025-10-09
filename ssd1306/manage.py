from sensors import SensorData

class DisplayDataManager:
    def __init__(self, display, x_start = 0, y_start = 0, delta_y = 12):
        self.display = display
        self.delta_y = delta_y
        self.x_start = 0
        self.y_start = 0

    def show_data(self, strings):
        self.display.fill(0)
        for i in range(len(strings)):
            self.display.text(strings[i], 0, self.delta_y * i)
        self.display.show()

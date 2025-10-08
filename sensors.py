class SensorData:
    def __init__(self):

        # Data from RTC DS3231
        self.RTC_DS3231_Date = "2000-01-01"
        self.RTC_DS3231_Time = "HH:MM:SS"
        self.RTC_DS3231_Temperature = 0
        self.RTC_DS3231_Alarm_Date = "2000-01-01"
        self.RTC_DS3231_Alarm_Time = "HH:MM:SS"

        # Data from BME280
        self.BME280_Temperature = 0
        self.BME280_Humidity = 0
        self.BME280_Pressure = 0

        # Data from DS18B20_1
        self.DS18B20_1_Temperature = 0

        # Data from DS18B20_2
        self.DS18B20_2_Temperature = 0

        # Data from DS18B20_3
        self.DS18B20_3_Temperature = 0

        # Data from RS485_DS18B20_1
        self.DS18B20_4_Temperature = 0

        # Data from RS485_DS18B20_2
        self.DS18B20_5_Temperature = 0

        # Data from INA219
        self.INA219_ShuntVoltage = 0
        self.INA219_BusVoltage = 0
        self.INA219_Power = 0
        self.INA219_Current = 0


def test():
    sensor = SensorData()
    print(vars(sensor))

if __name__ == "__main__":
    test()

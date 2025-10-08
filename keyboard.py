from machine import Pin

class KeyBoard:
    def __init__(self, pins, press_threshold=3, max_count=30):
        """
        КОНСТРУКТОР класса - вызывается при создании объекта
        pins - список номеров GPIO, к которым подключены кнопки
        press_threshold - минимальное количество циклов для регистрации нажатия
        max_count - максимальное значение счетчика (ограничивает рост)
        """
        self.__buttons = [Pin(pin, Pin.IN) for pin in pins]
        self.__button_count = len(pins)
        self.__flags = [False] * self.__button_count
        self.__current_states = [False] * self.__button_count # Текущее состояние кнопки
        self.__previous_states = [False] * self.__button_count # Предыдущие состояние кнопки
        self.__counters = [0] * self.__button_count
        self.press_threshold = press_threshold
        self.max_count = max_count

    def update(self):
        # Перебираем ВСЕ кнопки по очереди (0, 1, 2, ...)
        for i in range(self.__button_count):
            if not self.__flags[i]: # Если флаг состояния активен не активен (было произведено его считывание)
                # ЧИТАЕМ ТЕКУЩЕЕ ФИЗИЧЕСКОЕ СОСТОЯНИЕ кнопки с пина
                # button.value() возвращает 1 когда кнопка отпущена (из-за PULL_UP)
                # и 0 когда нажата (замкнута на землю)
                # not button.value() инвертирует: теперь True = нажата, False = отпущена
                current_state = not self.__buttons[i].value()
                self.__current_states[i] = current_state # Сохраняем прочитанное состояние в массив текущих состояний

                # --- ОСНОВНАЯ ЛОГИКА ОБРАБОТКИ ---
                if current_state: # Если кнопка СЕЙЧАС НАЖАТА (current_state = True)
                    self.__previous_states[i] = True # Запоминаем что кнопка БЫЛА нажата (для следующего цикла)
                    if self.__counters[i] < self.max_count: # Пока счётчик не достиг максимального значения
                        self.__counters[i] += 1 # УВЕЛИЧИВАЕМ счетчик этой кнопки на 1 -> Чем дольше кнопка удерживается - тем больше счетчик
                        print("+1")
                else:
                    if self.__previous_states[i]:
                        if self.__counters[i] > self.press_threshold:
                            self.__previous_states[i] = False
                            self.__flags[i] = True
                    else:
                        if self.__counters[i] > 0:
                            self.__counters[i] -= 1

    def is_pressed(self):
        """
        Проверяет, была ли нажата кнопка и сбрасывает флаг
        если была нажата
        """
        pressed_button = []
        for i in range(self.__button_count):
            pressed_button.append(self.__flags[i])
            if self.__flags[i]:
                self.__flags[i] = False

        return pressed_button

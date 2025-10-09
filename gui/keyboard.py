from machine import Pin

class KeyBoard:
    def __init__(self, pins, press_threshold=3, max_count=30):
        """
        Конструктор класса - вызывается при создании объекта, принимает на вход:
        pins - список номеров GPIO, к которым подключены кнопки
        press_threshold - минимальное количество циклов для регистрации нажатия
        max_count - максимальное значение счетчика (ограничивает рост)
        """
        self.__buttons = [Pin(pin, Pin.IN) for pin in pins] # Инициализация кнопок
        self.__button_count = len(pins) # Сколько всего кнопок
        self.__flags = [False] * self.__button_count # Флаг, показывающий была ли кнопка действительно нажата
        self.__current_states = [False] * self.__button_count # Текущее состояние кнопки
        self.__previous_states = [False] * self.__button_count # Предыдущие состояние кнопки
        self.__counters = [0] * self.__button_count
        self.press_threshold = press_threshold # Минимальное количество циклов для регистрации нажатия (пороговое значение срабатывания)
        self.max_count = max_count # максимальное значение счетчика (ограничивает рост в случае залипания)

    def update(self):
        # Перебираем ВСЕ кнопки по очереди (0, 1, 2, ...)
        for i in range(self.__button_count):
            if not self.__flags[i]: # Если флаг состояния активен не активен (было произведено его считывание)
                current_state = not self.__buttons[i].value() # not button.value() инвертирует: теперь True = нажата, False = отпущена
                self.__current_states[i] = current_state # Сохраняем прочитанное состояние в массив текущих состояний

                # --- ОСНОВНАЯ ЛОГИКА ОБРАБОТКИ ---
                if current_state: # Если кнопка СЕЙЧАС НАЖАТА (current_state = True)
                    self.__previous_states[i] = True # Запоминаем что кнопка БЫЛА нажата (для следующего цикла)
                    if self.__counters[i] < self.max_count: # Пока счётчик не достиг максимального значения
                        self.__counters[i] += 1 # УВЕЛИЧИВАЕМ счетчик этой кнопки на 1 -> Чем дольше кнопка удерживается - тем больше счетчик
                else:
                    if self.__previous_states[i] and self.__counters[i] > self.press_threshold: # Если прошлое состояние кнопки было 1 и счётчик выше порового значения
                        self.__previous_states[i] = False # Текущее состояние сохраняется как прошлое для следующей итерации
                        self.__flags[i] = True # Устанавливается флаг нажатия
                    elif self.__counters[i] > 0: # Если прошлое состояние также было нулём или счётчик не дошёл до порогового значения и при этом не ушел в ноль
                            self.__counters[i] -= 1 # Уменьшаем счётчик на единицу (наказание за дребезг)

    def get_pressed_state(self):
        """
        Проверяет, была ли нажата кнопка и сбрасывает флаг
        если была нажата
        """
        pressed_button_buf = list(self.__flags) # Буфер временного хранения флагов состояния
        for i in range(self.__button_count): # Проход циклом по всем флагам
            if self.__flags[i]: # Если флаг установлен,
                self.__flags[i] = False # то сбрасываем его, так как произведено считывание

        return pressed_button_buf # Возвращаем флаг

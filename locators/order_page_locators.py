from selenium.webdriver.common.by import By


class OrderPageLocators:
    # --- Первая часть формы заказа ---

    INPUT_NAME = [By.XPATH, './/input[@placeholder = "* Имя"]'] # Поле ввода имени
    INPUT_SURNAME = [By.XPATH, './/input[@placeholder = "* Фамилия"]']# Поле ввода фамилии
    INPUT_ADDRESS = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]'] # Поле ввода адреса
    INPUT_METRO = [By.XPATH, './/input[@placeholder = "* Станция метро"]'] # Поле выбора станции метро (открывает список)

    # Станции метро (словарь с ключами для data.py)
    METRO = {
        "rokossovskogo": [By.XPATH, './/div[text()="Бульвар Рокоссовского"]'],  # Станция «Бульвар Рокоссовского»
        "cherkizovskaya": [By.XPATH, './/div[text()="Черкизовская"]'],          # Станция «Черкизовская»
    }

    INPUT_PHONE = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]'] # Поле для ввода телефона
    BUTTON_NEXT = [By.XPATH, './/button[text() = "Далее"]'] # Кнопка перехода на следующую часть формы

    # --- Вторая часть формы заказа ---

    INPUT_DATE = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]'] # Поле даты доставки

    # Календарь: выбор конкретного дня (словарь)
    DATE = {
        "17": [By.XPATH, './/div[contains(@class,"react-datepicker__day--017")]'],  # Дата 17 число
        "20": [By.XPATH, './/div[contains(@class,"react-datepicker__day--020")]'],  # Дата 20 число
    }

    DROPDOWN_PERIOD = [By.XPATH, './/div[@class="Dropdown-placeholder"]'] # Дропдаун для выбора срока аренды

    # Срок аренды (словарь)
    PERIOD = {
        "1day": [By.XPATH, './/div[@class="Dropdown-option" and text()="сутки"]'],          # Сутки
        "5days": [By.XPATH, './/div[@class="Dropdown-option" and text()="пятеро суток"]'],  # Пятеро суток
    }

    # Цвет самоката (словарь)
    COLOR = {
        "black": [By.XPATH, './/label[contains(text(),"чёрный жемчуг")]'],           # Чёрный жемчуг
        "grey": [By.XPATH, './/label[contains(text(),"серая безысходность")]'],      # Серая безысходность
    }

    INPUT_COMMENT = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]'] # Поле для комментария курьеру
    BUTTON_ORDER_SUBMIT = [By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'] # Кнопка "Заказать" для отправки формы
    BUTTON_CONFIRM_YES = [By.XPATH, './/button[text() = "Да"]'] # Кнопка подтверждения "Да" во всплывающем окне
    MODAL_ORDER_SUCCESS = [By.XPATH, './/div[@class = "Order_Modal__YZ-d3"]'] # Модальное окно подтверждения успешного заказа

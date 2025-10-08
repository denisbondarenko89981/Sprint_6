from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.INPUT_SURNAME, last_name)

    @allure.step('Заполнить поле "Адрес: куда привезти заказ"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Выбрать станцию метро')
    def set_metro(self, station_key):
        self.click_on_element(OrderPageLocators.INPUT_METRO)
        self.click_on_element(OrderPageLocators.METRO[station_key])

    @allure.step('Заполнить поле "Телефон: на него позвонит курьер"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.INPUT_PHONE, phone)

    @allure.step('Нажать на кнопку "Далее"')
    def click_further_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Выбрать дату доставки')
    def set_date(self, date_key):
        self.click_on_element(OrderPageLocators.INPUT_DATE)
        self.click_on_element(OrderPageLocators.DATE[date_key])

    @allure.step('Выбрать срок аренды')
    def set_period(self, period_key):
        self.click_on_element(OrderPageLocators.DROPDOWN_PERIOD)
        self.click_on_element(OrderPageLocators.PERIOD[period_key])

    @allure.step('Выбрать цвет')
    def set_color(self, color_key):
        self.click_on_element(OrderPageLocators.COLOR[color_key])

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step('Проверить появление модального окна "Заказ оформлен"')
    def check_success_order(self):
        return self.get_text(OrderPageLocators.MODAL_ORDER_SUCCESS)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER_SUBMIT)

    @allure.step('Нажать на кнопку "Да"')
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_CONFIRM_YES)

    @allure.step('Оформить заказ')
    def create_order(self, user):
        self.set_name(user['name'])
        self.set_last_name(user['last_name'])
        self.set_address(user['address'])
        self.set_metro(user['station'])      
        self.set_phone(user['phone'])
        self.click_further_button()
        self.set_date(user['date'])          
        self.set_period(user['period'])      
        self.set_color(user['color'])        
        self.set_comment(user['comment'])
        self.click_order_button()
        self.click_yes_button()

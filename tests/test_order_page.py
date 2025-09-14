import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import OrderData


class TestOrderPage:

    @allure.title('Создание заказа через кнопку в хедере сайта (набор данных 1)')
    def test_create_order_header_button(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        home_page.open_home_page()
        home_page.accept_cookie()
        home_page.click_header_order_button()
        order_page.create_order(OrderData.first_order)

        success_text = order_page.check_success_order()
        assert "Заказ оформлен" in success_text

    @allure.title('Создание заказа через кнопку на главной странице (набор данных 2)')
    def test_create_order_page_button(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        home_page.open_home_page()
        home_page.accept_cookie()
        home_page.click_page_button()
        order_page.create_order(OrderData.second_order)

        success_text = order_page.check_success_order()
        assert "Заказ оформлен" in success_text

from conftest import driver
from pages.home_page import HomePage
from data import Url
import allure


class TestHeaderLogo:
    @allure.title('Переход по клику на лого Самоката ведет на главную страницу сервиса')
    def test_redirect_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_header_order_button()
        home_page.click_on_scooter_logo()
        home_page.check_redirection_on_scooter_page()
        assert home_page.get_current_url() == Url.SCOOTER_HOME_PAGE

    @allure.title('Переход по клику на лого Яндекса открывает Dzen в новой вкладке')
    def test_redirect_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_on_yandex_logo()
        home_page.tab_switch(driver)
        home_page.check_redirection_on_dzen_page()
        assert home_page.get_current_url() == Url.DZEN_HOME_PAGE

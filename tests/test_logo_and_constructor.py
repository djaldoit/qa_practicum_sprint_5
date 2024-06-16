import pytest
from data import AccountData
from locators import Locators
from conftest import driver


@pytest.mark.test
class TestConstructorAndLogo:
    # Проверка на переход по логотипу
    def test_logo(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(AccountData.EMAIL)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(AccountData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()

        # Проверка, что логотип появился
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка на переход по кнопке "Конструктор"
    def test_constructor(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(AccountData.EMAIL)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(AccountData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # Проверка, что перешли на конструктор
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
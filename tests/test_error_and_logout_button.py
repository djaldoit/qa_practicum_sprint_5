from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import AccountData
from locators import Locators
from conftest import driver


class TestLogoutAndRestore:

    # Некорректный пароль
    def test_unsuccessful_registration(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.FIELD_NAME).send_keys(AccountData.NAME)
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(AccountData.EMAIL)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(AccountData.INCORRECT_PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Проверка, что сообщение об ошибке появилось
        assert driver.find_element(*Locators.ERROR_MESSAGE).is_displayed()

    # Выход из учетной записи
    def test_logaut(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(AccountData.EMAIL)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(AccountData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.LK_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.EXIT_BUTTON)).click()

        log_in_logo = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.LOGIN_TITLE))

        # Проверка, что выход произведен и видно лого вход
        assert log_in_logo.is_displayed()
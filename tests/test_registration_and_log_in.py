from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import AccountData, UserDataGenerator
from locators import Locators
from conftest import driver


class TestRegistrationAndLogaut:
    # Успешная регистрация
    def test_successful_registration(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.FIELD_NAME).send_keys(UserDataGenerator.user_data_generator()['name'])
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(UserDataGenerator.user_data_generator()['email'])
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(UserDataGenerator.user_data_generator()['password'])
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        logo_in = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_TITLE)
        )

        # Проверка, что заголовок "Вход" появился
        assert logo_in.is_displayed()

    # Успешный вход в форме регистрации
    def test_successful_login(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.LINK_LOGIN_REG).click()
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(AccountData.EMAIL)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(AccountData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        # Проверка, что регистрация прошла успешно
        assert driver.find_element(*Locators.LOGIN_TITLE).is_enabled()

    # Вход через кнопку "Войти" в форме восстановления пароля
    def test_restore_button_log_in(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD).click()
        driver.find_element(*Locators.LOG_IN).click()
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(AccountData.EMAIL)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(AccountData.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.LK_BUTTON).click()

        # Проверка, вход через кнопку 'Войти' в форме восстановления пароля прошла успешно
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'




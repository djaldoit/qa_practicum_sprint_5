from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from conftest import driver


class TestIngredients:
    def test_fillings(self, driver):
        driver.find_element(*Locators.BUTTON_SOUSES).click()
        driver.find_element(*Locators.BUTTON_BREADS).click()

        section_breads = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BREADS_TXT)
        )

        # Проверка, что перешли в меню "Булки"
        assert section_breads.is_displayed()

    def test_sauces(self, driver):
        driver.find_element(*Locators.BUTTON_SOUSES).click()

        section_sauces = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SAUCES_TXT)
        )

        # Проверка, что перешли в меню "Соусы"
        assert section_sauces.is_displayed()

    def test_breads(self, driver):
        driver.find_element(*Locators.BUTTON_FILLINGS).click()

        section_breads = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.FILLINGS_TXT)
        )

        # Проверка, что перешли в меню "Начинки"
        assert section_breads.is_displayed()
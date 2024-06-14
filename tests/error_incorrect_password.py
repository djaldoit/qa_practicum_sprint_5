from selenium.webdriver.common.by import By
from selenium import webdriver



#Создание драйвера
driver = webdriver.Chrome()

#Открыть браузер и перейти на страницу
driver.get("https://stellarburgers.nomoreparties.site/")

#Нажать на кнопку "Войти в аккаунт"
driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

#Вводим логин
driver.find_element(By.NAME, "name").send_keys('dzha@mail.com')

#Вводим пароль некоректный
driver.find_element(By.NAME, "Пароль").send_keys('1123')

#Нажать на кнопку "Войти"
driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

#Проверка на ошибку
assert driver.find_element(By.CLASS_NAME, "input__error").text == "Некорректный пароль"

driver.quit()
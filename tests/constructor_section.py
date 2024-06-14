from selenium.webdriver.common.by import By
from selenium import webdriver
import time


#Создание драйвера
driver = webdriver.Chrome()

#Открыть браузер и перейти на страницу
driver.get("https://stellarburgers.nomoreparties.site/")

#Нажать на соусы
driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]").click()

#Нажать на Начинки
driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]").click()

#Нажать на Булки
driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]").click()

driver.quit()
from selenium.webdriver.common.by import By


class Locators:
    # Локаторы авторизации
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # кнопка "Войти в аккаунт" в лэндинге
    FIELD_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # поле ввода email при входе в акк
    FIELD_NAME = (By.NAME, "name") # поле ввода логина
    FIELD_PASSWORD = (By.NAME, "Пароль") # поле ввода пароля
    SUBMIT_BUTTON = (By.NAME, "submit") # кнопка "Войти в аккаунт"
    LOGIN_SUBMIT = (By.XPATH, "//button")  # Кнопка ссылки "Войти" в форме регистрации
    LOGIN_TITLE = (By.XPATH, "//h2[text() = 'Вход']")  # текст Вход в форме регистрации
    LOGIN2_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # кнопка "Войти" при вводе логина/пароля

    # Локаторы Восстановления пароля
    LK_BUTTON = (By.LINK_TEXT, "Личный Кабинет")  # Кнопка "Личный кабинет"
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка Выход в ЛК
    LINK_LOGIN_REG = (By.XPATH, "//a[@href = '/login']")  # Ссылка "Войти" на странице авторизации
    FORGOT_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка "Восстановить пароль"
    LOG_IN = (By.XPATH, "//a[text() = 'Войти']")  # текст "Войти" на странице восстановления пароля
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # кнопка "Зарегистрироваться" при регистрации
    REGISTER_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")  # кнопка "Зарегистрироваться"

    # Локатор ошибки
    ERROR_MESSAGE = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")  # сообщение об ошибке

    # Локаторы конструктора и лого
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # логотип
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")  # "Конструктор"
    BUTTON_SOUSES = (By.XPATH, "//span[text() = 'Соусы']")  # кнопка "Соусы"
    BUTTON_FILLINGS = (By.XPATH, "//span[text() = 'Начинки']")  # кнопка "Начинки"
    BUTTON_BREADS = (By.XPATH, "//span[text() = 'Булки']")  # кнопка "Булки"
    SAUCES_TXT = (By.XPATH, "//h2[text() = 'Соусы']")  # раздел Соусы
    FILLINGS_TXT = (By.XPATH, "//h2[text() = 'Булки']")  # раздел Начинки
    BREADS_TXT = (By.XPATH, "//h2[text() = 'Начинки']")  # раздел Булки



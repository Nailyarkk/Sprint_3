from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    reg_site = 'https://stellarburgers.nomoreparties.site/register'

class SignInMain:
    name_site = 'https://stellarburgers.nomoreparties.site/'
    name_const = 'nailyarkk@ya.ru'
    password_const = 'Almaty2023'
    element_value = (By.CSS_SELECTOR, '.input__textfield-disabled[name="Name"][value="Nailyark_test"]')
    element_modal = (By.CSS_SELECTOR, 'div.Modal_modal_overlay__x2ZCr')
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    SUBMIT_TEXT_LK = (By.LINK_TEXT, "Личный Кабинет")
    SUBMIT_LOGIN = (By.CSS_SELECTOR, 'a[href="/login"]')
    SUBMIT_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    SUBMIT_EXIT = (By.XPATH, "//button[text()='Выход']")
    SUBMIT_SIGNIN = (By.XPATH, '//button[text()="Войти"]')
    NAME_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    SUBMIT_BUTTON_SIGN_IN = (By.XPATH, "//button[contains(text(),'Войти')]")
    SUBMIT_LK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    CURR_NAME = (By.XPATH, '//input[@name="name" and @value="nailyarkk@ya.ru"]')
    sousy = (By.XPATH, '//div//span[text()="Соусы"]')
    nachinky = (By.XPATH, '//div//span[text()="Начинки"]')
    bulky = (By.XPATH, '//div//span[text()="Булки"]')
    current_tab_const = 'tab_tab_type_current__2BEPc'
    tab_type_current_locator_sousy = (By.XPATH,'//div[contains(@class, "tab_tab_type_current__2BEPc")]//span[text()="Соусы"]' )
    tab_type_current_locator_nachinky= (By.XPATH,'//div[contains(@class, "tab_tab_type_current__2BEPc")]//span[text()="Начинки"]' )
    tab_type_current_locator_bulky = (By.XPATH, '//div[contains(@class, "tab_tab_type_current__2BEPc")]//span[text()="Булки"]')



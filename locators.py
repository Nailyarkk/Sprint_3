from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')

class SignInMain:
    element_value = (By.XPATH, '//input[@value="nailyarkk@ya.ru"]')

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
    CURR_NAME123 = (By.XPATH, '//input[@name="Name"]')
    CURR_NAME = (By.XPATH, '//input[@name="name" and @value="nailyarkk@ya.ru"]')
    sousy = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')
    nachinky = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')
    bulky = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
    constrfindtab = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default']")
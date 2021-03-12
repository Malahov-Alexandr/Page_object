from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    EMAIL_FOR_SIGN_IN = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_FOR_SIGN_IN = (By.CSS_SELECTOR, '#id_login-password')
    EMAIL_FOR_SIGN_UP = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FOR_SIGN_UP = (By. CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_SIGN_IN_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "//button[@name='registration_submit']")
    
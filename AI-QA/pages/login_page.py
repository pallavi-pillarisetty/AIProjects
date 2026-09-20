from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "email").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "password").send_keys(password)

    def tap_login(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login_button").click()

    def is_home_screen_displayed(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "home_screen").is_displayed()

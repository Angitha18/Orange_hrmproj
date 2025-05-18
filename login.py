from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage.basepage import BasePage


class LoginPage(BasePage):

    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):

        username_field = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_FIELD)
        )
        username_field.clear()  # Clear any existing text
        username_field.send_keys(username)
        print(f"👤 Entered username: {username}")

    def enter_password(self, password):

        password_field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_FIELD)
        )
        password_field.clear()  # Clear any existing text
        password_field.send_keys(password)
        print("Entered password")

    def click_login(self):

        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()
        print("Clicked Login")

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        print("Login completed.")
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        """Wait for element to be clickable and then click."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
        except TimeoutException:
            print(f"Timeout: Element {by_locator} not clickable.")

    def send_keys(self, by_locator, text):
        """Wait for element and send keys."""
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"Timeout: Unable to send keys to {by_locator}.")

    def get_element(self, by_locator):
        """Wait for element and return it."""
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def get_text(self, by_locator):
        """Get text from an element."""
        element = self.get_element(by_locator)
        return element.text

    def is_visible(self, by_locator):
        """Check if element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def wait_and_click_suggestion(self, text):
        """Wait for autocomplete suggestion and click."""
        try:
            suggestion = (By.XPATH, f"//div[@role='listbox']//span[normalize-space()='{text}']")
            self.click(suggestion)
        except TimeoutException:
            print(f"Timeout: Suggestion '{text}' not found.")
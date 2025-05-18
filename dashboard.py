from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage.basepage import BasePage


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.pim_option = (By.XPATH, "//span[contains(.,'PIM')]")

    def pim_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_option)
        ).click()

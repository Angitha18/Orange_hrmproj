from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage.basepage import BasePage


class PersonalDetails(BasePage):

    NATIONALITY_DROPDOWN = (By.XPATH, "//label[contains(text(),'Nationality')]/following::div[contains(@class,'oxd-select-text')][1]")
    MARITAL_STATUS_DROPDOWN = (By.XPATH, "//label[text()='Marital Status']/parent::div/following-sibling::div//div[contains(@class, 'oxd-select-text')]")
    DATE_OF_BIRTH_INPUT = (By.XPATH, "//label[text()='Date of Birth']/parent::div/following-sibling::div//input")
    SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
    FORM_LOADER = (By.CLASS_NAME, "oxd-form-loader")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class, 'oxd-toast--success')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page_load(self):

        self.wait.until(EC.invisibility_of_element_located(self.FORM_LOADER))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Nationality']")))
        print("Personal Details page loaded.")

    def select_nationality(self, nationality):

        print(f"Selecting nationality: {nationality}")
        self.wait.until(EC.invisibility_of_element_located(self.FORM_LOADER))

        dropdown = self.wait.until(EC.element_to_be_clickable(self.NATIONALITY_DROPDOWN))
        dropdown.click()

        option = (By.XPATH, f"//div[@role='listbox']//span[normalize-space()='{nationality}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()
        print(f"Nationality selected: {nationality}")

    def select_marital_status(self, status="Single"):

        self.wait.until(EC.invisibility_of_element_located(self.FORM_LOADER))

        dropdown = self.wait.until(EC.element_to_be_clickable(self.MARITAL_STATUS_DROPDOWN))
        dropdown.click()

        option = (By.XPATH, f"//div[@role='listbox']//span[text()='{status}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()
        print(f"Marital status selected: {status}")

    def set_date_of_birth(self, dob_str):

        print(f"Setting Date of Birth: {dob_str}")
        self.wait.until(EC.invisibility_of_element_located(self.FORM_LOADER))

        dob_field = self.wait.until(EC.presence_of_element_located(self.DATE_OF_BIRTH_INPUT))
        dob_field.click()
        dob_field.send_keys(Keys.CONTROL + "a")
        dob_field.send_keys(Keys.DELETE)

        self.wait.until(lambda d: dob_field.get_attribute("value") == "")
        dob_field.send_keys(dob_str)
        self.wait.until(lambda d: dob_field.get_attribute("value") != "")
        print("✅ Date of Birth set.")

    def save_personal_details(self):

        print(" Saving personal details...")
        self.wait.until(EC.invisibility_of_element_located(self.FORM_LOADER))

        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()

        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
            print("✅ Personal details saved successfully.")
        except Exception:
            print("⚠No success confirmation appeared")

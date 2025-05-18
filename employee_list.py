from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from BasePage.basepage import BasePage


class EmployeeListPage(BasePage):

    EMPLOYEE_NAME_FIELD = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    EMPLOYEE_LIST_TAB = (By.XPATH, "//span[text()='Employee List']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def _suggestion_box(self, name):
        """Returns locator for employee name suggestion."""
        return (By.XPATH, f"//div[@role='listbox']//span[normalize-space()='{name}']")

    def _result_row(self, name):
        """Returns locator for a row in the results matching the employee's first name."""
        return (By.XPATH, f"//div[@class='oxd-table-card']//div[text()='{name.split()[0]}']")

    def go_to_employee_list(self):

        current_url = self.driver.current_url
        if "viewEmployeeList" in current_url:
            print("Already on Employee List page. Skipping navigation.")
            return

        print("Navigating to Employee List...")
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
        self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_LIST_TAB)).click()
        print("Employee List page loaded.")

    def search_and_verify_employee(self, full_name):

        print(f"Searching for: {full_name}")

        name_field = self.wait.until(EC.presence_of_element_located(self.EMPLOYEE_NAME_FIELD))
        name_field.clear()
        name_field.send_keys(full_name)

        try:
            suggestion = self.wait.until(EC.element_to_be_clickable(self._suggestion_box(full_name)))
            suggestion.click()
            print(f"Selected suggestion: {full_name}")
        except Exception as e:
            print(f"No suggestion found for: {full_name} or element not clickable. Error: {e}")
            return

        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

        try:
            self.wait.until(EC.presence_of_element_located(self._result_row(full_name)))
            print(f"Employee found in results: {full_name}")
        except Exception as e:
            print(f" Employee NOT found in results: {full_name}. Error: {e}")

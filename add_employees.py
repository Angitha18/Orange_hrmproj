from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage.basepage import BasePage


class AddEmployees(BasePage):

    ADD_EMPLOYEE_MENU = (By.XPATH, "//a[text()='Add Employee']")
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    MIDDLE_NAME_FIELD = (By.NAME, "middleName")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    EMPLOYEE_ID_FIELD = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div//input")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    FORM_LOADER = (By.CLASS_NAME, "oxd-form-loader")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def open_add_employee_form(self):

        self.wait.until(EC.element_to_be_clickable(self.ADD_EMPLOYEE_MENU)).click()
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_FIELD))
        print("Add Employee form opened.")

    def fill_employee_details(self, emp_data):

        print("Filling employee details...")

        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_FIELD)).send_keys(emp_data["firstName"])
        self.wait.until(EC.presence_of_element_located(self.MIDDLE_NAME_FIELD)).send_keys(emp_data["middleName"])
        self.wait.until(EC.presence_of_element_located(self.LAST_NAME_FIELD)).send_keys(emp_data["lastName"])

        emp_id_input = self.wait.until(EC.presence_of_element_located(self.EMPLOYEE_ID_FIELD))
        emp_id_input.clear()
        emp_id_input.send_keys(emp_data["id"])

        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        print(f"Employee {emp_data['firstName']} saved.")

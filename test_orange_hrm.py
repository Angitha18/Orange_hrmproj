from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.login import LoginPage
from pageObjects.add_employees import AddEmployees
from pageObjects.personal_details import PersonalDetails
from pageObjects.employee_list import EmployeeListPage

# ✅ Inline test data
employees = [
    {
        "firstName": "Shyma",
        "middleName": "S",
        "lastName": "Satheesh",
        "id": "00900",
        "nationality": "Indian",
        "maritalStatus": "Single",
        "dob": "1997-01-01"
    },
    {
        "firstName": "Shreya",
        "middleName": "Ram",
        "lastName": "Kumar",
        "id": "00511",
        "nationality": "Indian",
        "maritalStatus": "Single",
        "dob": "1996-02-02"
    },
    {
        "firstName": "Adhi",
        "middleName": "Roy",
        "lastName": "Acharya",
        "id": "00366",
        "nationality": "Indian",
        "maritalStatus": "Single",
        "dob": "1995-03-03"
    }
]

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


login_page = LoginPage(driver)
add_employee_page = AddEmployees(driver)
personal_details_page = PersonalDetails(driver)
employee_list_page = EmployeeListPage(driver)


login_page.login("Admin", "admin123")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
)


WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))
).click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Add Employee']"))
)


for emp in employees:
    print(f"\n🧾 Adding: {emp['firstName']} {emp['middleName']} {emp['lastName']} - ID: {emp['id']}")
    add_employee_page.open_add_employee_form()
    add_employee_page.fill_employee_details(emp)
    personal_details_page.select_nationality(emp.get("nationality", "Indian"))
    personal_details_page.select_marital_status(emp.get("maritalStatus", "Single"))
    personal_details_page.set_date_of_birth(emp.get("dob", "2000-01-01"))
    personal_details_page.save_personal_details()
    personal_details_page.wait_for_page_load()


employee_list_page.go_to_employee_list()


names_to_verify = [
    f"{emp['firstName']} {emp['middleName']} {emp['lastName']}" for emp in employees
]

print("\n🔍 Verifying Employees in Employee List:")
for full_name in names_to_verify:
    employee_list_page.search_and_verify_employee(full_name)


driver.quit()

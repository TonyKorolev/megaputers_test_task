from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
import csv, time

class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def read_name_in_staff(self):
        arr = []
        with open("employees_name.csv", "r") as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                arr.append(row)
        return arr
    
    def should_be_input_employee(self):
        assert self.is_element_present(*BasePageLocators.LOCATOR_INPUT_EMPLOYEE)

    def should_be_find_button(self):
        assert self.is_element_present(*BasePageLocators.LOCATOR_BUTTON_FIND)

    def enter_name_employee(self, str):
        input = self.browser.find_element(*BasePageLocators.LOCATOR_INPUT_EMPLOYEE)
        input.send_keys(str)
    
    def find_employees_sertificate(self):
        button = self.browser.find_element(*BasePageLocators.LOCATOR_BUTTON_FIND)
        button.click()

    def clear_enter_name_employee(self):
        input = self.browser.find_element(*BasePageLocators.LOCATOR_INPUT_EMPLOYEE)
        input.clear()

    def get_count_sertificate_employee(self):
        if (self.is_element_present(*BasePageLocators.LOCATOR_COUNT_SERTIFICATE) == True):
            count_selector = self.browser.find_element(*BasePageLocators.LOCATOR_COUNT_SERTIFICATE)
            count = int(count_selector.get_attribute("rowspan"))
        else: 
            count = 0
        return count
    
    def get_name_sertificate_employee(self, num):
        if (self.is_element_present(*BasePageLocators.LOCATOR_NAME_SERTIFICATE) == True):
            if (num == 1):
                name_sertificate = self.browser.find_element(*BasePageLocators.LOCATOR_NAME_SERTIFICATE).text
            else:
                name_sertificate = self.browser.find_element(By.CSS_SELECTOR, f"#text1 > table > tbody > tr:nth-child({num}) > td:nth-child(1)").text
        else:
            name_sertificate = ""
        return name_sertificate


    def get_date_sertificate_employee(self, num):
        if (self.is_element_present(*BasePageLocators.LOCATOR_NAME_SERTIFICATE) == True):
            if (num == 1):
                date_sertificate = self.browser.find_element(*BasePageLocators.LOCATOR_DATE_SERIFICATE).text
            else:
                date_sertificate = self.browser.find_element(By.CSS_SELECTOR, f"#text1 > table > tbody > tr:nth-child({num}) > td:nth-child(2)").text
        else:
            date_sertificate = ""
        return date_sertificate

    def write_employee_with_sertificate(self, arr):
        csv.register_dialect("my_dialect", delimiter=",", lineterminator="\r")
        with open("employees_name_with_sertificate.csv", "w") as file:
            file_writer = csv.writer(file,"my_dialect")
            for i in range(len(arr)):
                BasePage.should_be_input_employee(self)
                BasePage.should_be_find_button(self)
                BasePage.enter_name_employee(self, arr[i])
                BasePage.find_employees_sertificate(self)
                time.sleep(5)
                BasePage.clear_enter_name_employee(self)
                count_sertifiacte = BasePage.get_count_sertificate_employee(self)
                if (count_sertifiacte != 0):
                    for j in range(count_sertifiacte):
                        name_employee = arr[i]
                        name_sertificate = BasePage.get_name_sertificate_employee(self, j+1)
                        date_sertificate = BasePage.get_date_sertificate_employee(self, j+1)
                        file_writer.writerow([name_employee, name_sertificate, date_sertificate])
                else: 
                    file_writer.writerow([name_employee, "", ""])
    



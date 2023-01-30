from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
import csv, time

class BasePage():
    # инициализация браузера, ссылки
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    # открытие ссылки
    def open(self):
        self.browser.get(self.url)
    
    # проверка наличия элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    # проверка наличия поля в поисковике для ввода ФИО сотрудника
    def should_be_input_employee(self):
        assert self.is_element_present(*BasePageLocators.LOCATOR_INPUT_EMPLOYEE)

    # проверка наличия кнопки "Найти"
    def should_be_find_button(self):
        assert self.is_element_present(*BasePageLocators.LOCATOR_BUTTON_FIND)

    # ввод ФИО сотрудника в поле поисковика
    def enter_name_employee(self, str):
        input = self.browser.find_element(*BasePageLocators.LOCATOR_INPUT_EMPLOYEE)
        input.send_keys(str)
    
    # клик по кнопке "Найти"
    def find_employees_sertificate(self):
        button = self.browser.find_element(*BasePageLocators.LOCATOR_BUTTON_FIND)
        button.click()

    # удаление введенных ранее ФИО сотрудника
    def clear_enter_name_employee(self):
        input = self.browser.find_element(*BasePageLocators.LOCATOR_INPUT_EMPLOYEE)
        input.clear()

    # считывание количества сертификатов у сотрудника, при отсутствии возвращает 0
    def get_count_sertificate_employee(self):
        if (self.is_element_present(*BasePageLocators.LOCATOR_COUNT_SERTIFICATE) == True):
            count_selector = self.browser.find_element(*BasePageLocators.LOCATOR_COUNT_SERTIFICATE)
            count = int(count_selector.get_attribute("rowspan"))
        else: 
            count = 0
        return count
    
    # считывание наименования сертификата
    def get_name_sertificate_employee(self, num):
        if (self.is_element_present(*BasePageLocators.LOCATOR_NAME_SERTIFICATE) == True):
            if (num == 1):
                name_sertificate = self.browser.find_element(*BasePageLocators.LOCATOR_NAME_SERTIFICATE).text
            else:
                name_sertificate = self.browser.find_element(By.CSS_SELECTOR, f"#text1 > table > tbody > tr:nth-child({num}) > td:nth-child(1)").text
        else:
            name_sertificate = ""
        return name_sertificate

    # считывание даты сертификата
    def get_date_sertificate_employee(self, num):
        if (self.is_element_present(*BasePageLocators.LOCATOR_NAME_SERTIFICATE) == True):
            if (num == 1):
                date_sertificate = self.browser.find_element(*BasePageLocators.LOCATOR_DATE_SERIFICATE).text
            else:
                date_sertificate = self.browser.find_element(By.CSS_SELECTOR, f"#text1 > table > tbody > tr:nth-child({num}) > td:nth-child(2)").text
        else:
            date_sertificate = ""
        return date_sertificate

    # считывание ФИО сотрудников с файла "employees_name"
    # и запись ФИО сотрудника и его сертификатов в файл "employees_name_with_sertificate.csv"
    def write_employee_with_sertificate(self):
        arr = []
        with open("employees_name.csv", "r") as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                arr.append(row)
        csv.register_dialect("my_dialect", delimiter=",", lineterminator="\r")
        with open("employees_name_with_sertificate.csv", "w") as file:
            file_writer = csv.writer(file,"my_dialect")
            for i in range(len(arr)):
                name_employee = str(arr[i])[2:-2]
                BasePage.should_be_input_employee(self)
                BasePage.should_be_find_button(self)
                BasePage.enter_name_employee(self, name_employee)
                BasePage.find_employees_sertificate(self)
                time.sleep(5)
                BasePage.clear_enter_name_employee(self)
                count_sertifiacte = BasePage.get_count_sertificate_employee(self)
                if (count_sertifiacte != 0):
                    for j in range(count_sertifiacte):
                        name_sertificate = " " + BasePage.get_name_sertificate_employee(self, j+1)
                        date_sertificate = " " + BasePage.get_date_sertificate_employee(self, j+1)
                        file_writer.writerow([name_employee, name_sertificate, date_sertificate])
                else: 
                    file_writer.writerow([name_employee, "", ""])
    



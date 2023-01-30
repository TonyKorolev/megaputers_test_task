from selenium.webdriver.common.by import By

class BasePageLocators():
    LOCATOR_INPUT_EMPLOYEE = (By.ID, "certificates-text")
    LOCATOR_BUTTON_FIND = (By.ID, "certificates-button")
    LOCATOR_COUNT_SERTIFICATE = (By.CSS_SELECTOR, "#text1 > table > tbody > tr > td:nth-child(1)")
    LOCATOR_NAME_SERTIFICATE = (By.CSS_SELECTOR, "#text1 > table > tbody > tr > td:nth-child(2)")
    LOCATOR_DATE_SERIFICATE = (By.CSS_SELECTOR, "#text1 > table > tbody > tr > td:nth-child(3)")
from .pages.base_page import BasePage
# import read_name as rn
import pytest, csv, time




def test_get_employee_with_sertificate(browser):
    link = "https://www.megaputer.ru/produkti/sertifikat/"
    page = BasePage(browser, link)
    page.open()
    page.write_employee_with_sertificate()

from .pages.base_page import BasePage
# import read_name as rn
import pytest, csv, time




def test_get_employee_with_sertificate(browser):
    link = "https://www.megaputer.ru/produkti/sertifikat/"
    page = BasePage(browser, link)
    page.open()
    nameArr = page.read_name_in_staff()
    page.write_employee_with_sertificate(nameArr)

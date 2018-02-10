# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/2/10 下午5:30

from selenium import webdriver
import time
from PageObject.addressBook import *
from util.Excel import *
from ProjectVar.var import *
from Conf import login_info


def add_contact(driver, name="", email="", is_star=True, mobile="", other_info=""):
    ap = AddressPage(driver)
    ap.add_contact_button().click()
    time.sleep(2)
    ap.contact_name().send_keys(name)
    ap.contact_email().send_keys(email)
    if is_star == "True":
        ap.contact_is_star().click()
    ap.contact_mobile().send_keys(mobile)
    ap.contact_other_info().send_keys(other_info)
    ap.contact_save_button().click()
    time.sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    login(driver, login_info.username, login_info.password)
    visit_address_page(driver)
    add_contact(driver, "fosterwu", "201773733@qq.com", True, "13533333333", u"光荣之路")
    driver.quit()

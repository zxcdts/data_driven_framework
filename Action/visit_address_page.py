# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/2/10 下午5:07
from selenium import webdriver
import time
from PageObject.home_page import *
from login import *
from Conf import login_info


def visit_address_page(driver):
    hp = HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="/Users/zhangbingwei/chromedriver")
    login(driver, login_info.username, login_info.password)
    visit_address_page(driver)

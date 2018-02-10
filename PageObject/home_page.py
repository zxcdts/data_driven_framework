# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/2/10 下午4:35
import time
from util.ObjectMap import *
from util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from Action.login import *
from Conf import login_info


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.login_page_items = self.parse_config_file.getItemsFromSection("126mail_homepage")
        # print self.login_page_items

    def address_book_page_link(self):
        locateType, locateExpression = self.login_page_items['home_page.addressbook'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)


if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path="/Users/zhangbingwei/chromedriver")
    login(driver, login_info.username, login_info.password)
    hp = HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(5)

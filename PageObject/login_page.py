# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/2/10 下午4:12

import time
from util.ObjectMap import *
from util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from selenium import webdriver
from Conf import login_info


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.login_page_items = self.parse_config_file.getItemsFromSection("126mail_login")
        # print self.login_page_items

    def login_frame(self):
        locateType, locateExpression = self.login_page_items['login_page.frame'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def username(self):
        locateType, locateExpression = self.login_page_items['login_page.username'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def password(self):
        locateType, locateExpression = self.login_page_items['login_page.password'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def loginbutton(self):
        locateType, locateExpression = self.login_page_items['login_page.loginbutton'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def switch_to_loginframe(self):
        self.driver.switch_to.frame(self.login_frame())

    def input_username(self, username):
        self.username().send_keys(username)

    def input_password(self, password):
        self.password().send_keys(password)

    def loginbutto_click(self):
        self.loginbutton().click()

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="/Users/zhangbingwei/chromedriver")
    driver.get("http://mail.126.com")
    time.sleep(2)
    lp = LoginPage(driver)
    lp.switch_to_loginframe()
    time.sleep(2)
    lp.input_username(login_info.username)
    lp.input_password(login_info.password)
    lp.loginbutto_click()
    driver.quit()
    time.sleep(4)

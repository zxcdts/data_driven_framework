# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/2/10 下午4:49
from selenium import webdriver
from util.Log import *
from util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
from Conf import login_info
from ProjectVar.var import *


def login(driver, username, password):
    driver.get("http://mail.126.com")
    time.sleep(2)
    lp = LoginPage(driver)
    lp.switch_to_loginframe()
    time.sleep(2)
    lp.input_username(username)
    lp.input_password(password)
    lp.loginbutto_click()
    time.sleep(4)
    info("login successfully!")
    print date_time_chinese()


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    login(driver, login_info.username, login_info.password)

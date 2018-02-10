# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/2/10 下午4:45
import time
from util.ObjectMap import *
from util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from Action.login import *
from Action.visit_address_page import *
from Conf import login_info

class AddressPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection(
            "126mail_addcontactspage")
        # print self.login_page_items

    def add_contact_button(self):
        locateType, locateExpression = self.login_page_items['addcontacts_page.createcontactsbtn'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_name(self):
        locateType, locateExpression = self.login_page_items['addcontacts_page.contactpersonname'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_email(self):
        locateType, locateExpression = self.login_page_items['addcontacts_page.contactpersonemail'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_is_star(self):
        locateType, locateExpression = self.login_page_items['addcontacts_page.starcontacts'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_mobile(self):
        locateType, locateExpression = self.login_page_items['addcontacts_page.contactpersonmobile'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_other_info(self):
        locateType, locateExpression = self.login_page_items['addcontacts_page.contactpersoncomment'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def contact_save_button(self):
        locateType, locateExpression = self.login_page_items['addcontacts_page.savecontaceperson'].split(">")
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="/Users/zhangbingwei/chromedriver")
    login(driver, login_info.username, login_info.password)
    hp = HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(5)
    ap = AddressPage(driver)
    ap.add_contact_button().click()
    time.sleep(2)
    ap.contact_name().send_keys("gloryroad")
    ap.contact_email().send_keys("87393932@qq.com")
    ap.contact_is_star().click()
    ap.contact_mobile().send_keys("1322222222")
    ap.contact_other_info().send_keys(u"光荣之路")
    ap.contact_save_button().click()
    time.sleep(5)
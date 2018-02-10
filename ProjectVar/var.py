# -*- coding: utf-8 -*-
import os

project_path = os.path.dirname(os.path.dirname(__file__))
Page_Object_Path = project_path + '/Conf/PageObjectRepository.ini'
Logger_conf_path = project_path + '/Conf/Logger.conf'
# 邮件文件
test_data_excel_path = project_path + "/TestData/126邮箱联系人.xlsx"
username_col_no = 1
password_col_no = 2
is_executed_col_no = 4
test_result_col_no = 6
exception_info_col_no = 7
assert_keyword_col_no = 6
chrome_driver_path = '/Users/zhangbingwei/chromedriver'
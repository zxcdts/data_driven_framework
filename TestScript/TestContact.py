# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/2/10 下午5:37

from selenium import webdriver
from util.Log import *
from util.Excel import *
from util.FormatTime import *
import time
from Action.visit_address_page import *
from Action.add_contact import *
from Action.login import *
from ProjectVar.var import *
import sys

reload(sys)
sys.setdefaultencoding("utf8")
# 取出所有行，使用切片获取非第一行的所有行，因为第一行是标题，所以不用取
# 遍历每一行，然后使用读取这一行单元格的方法，将用户名和密码读取到两个
# 变量里面，然后传到login方法中，调用即可
pe = ParseExcel(test_data_excel_path)
pe.set_sheet_by_index(0)
print pe.get_default_name()
rows = pe.get_all_rows()[1:]
for id, row in enumerate(rows):
    if row[is_executed_col_no].value == 'y':
        username = row[username_col_no].value
        password = row[password_col_no].value
        # print "username:", row[username_col_no].value
        # print "password:", row[password_col_no].value
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        try:
            login(driver, username, password)
            visit_address_page(driver)
            time.sleep(3)
            pe.set_sheet_by_index(1)
            print pe.get_default_name()
            print 'all rows', pe.get_all_rows()
            test_data_result_flag = True
            for id2, row in enumerate(pe.get_all_rows()):
                if row[7].value == 'y':
                    try:
                        print id2
                        add_contact(driver, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value)
                        # 此处存在疑问，别人的代码是id+2能够写入正确的值
                        pe.write_cell_content(id2 + 1, 9, time_chinese())
                        print "assert word:", row[assert_keyword_col_no].value
                        assert row[assert_keyword_col_no].value in driver.page_source
                        pe.write_cell_content(id2 + 1, 10, "pass")
                    except Exception, e:
                        info(u'异常信息' + e.message)
                        pe.write_cell_content(id2 + 1, 9, time_chinese())
                        pe.write_cell_content(id2 + 1, 10, "fail")
                        test_data_result_flag = False
                else:
                    pe.write_cell_content(id2 + 1, 10, u'忽略')
                    continue
            if test_data_result_flag == True:
                pe.set_sheet_by_index(0)
                pe.write_cell_content(id + 2, test_result_col_no, u"成功")
            else:
                pe.set_sheet_by_index(0)
                pe.write_cell_content(id + 2, test_result_col_no, u"失败")
        except Exception, e:
            info(u'异常信息' + e.message)

        driver.quit()
    else:
        print u'第' + str(id + 1) + u'行数据未执行'
        pe.set_sheet_by_index(0)
        pe.write_cell_content(id + 2, test_result_col_no, u'忽略')
        continue

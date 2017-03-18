__author__ = 'xueyan'
# coding:utf-8
import unittest
import sys, os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import HomePage
from model import Model
from Page.multiCoursePlanHourPage import multiCoursePlanHourPage

# from model.Model import  DataHelper
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from  selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoAlertPresentException
from  selenium.common.exceptions import NoAlertPresentException


class MultiCoursePlan(BaseLogin, multiCoursePlanHourPage, HomePage):
    # 通过一对多消课管理列表"排课"按钮进入排课
    def testoMultiCoursePlan_001(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击一对多管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[3]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        #查询学员姓名
        driver.find_element_by_xpath("//input[@st-search='myCrmCustomerStudentGroupFilter.group_no']").send_keys("班组琪琪01")
        self.wait
        #操作列表
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        # 点击班组排课操作
        driver.find_element_by_xpath("//a[contains(text(),'班组排课')]").click()
        self.wait
        self.multiCourse01()
if __name__ == '__main__':
    unittest.main(verbosity=2)

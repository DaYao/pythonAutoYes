__author__ = 'xueyan'
# coding:utf-8
import unittest
import sys, os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import HomePage
from model import Model
from Page.singleCoursePlanHourPage import SingleCoursePlanHourPage
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


class ListHourCoursePlan60(BaseLogin, SingleCoursePlanHourPage, HomePage):
    # 通过一对一消课管理列表"排课"按钮进入排课
    def testListHourCoursePlan60_001(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击一对一消课管理列表
        click = driver.find_element_by_xpath("//*[@id='CoursePlanManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        #点击"排课"按钮
        driver.find_element_by_xpath("//a[@ng-click='showPaikeView(3,0)']").click()
        self.wait
        # 切换到学员排课tab
        driver.find_element_by_xpath("//*[@id='body']/div[4]/div/div/div[2]/span[2]").click()
        self.wait
        #查询学员姓名
        driver.find_element_by_xpath("//input[@name='myCrmCustomerStudentFilter.name']").clear()
        driver.find_element_by_xpath("//input[@name='myCrmCustomerStudentFilter.name']").send_keys("自动化测试一对一")
        self.wait
        #选中单选按钮
        driver.find_element_by_xpath("//label[@class='radio-vr']").click()
        self.wait
        self.hourCours01()

if __name__ == '__main__':
    unittest.main(verbosity=2)

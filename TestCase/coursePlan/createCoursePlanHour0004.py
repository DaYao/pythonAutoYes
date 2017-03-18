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
from Page.listeningCoursePlanPage import ListeningCoursePlanPage
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


class StudentTimeHourCoursePlan60(BaseLogin, SingleCoursePlanHourPage,ListeningCoursePlanPage, HomePage):
    #通过学生时间表进入排课，学员排课
    #@unittest.skip('test')
    def testListHourCoursePlan60_001(self):
        driver = self.driver
        studentName = '自动化测试一对一'
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学生时间表
        click = driver.find_element_by_xpath("//a[contains(text(),'学生时间表')]")
        ActionChains(driver).click(click).perform()
        self.wait
        #点击"选择学生"按钮
        allTeacher=driver.find_element_by_xpath("//button[@ng-click='tcl.selectedPersons()']")
        allTeacher.click()
        self.wait
        #录入学生姓名
        driver.find_element_by_xpath("//*[@id='studentName']").send_keys(studentName)
        self.wait
        #查询
        driver.find_element_by_xpath("//a[@ng-click='getLeadsStudentInfoByFilter()']").click()
        self.wait
        #点击"确定"按钮
        driver.find_element_by_xpath("//input[@name='studentRadio']").click()
        self.wait
        #点击查询
        driver.find_element_by_xpath("//button[@id='keydown-query']").click()
        for i in range(5):
            driver.find_element_by_xpath("//button[@id='keydown-query']").send_keys(Keys.DOWN)
        # 鼠标移入操作
        driver.find_element_by_xpath("//*[@id='body']/div[2]/div[2]/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/ul/li/main/span").click()
        self.wait
        #点击"排课"
        driver.find_element_by_xpath("//*[@id='body']/div[2]/div[2]/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/ul/li/main/div/ul/li/a").click()
        self.wait
        valitext=self.hourCours01()
        context_expxcted="排课成功!共排课1次(1小时)"
        self.assertEqual(context_expxcted, valitext)
if __name__ == '__main__':
    unittest.main(verbosity=2)

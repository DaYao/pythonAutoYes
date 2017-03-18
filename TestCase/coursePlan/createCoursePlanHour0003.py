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


class TeacherTimeHourCoursePlan60(BaseLogin, SingleCoursePlanHourPage,ListeningCoursePlanPage, HomePage):
    # 通过教师时间表进入排课，学员排课
    @unittest.skip('test')
    def testListHourCoursePlan60_001(self):
        driver = self.driver
        studentName = '自动化测试一对一'
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'首页')]")).perform()
        self.wait
        # 点击教师时间表
        click = driver.find_element_by_xpath("//*[@id='InvitationDetailManagement']/li[3]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        #点击"全部教师"按钮
        allTeacher=driver.find_element_by_xpath("//button[@ng-click='tcl.selectedPersons()']")
        allTeacher.click()
        self.wait
        #录入教师姓名
        driver.find_element_by_xpath("//*[@id='teacherName']").send_keys("黄临凤")
        self.wait
        #选中checkbox
        driver.find_element_by_xpath("//tr[@ng-repeat='row in teacherLists']/td[1]/input").click()
        self.wait
        #点击"确定"按钮
        driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        #键盘下拉
        for i in range(30):
            driver.find_element_by_xpath("//button[@ng-click='tcl.selectedPersons()']").send_keys(Keys.DOWN)
        #点击查询按钮
        driver.find_element_by_xpath("//button[@id='refe']").click()
        self.wait
        for i in range(10):
            driver.find_element_by_xpath("//button[@id='refe']").send_keys(Keys.DOWN)
        # 鼠标移入操作
        driver.find_element_by_xpath("//*[@id='tableTime']/tbody/tr[2]/td[3]/ul/li/main/span").click()
        self.wait
        #点击"排课"
        driver.find_element_by_xpath("//*[@id='tableTime']/tbody/tr[2]/td[3]/ul/li/main/div/ul/li[1]/a").click()
        self.wait
        #查询学员姓名
        driver.find_element_by_xpath("//input[@name='myCrmCustomerStudentFilter.name']").send_keys(studentName)
        self.wait
        #选中单选按钮
        driver.find_element_by_xpath("//label[@class='radio-vr']").click()
        self.wait
        valitext=self.hourCours01()
        context_expxcted="排课成功!共排课1次(1小时)"
        self.assertEqual(context_expxcted, valitext)
# 通过教师时间表进入排课，试听排课
    @unittest.skip('test')
    def testListHourCoursePlan60_002(self):
            driver = self.driver
            studentName='试听排课自动化'
            ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'首页')]")).perform()
            self.wait
            # 点击教师时间表
            click = driver.find_element_by_xpath("//*[@id='InvitationDetailManagement']/li[3]/a")
            ActionChains(driver).click(click).perform()
            self.wait
            # 点击"全部教师"按钮
            allTeacher = driver.find_element_by_xpath("//button[@ng-click='tcl.selectedPersons()']")
            allTeacher.click()
            self.wait
            # 录入教师姓名
            driver.find_element_by_xpath("//*[@id='teacherName']").send_keys("黄临凤")
            self.wait
            # 选中checkbox
            driver.find_element_by_xpath("//tr[@ng-repeat='row in teacherLists']/td[1]/input").click()
            self.wait
            # 点击"确定"按钮
            driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
            # 键盘下拉
            for i in range(30):
                driver.find_element_by_xpath("//button[@ng-click='tcl.selectedPersons()']").send_keys(Keys.DOWN)
            # 点击查询按钮
            driver.find_element_by_xpath("//button[@id='refe']").click()
            self.wait
            for i in range(10):
                driver.find_element_by_xpath("//button[@id='refe']").send_keys(Keys.DOWN)
            # 鼠标移入操作
            driver.find_element_by_xpath("//*[@id='tableTime']/tbody/tr[2]/td[3]/ul/li/main/span").click()
            self.wait
            # 点击"试听排课"
            driver.find_element_by_xpath("//*[@id='tableTime']/tbody/tr[2]/td[3]/ul/li/main/div/ul/li[2]/a").click()
            self.wait
            # 查询学员姓名
            driver.find_element_by_xpath("//input[@name='myCrmCustomerStudentFilter.name']").send_keys(studentName)
            self.wait
            # 选中单选按钮
            driver.find_element_by_xpath("//label[@class='radio-vr']").click()
            self.wait
            valitext = self.listenPlan01()
            context_expxcted = "排课成功!共排课1次(1小时)"
            self.assertEqual(context_expxcted, valitext)
    '''消课'''
    def testListHourCoursePlan60_003(self):
        driver = self.driver
        studentName = '自动化测试一对一'
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'首页')]")).perform()
        self.wait
        # 点击教师时间表
        click = driver.find_element_by_xpath("//*[@id='InvitationDetailManagement']/li[3]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        #点击"全部教师"按钮
        allTeacher=driver.find_element_by_xpath("//button[@ng-click='tcl.selectedPersons()']")
        allTeacher.click()
        self.wait
        #录入教师姓名
        driver.find_element_by_xpath("//*[@id='teacherName']").send_keys("王兰")
        self.wait
        #选中checkbox
        driver.find_element_by_xpath("//tr[@ng-repeat='row in teacherLists']/td[1]/input").click()
        self.wait
        #点击"确定"按钮
        driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        #键盘下拉
        for i in range(30):
            driver.find_element_by_xpath("//button[@ng-click='tcl.selectedPersons()']").send_keys(Keys.DOWN)
        #点击查询按钮
        driver.find_element_by_xpath("//button[@id='refe']").click()
        self.wait
        for i in range(10):
            driver.find_element_by_xpath("//button[@id='refe']").send_keys(Keys.DOWN)
        # 鼠标移入操作
        driver.find_element_by_xpath("//*[@id='tableTime']/tbody/tr[2]/td[3]/ul/li/main/span").click()
        self.wait
        #点击"排课"
        driver.find_element_by_xpath("//*[@id='tableTime']/tbody/tr[1]/td[4]/ul/li[1]/main/span").click()
        self.wait
        driver.find_element_by_xpath("//*[@id='tableTime']/tbody/tr[1]/td[4]/ul/li[1]/main/div/ul/div[2]/a[1]").click()
        self.wait
        driver.find_element_by_xpath("//button[@class='confirm']").click()
        self.wait

if __name__ == '__main__':
    unittest.main(verbosity=2)

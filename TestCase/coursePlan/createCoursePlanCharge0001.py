__author__ = 'xueyan'
# coding:utf-8
import  unittest
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import  HomePage
from model import Model
from Page.singleCoursePlanChargePage import singleCoursePlanChargePage
from ddt import  ddt,data,unpack
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import  NoSuchElementException
from  selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import  NoAlertPresentException
from  selenium.common.exceptions import NoAlertPresentException

class StudentChargeCoursePlan60(BaseLogin,singleCoursePlanChargePage,HomePage):
    #通过学员管理入口进入排课
    #@unittest.skip('test')
    def testChargeCoursePlan60_001(self):
        studentName='自动化一对一储值'
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        self.wait
        # 点击学员列表操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        # 点击排课操作
        # driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[6]/a").click()
        driver.find_element_by_xpath("//a[contains(text(),'排课')]").click()

        self.wait
        #调用公共一对一排课界面
        self.docoursePlan01()
    #@unittest.skip('test')
    def atestChargeCoursePlan60_002(self):
        studentName='自动化一对一储值'
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        self.wait
        # 点击学员列表操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        # 点击排课操作
        # driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[6]/a").click()
        driver.find_element_by_xpath("//a[contains(text(),'排课')]").click()
        self.wait
        #调用公共一对一排课界面
        self.docoursePlan02()
if __name__=='__main__':
	unittest.main(verbosity=2)

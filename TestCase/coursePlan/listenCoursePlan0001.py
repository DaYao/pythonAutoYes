__author__ = 'xueyan'
# coding:utf-8
import  unittest
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import  HomePage
from model import Model
from Page.listeningCoursePlanPage import ListeningCoursePlanPage
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

class ListeningCoursePlan(BaseLogin,ListeningCoursePlanPage,HomePage):
    #@unittest.skip('test')
    def testListeningCoursePlan_001(self):
        studentName='试听课排课自动测试'
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'首页')]")).perform()
        self.wait
        # 点击我的意向客户列表
        click = driver.find_element_by_xpath("//*[@id='LeadsStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//input[@st-search='myCrmLeadsStudentFilter.name']").send_keys(studentName)
        self.wait
        # 点击列表操作
        driver.find_element_by_xpath("//a[@id='nw+0']/span").click()
        self.wait
        # 点击排课操作
        driver.find_element_by_xpath("//a[@ng-click='addCoursePlanInfo(row,3)']").click()
        self.wait
        #调用公共排课界面
        self.listenPlan01()

if __name__=='__main__':
	unittest.main(verbosity=2)

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


class schoolTimeHourCoursePlan60(BaseLogin, HomePage):
    #通过校区时间表，排课消课
    #@unittest.skip('test')
    def testListHourCoursePlan60_001(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学生时间表
        click = driver.find_element_by_xpath("//a[contains(text(),'校区时间表')]")
        ActionChains(driver).click(click).perform()
        self.wait
        #查询
        driver.find_element_by_xpath("//*[@id='body']/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[2]/td[2]/ul/li/main/span/p").click()
        self.wait
        #点击"确定"按钮
        driver.find_element_by_xpath("//*[@id='body']/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[2]/td[2]/ul/li/main/div/ul/div[2]/a[1]").click()
        self.wait
        driver.find_element_by_xpath("//button[@class='confirm']").click()

if __name__ == '__main__':
    unittest.main(verbosity=2)

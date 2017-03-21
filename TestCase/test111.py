__author__ = 'xueyan'
# coding:utf-8
import unittest
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import HomePage
from Page.createStudentOrderPage import CreateStudentOrderPage
from Page.orderVerifyPage import VerifyOrderPage
from Page.chargeBackPage import ChargeBackPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class GroupDemo2(BaseLogin,CreateStudentOrderPage,VerifyOrderPage,ChargeBackPage,HomePage):

    def testcreateGroup_011(self):
        driver = self.driver
        try:
            click = driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")
            ActionChains(driver).click(click).perform()
            self.wait5
        except NoSuchElementException as e:
            print(e)

        try:
            driver.find_element_by_link_text("学员管理").click()
            self.wait5
        except NoSuchElementException as e:
            print(e)

        driver.find_element_by_xpath("//*[@id='noMar']").send_keys('lhf031103')
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        driver.find_element_by_link_text("录订单").click()
        self.wait

        orderNo = '2017031736'
        self.TestAddOrder(orderNo)
        self.wait5
        self.testVerifyOrder(orderNo)
        #self.wait1
        #self.testChargeBack()

if __name__ == '__main__':
    unittest.main(verbosity=2)

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
from Page.OrderRefundPage import OrderRefundPage
from Page.presentOrderPage import presentOrderPage
from model.pyMysqlDB import myDB
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import  datetime

class OrderOperation(BaseLogin,CreateStudentOrderPage,VerifyOrderPage,ChargeBackPage,OrderRefundPage,presentOrderPage,HomePage):

    studentOrderName = 'lhf032201'
    def createOrderNo(self):
        now = datetime.datetime.now()
        orderNoBase = 'lhf'+now.strftime('%Y%m%d')
        return orderNoBase

    @unittest.skip('test')
    def testOrderAdd(self):#添加订单
        orderNo = self.createOrderNo()+'01'
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

        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(self.studentOrderName)
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        driver.find_element_by_link_text("录订单").click()
        self.wait


        self.TestAddOrder(orderNo)
        self.wait5
        self.testVerifyOrder(orderNo)

    @unittest.skip('test')
    def testOrderChargeBack(self):#订单退单
        orderNo = self.createOrderNo() + '02'
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

        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(self.studentOrderName)
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        driver.find_element_by_link_text("录订单").click()
        self.wait

        self.TestAddOrder(orderNo)
        self.wait5
        self.testVerifyOrder(orderNo)
        self.wait5
        self.testChargeBack()

    @unittest.skip('test')
    def testRefundVerify(self):#订单退费
        orderNo = self.createOrderNo() + '03'

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

        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(self.studentOrderName)
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        driver.find_element_by_link_text("录订单").click()
        self.wait

        self.TestAddOrder(orderNo)
        self.wait5
        self.testVerifyOrder(orderNo)
        self.wait10

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

        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(self.studentOrderName)
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='showReturnView(row)']").click()
        self.wait5
        self.testRefund()
        self.wait5

        try:
            click = driver.find_element_by_xpath("//a[@href='#/sos-admin/refund']")
            ActionChains(driver).click(click).perform()
            self.wait1
            ActionChains(driver).click(click).perform()
            self.wait5
        except NoSuchElementException as e:
            print(e)

        self.refundOrderVerify(orderNo)

    def testPresentOrder(self):
        #returnNum = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        #studentName = '自动化学员' + returnNum
        #teacherName = '自动化教师' + returnNum
        orderNo = self.createOrderNo() + '04'

        driver = self.driver
        self.testPresent(self.studentOrderName)


if __name__ == '__main__':
    unittest.main(verbosity=2)

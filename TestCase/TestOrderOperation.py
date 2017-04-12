__author__ = 'lhf'
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
from Page.transferOrderPage import TransferOrderPage
from Page.changeOrderRemaind import ChangeOrderRemindPage

from model.pyMysqlDB import myDB
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import  datetime
from selenium.webdriver.common.keys import Keys

class OrderOperation(BaseLogin,CreateStudentOrderPage,VerifyOrderPage,ChargeBackPage,OrderRefundPage,presentOrderPage,TransferOrderPage,ChangeOrderRemindPage,HomePage):

    studentOrderName = 'lhf032201'

    def createOrderNo(self):
        now = datetime.datetime.now()
        orderNoBase = 'lhf'+now.strftime('%Y%m%d')
        return orderNoBase

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
        self.wait5


        self.AddOrder(orderNo)
        self.wait5
        self.VerifyOrder(orderNo)


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
        self.wait5

        self.AddOrder(orderNo)
        self.wait5
        self.VerifyOrder(orderNo)
        self.wait5
        self.ChargeBack()

    def testRefundVerify(self):#订单退费
        returnNum = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        studentName = '自动化学员' + returnNum
        orderNo = 'pay' + returnNum
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

        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait5
        driver.find_element_by_xpath("//a[@ng-click='showReturnView(row)']").click()
        self.wait5
        self.Refund()
        self.wait5

        click = driver.find_element_by_xpath("//a[@data-target='#RefundManagement']")
        ActionChains(driver).click(click).perform()
        self.wait1
        ActionChains(driver).click(click).perform()
        self.wait1
        ActionChains(driver).click(click).perform()
        self.wait1

        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        ActionChains(self.driver).key_up(Keys.DOWN).perform()
        self.wait1

        click = driver.find_element_by_xpath("//a[@href='#/sos-admin/refund']")
        ActionChains(driver).click(click).perform()
        self.wait1

        self.refundOrderVerify(orderNo)

        myDB.connect_function(myDB, 'func_del_autoInsertStudent(' + returnNum + ')')

    def testPresentOrder(self):#返课
        returnNum = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        studentName = '自动化学员' + returnNum

        self.Present(studentName)
        self.wait5
        self.PresentVerify(studentName)

        myDB.connect_function(myDB, 'func_del_autoInsertStudent(' + returnNum + ')')

    def testTrasferOrder(self):
        returnNum = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        studentOrderName = '自动化学员' + returnNum
        self.wait1
        returnNum1 = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        transferNewStudent = '自动化学员' + returnNum1

        self.Transfer(studentOrderName,transferNewStudent)
        self.wait5
        self.TransferVerify(studentOrderName)
        self.TransferSum(studentOrderName,transferNewStudent)
        self.wait5
        self.TransferReverse()

        myDB.connect_function(myDB,'func_del_autoInsertStudent('+ returnNum+ ')')
        myDB.connect_function(myDB, 'func_del_autoInsertStudent(' + returnNum1 + ')')

    def testChangeOrder(self):
        returnNum = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        studentName = '自动化学员' + returnNum

        self.ChangeOrder(studentName)

        myDB.connect_function(myDB, 'func_del_autoInsertStudent(' + returnNum + ')')

if __name__ == '__main__':
    unittest.main(verbosity=2)

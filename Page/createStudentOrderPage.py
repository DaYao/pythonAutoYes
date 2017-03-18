__author__ = 'liuhf'
# coding:utf-8
import sys,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .BasePage import WebUI
import datetime


class CreateStudentOrderPage(WebUI):
    orderID = (By.XPATH,"//*[@id = 'orderNo']")#合同编号
    name = (By.NAME,'name')#姓名及电话
    type = (By.ID,'orderType')#业绩类型
    startDate = 'contractStartDate' #签约时间
    endDate = 'contractEndDate'#到期时间
    orderRule = (By.ID,'orderRule')#课时规则
    selectCourse = (By.XPATH,"//button[@ng-click='selectCourse()']")#选择课程
    selectOneCourse = "//label[@class='checkbox-bg']"#选择课程复选框
    selectSubject = (By.XPATH,"//span[@ng-click='showTriggar($index)']")#选择科目按钮
    selectOneSubject = (By.XPATH,"//li[@ng-click='setCourseSubject(row,subject)']")#选择科目
    selectSubjectConfirm = (By.XPATH,"//a[@ng-click='showTriggar()']")#选择科目确定按钮
    selectSubjectDo = (By.XPATH,"//button[@ng-click='doSelectCourse()']")#选择课程保存按钮
    price = (By.XPATH,"//input[@ng-value='row.actualPrice']")#单价
    count = (By.XPATH,"//input[@ng-value='row.originalNum']")#数量
    discount = (By.XPATH,"//input[@ng-change='resetPayCondition();']")#直减优惠
    addCharge = (By.XPATH, "//a[@ng-click='addShouFei(1)']")#添加收费
    thisPrice = (By.ID,"supplementaryFee")#本次收费
    priceDate = (By.XPATH, "input[ng-model='order.payDate'")#收费日期
    chargeConfirm = (By.XPATH,"//button[@ng-click='saveTempChargeRecord()']")#收费确定按钮
    priceAttention = (By.XPATH,"//div[@class='sa-confirm-button-container']/button")
    saveOrder = (By.XPATH,"//button[@ng-click='saveOrder()']")#订单保存按钮
    saveConfirm = (By.XPATH,"//button[@class='confirm']")#确认按钮

    def SetTime(self,element,tTimeValue):
        tTime = "$(\"input[id="+ element +"]\").removeAttr('readonly');$(\"input[id="+ element +"]\").attr('value',\"" + tTimeValue + "\").trigger('change')"
        self.driver.execute_script(tTime)


    def TestAddOrder(self,contranctID):#添加订单

        self.findElement(*self.orderID).send_keys(contranctID)
        self.findElement(*self.type).send_keys('续费')

        now = datetime.datetime.now()
        tTimeNow = now.strftime('%Y-%m-%d')
        self.SetTime(self.startDate,tTimeNow)


        oneMonth = datetime.timedelta(days=30)
        nextMonth = now + oneMonth
        tTimeNextMonth = nextMonth.strftime('%Y-%m-%d')

        self.SetTime(self.endDate,tTimeNextMonth)

        self.findElement(*self.orderRule).send_keys('1小时')
        self.wait1
        click = self.driver.find_element_by_xpath("//button[@ng-click='selectCourse()']")
        ActionChains(self.driver).click(click).perform()

        self.wait1
        self.driver.find_elements_by_xpath("//label[@class='checkbox-bg']").pop(1).click()

        self.findElement(*self.selectSubject).click()
        self.wait1
        self.driver.find_elements_by_xpath("//li[@ng-click='setCourseSubject(row,subject)']").pop(1).click()

        self.findElement(*self.selectSubjectConfirm).click()
        self.findElement(*self.selectSubjectDo).click()
        self.wait1

        self.findElement(*self.price).send_keys('100')
        self.findElement(*self.count).send_keys('100')
        self.findElement(*self.discount).send_keys('0')

        self.wait1
        self.findElement(*self.addCharge).click()

        self.findElement(*self.thisPrice).send_keys('10000')


        tTime = "$(\"input[ng-model='order.payDate']\").removeAttr('readonly');$(\"input[ng-model='order.payDate']\").attr('value',\"" + tTimeNow + "\").trigger('change')"
        self.driver.execute_script(tTime)

        click = self.findElement(*self.chargeConfirm)
        ActionChains(self.driver).click(click).perform()
        self.wait1
        ActionChains(self.driver).click(click).perform()

        #click = self.findElement(*self.priceAttention)
        #ActionChains(self.driver).click(click).perform()

        '''ActionChains(self.driver).key_down(Keys.DOWN).perform()
        ActionChains(self.driver).key_up(Keys.DOWN).perform()
        self.wait1
        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        ActionChains(self.driver).key_up(Keys.DOWN).perform()
        self.wait1
        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        ActionChains(self.driver).key_up(Keys.DOWN).perform()
        self.wait1
        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        ActionChains(self.driver).key_up(Keys.DOWN).perform()
        self.wait1'''
        self.wait1
        attributeValue = "document.getElementsByTagName('button')[11].removeAttribute('disabled')"
        self.driver.execute_script(attributeValue)

        self.findElement(*self.saveOrder).click()
        self.wait1
        self.findElement(*self.saveConfirm).click()
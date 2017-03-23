__author__ = 'liuhf'
# coding:utf-8
import sys,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .BasePage import WebUI
import datetime
from selenium.webdriver.support.select import Select

class OrderRefundPage(WebUI):
    refundButton = (By.XPATH,"//tbody[@ng-show='!isNormalOrderLoading']/tr[1]/td[28]/a[2]")#订单列表退费按钮
    refundReason = (By.XPATH,"//select[@ng-model='refundOrder.refundReasonType']")#退费原因
    refundConfirm = (By.XPATH,"//button[@ng-click='refundConfirm()']")#提交退费
    oKConfirm = (By.XPATH,"//button[@class ='confirm']")#成功验证

    #退费审核
    orderNoInput = (By.XPATH,"//div[@class='overflow-x']/table/thead/tr[2]/th[1]/input")#合同编号
    orperationButton = (By.XPATH,"//a[@id='nw+0']")#操作按钮
    refundVerify = (By.XPATH, "//li[@ng-click='auditOrder(row)']")  # 审核
    refundOk = (By.XPATH, "//button[@ng-click='auditRefund()']")  # 确认退款
    refundOkConfirm = (By.XPATH, "//button[@class='confirm']")  # 确定

    def testRefund(self):#订单退费
        click =self.findElement(*self.refundButton)
        ActionChains(self.driver).click(click).perform()
        self.wait
        s1 = Select(self.findElement(*self.refundReason))
        s1.select_by_index(1)
        self.wait5

        click = self.findElement(*self.refundConfirm)
        ActionChains(self.driver).click(click).perform()
        self.wait5
        self.findElement(*self.oKConfirm).click()

    def refundOrderVerify(self,orderno):
        self.findElement(*self.orderNoInput).send_keys(orderno)
        self.wait5
        self.findElement(*self.orperationButton).click()
        self.wait
        self.findElement(*self.refundVerify).click()
        self.wait5
        self.findElement(*self.refundOk).click()
        self.wait5
        self.findElement(*self.refundOkConfirm).click()
        self.wait
        self.findElement(*self.refundOkConfirm).click()
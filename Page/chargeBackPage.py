__author__ = 'liuhf'
# coding:utf-8
import sys,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .BasePage import WebUI
import datetime

class ChargeBackPage(WebUI):
    orderNo = (By.XPATH, "//input[@ng-model='orderFilter.orderNo']")  # 订单编号
    selectMore = (By.XPATH, "//a[contains(text(),'更多查询条件')]")  # 查询更多
    queryButton = (By.XPATH, "//*[@id='keydown-query']")  # 查询按钮
    orperateButton = (By.XPATH, "//span[@class='glyphicon glyphicon-caozuo']")  # 操作按钮
    chargeBack = (By.XPATH, "//a[contains(text(),'退单')]")  # 退单操作按钮
    backMount = (By.XPATH, "//input[@ng-model='order.refundAmount']")  # 退单金额
    BackButton = (By.XPATH, "//button[@ng-click='refund()']")  # 退单按钮
    confirmButton = (By.XPATH, "//button[@class='confirm']")  # 确认退单

    def testChargeBack(self):
        '''click = self.driver.find_element_by_xpath("//a[contains(text(),'首页')]")
        ActionChains(self.driver).click(click).perform()
        self.wait1
        self.driver.find_element_by_link_text("普通订单列表").click()
        self.wait5

        click = self.findElement(*self.selectMore)
        ActionChains(self.driver).click(click).perform()
        self.wait

        self.findElement(*self.orderNo).send_keys(ddnumber)
        self.wait1
        self.findElement(*self.queryButton).click()
        self.wait5'''
        click = self.findElement(*self.orperateButton)
        ActionChains(self.driver).click(click).perform()
        self.wait

        click = self.findElement(*self.chargeBack)
        ActionChains(self.driver).click(click).perform()
        self.wait1

        self.findElement(*self.backMount).send_keys('1')
        self.wait1
        click = self.findElement(*self.BackButton)
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.findElement(*self.confirmButton).click()
        self.wait5
        self.findElement(*self.confirmButton).click()

__author__ = 'liuhf'
# coding:utf-8
import sys,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
from .BaseLoginPage import BaseLogin
from .BasePage import WebUI
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By

class VerifyOrderPage(WebUI):
    studentName = (By.XPATH, "//input[@ng-model='orderFilter.name']")  # 学员姓名
    orderNo = (By.XPATH,"//input[@ng-model='orderFilter.orderNo']") #订单编号
    selectMore = (By.XPATH,"//a[contains(text(),'更多查询条件')]")#查询更多
    queryButton = (By.XPATH,"//*[@id='keydown-query']")#查询按钮
    orperateButton = (By.XPATH, "//span[@class='glyphicon glyphicon-caozuo']")  # 操作按钮
    verifyOrder = (By.XPATH, "//li[@ng-click='auditOrder(row)']") #审核按钮
    verifyButton = (By.XPATH,"//button[@ng-click='allPayOrder()']")#审核通过
    confirmButton = (By.XPATH,"//button[@class='confirm']")#确认审核通过

    def VerifyOrder(self,ddnumber):
        click = self.driver.find_element_by_xpath("//a[contains(text(),'首页')]")
        ActionChains(self.driver).click(click).perform()
        self.wait5
        self.driver.find_element_by_link_text("普通订单列表").click()
        self.wait10

        click = self.findElement(*self.selectMore)
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.findElement(*self.orderNo).send_keys(ddnumber)
        self.wait1
        self.findElement(*self.queryButton).click()
        self.wait10
        click = self.findElement(*self.orperateButton)
        ActionChains(self.driver).click(click).perform()
        self.wait1

        click = self.findElement(*self.verifyOrder)
        ActionChains(self.driver).click(click).perform()
        self.wait5
        click = self.findElement(*self.verifyButton)
        ActionChains(self.driver).click(click).perform()
        self.wait5
        self.findElement(*self.confirmButton).click()
        self.wait5
        valitext = self.driver.find_element_by_xpath("//h2[contains(text(),'操作成功')]").text
        context_expxcted = "操作成功"
        self.assertEqual(context_expxcted, valitext)
        self.findElement(*self.confirmButton).click()

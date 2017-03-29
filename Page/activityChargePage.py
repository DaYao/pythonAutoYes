__author__ = 'liuhf'
# coding:utf-8
import sys,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .BasePage import WebUI
import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class ActivityChargePage(WebUI):
    totalMount = (By.XPATH,"//input[@name='totalConsumers']")# 总消课数量
    distributeButton = (By.XPATH, "//a[@ng-click='autoDistribution()']")  # 自动分配
    chargeReason = (By.XPATH,"//input[@ng-model='setParam.consumerRseason']")#消课原因
    chargeSubmit = (By.XPATH, "//button[@ng-click='submitAudit()']")  # 提交审核
    chargeConfirm = (By.XPATH, "//button[@ng-if='!hasNext']")  # 提交成功提示

    #活动消课审核
    chargeName = (By.XPATH, "//input[@ng-model='mtSeach.student_name']")  # 学员姓名
    queryNameButton = (By.XPATH, "//a[@ng-click='callServerrecordFilterChange()']")  # 查询按钮
    chargeOrperateButton = (By.XPATH, "//span[@class='glyphicon glyphicon-caozuo']")  # 操作按钮
    verifyCharge = (By.XPATH, "//a[@ng-click='Activityconsume(row)']")  # 审核按钮
    chargeButton = (By.XPATH, "//button[@class='confirm']")  # 确认审核通过

    def ActivityCharge(self,activityChargeName):
        self.wait5
        click = self.driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.driver.find_element_by_link_text("学员管理").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='noMar']").send_keys(activityChargeName)
        self.wait
        self.driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        self.driver.find_element_by_xpath("//div[@class='ui-bubble']/div/ul/li[7]").click()
        self.wait5

        self.findElement(*self.totalMount).send_keys('100')
        self.wait
        click = self.findElement(*self.distributeButton)
        ActionChains(self.driver).click(click).perform()
        self.wait5

        now = datetime.datetime.now()
        tTimeNow = now.strftime('%Y-%m-%d')
        tTime = "$(\"input[ng-model='setParam.consumersTime']\").removeAttr('readonly');$(\"input[ng-model='setParam.consumersTime']\").attr('value',\"" + tTimeNow + "\").trigger('change')"
        self.driver.execute_script(tTime)

        self.findElement(*self.chargeReason).send_keys('出国游学')
        self.wait1
        self.findElement(*self.chargeSubmit).click()
        self.wait1

        self.findElement(*self.chargeConfirm).click()

    def ActivityChargeVerify(self,activityChargeName):
        click = self.driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")
        ActionChains(self.driver).click(click).perform()
        self.wait10

        click = self.driver.find_element_by_xpath("//a[contains(text(),'活动消课')]")
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.findElement(*self.chargeName).send_keys(activityChargeName)
        self.wait5

        self.findElement(*self.queryNameButton).click()
        self.wait5
        click = self.findElement(*self.chargeOrperateButton)
        ActionChains(self.driver).click(click).perform()
        self.wait1
        click = self.findElement(*self.verifyCharge)
        ActionChains(self.driver).click(click).perform()
        self.wait1
        click = self.findElement(*self.chargeButton)
        ActionChains(self.driver).click(click).perform()

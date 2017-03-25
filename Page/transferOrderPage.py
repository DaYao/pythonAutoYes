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

class TransferOrderPage(WebUI):
    orderSelect = (By.XPATH, "//table[@st-table='orderTransferAvailableOrders']/tbody/tr/td/input")  # 订单选择
    transferStudent = (By.XPATH, "//input[@ng-model='order.name']")  # 受让学员姓名
    searchStudent = (By.XPATH,"//form[@name='addTransferForm']/div/div[3]/div/div[2]/div/a")#查找按钮
    searchStudentName = (By.XPATH,"//input[@ng-model='schoolCrmLeadsStudentFilter.name']")#查找学生
    queryStudent = (By.XPATH,"//a[@ng-click='getLeadsListFiter()']")#查询按钮
    leadsSelect = (By.XPATH,"//label[@ng-click='selectOneMt(row)']")#选择学员
    selectOk = (By.XPATH,"//button[@ng-click='selectTransferLeads()']")#确定
    lectureType = (By.XPATH, "//div[@ng-if='order.transferWay == 1']/div[2]/div[2]/div/select")  # 授课方式
    saveTransfer = (By.XPATH, "//button[@ng-click='saveTransferOrder()']")  # 保存
    transferConfirm = (By.XPATH, "//button[@class='confirm']")  # 成功提示

    #转课审核
    oldNameInput = (By.XPATH, "//input[@st-search='name']")  # 原学员姓名
    verifyTransferButton = (By.XPATH, "//a[@ng-click='editTransferOrder(row)']")  # 审核按钮
    transferOk = (By.XPATH, "//button[@ng-click='auditOrderTransferPass()']")  # 审核通过按钮
    transferOkConfirm = (By.XPATH, "//button[@class='confirm']")  # 确定

    def Transfer(self,transferName,transferNewStudent):
        self.wait5
        click = self.driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.driver.find_element_by_link_text("学员管理").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='noMar']").send_keys(transferName)
        self.wait
        self.driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        self.driver.find_element_by_link_text("转课").click()
        self.wait5

        self.findElement(*self.orderSelect).click()
        self.wait1

        '''name = "document.getElementById('name').removeAttribute('readonly')"
        self.driver.execute_script(name)
        name1 = "$(\"input[id='name']\").attr('value',\"" + transferNewStudent + "\").trigger('change')"
        self.driver.execute_script(name1)'''
        self.findElement(*self.searchStudent).click()
        self.wait5
        self.findElement(*self.searchStudentName).send_keys(transferNewStudent)

        click = self.findElement(*self.queryStudent)
        ActionChains(self.driver).click(click).perform()
        self.wait5
        self.findElement(*self.leadsSelect).click()
        self.wait1
        self.findElement(*self.selectOk).click()
        self.wait5

        self.findElement(*self.lectureType).send_keys('一对一')
        self.wait1
        click = self.findElement(*self.saveTransfer)
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.findElement(*self.transferConfirm).click()

    def TransferVerify(self,tansferOldName):
        click = self.driver.find_element_by_xpath("//a[contains(text(),'首页')]")
        ActionChains(self.driver).click(click).perform()
        self.wait10

        click = self.driver.find_element_by_xpath("//ul[@id='OrderManagement']/li[2]")
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.findElement(*self.oldNameInput).send_keys(tansferOldName)
        self.wait5
        self.findElement(*self.verifyTransferButton).click()
        self.wait5
        self.findElement(*self.transferOk).click()
        self.wait
        self.findElement(*self.transferOkConfirm).click()
        self.wait
        self.findElement(*self.transferOkConfirm).click()
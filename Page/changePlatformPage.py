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

class ChangePlatformPage(WebUI):
    otherPlatform = (By.XPATH,"//input[@id='departName']")# 转入校区
    selectDepartment = (By.XPATH,"//treecontrol[@class='tree-classic ng-isolate-scope']/ul/li[1]/i[1]")#选择部门
    selectNextDepartment = (By.XPATH, "//treecontrol[@class='tree-classic ng-isolate-scope']/ul/li[1]/treeitem/ul/li[1]/i[1]")  # 选择下级部门
    selectSchool = (By.XPATH,"//span[contains(text(),'北京和平西桥校区')]")
    saveSelection = (By.XPATH,"//button[@ng-click='departmentSelected()']")#保存选择校区
    changePlatformAmount = (By.XPATH, "//input[@id='changePlatformAmount']")  # 转出平台业绩
    changeDate = (By.XPATH,"//input[@ng-model='platform.changePlatformDate']")#转平台日期
    saveChange = (By.XPATH, "//button[@ng-click='savePlatformChange()']")  # 提交
    changeConfirm = (By.XPATH, "//button[@class='confirm']")  # 操作成功提示

    #转平台审核
    verifyChange = (By.XPATH, "//a[contains(text(),'审核')]")  # 审核按钮
    changeButton = (By.XPATH, "//form[@name='addPlatForm']/div/div[3]/div/button[2]")  # 确认审核通过
    verifyConfirm = (By.XPATH, "//button[@class='confirm']")  # 操作成功
    def ChangePlatform(self,changePlatformName):
        self.wait5
        click = self.driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.driver.find_element_by_link_text("学员管理").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='noMar']").send_keys(changePlatformName)
        self.wait
        self.driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        self.driver.find_element_by_xpath("//div[@class='ui-bubble']/div/ul/li[11]").click()
        self.wait5

        self.findElement(*self.otherPlatform).click()
        self.wait1
        self.findElement(*self.selectDepartment).click()
        self.wait1
        self.findElement(*self.selectNextDepartment).click()
        self.wait1
        click = self.findElement(*self.selectSchool)
        ActionChains(self.driver).click(click).perform()
        self.wait1
        self.findElement(*self.saveSelection).click()
        self.wait

        self.findElement(*self.changePlatformAmount).send_keys('2000')
        self.wait

        now = datetime.datetime.now()
        tTimeNow = now.strftime('%Y-%m-%d')
        tTime = "$(\"input[ng-model='platform.changePlatformDate']\").removeAttr('readonly');$(\"input[ng-model='platform.changePlatformDate']\").attr('value',\"" + tTimeNow + "\").trigger('change')"
        self.driver.execute_script(tTime)

        click = self.findElement(*self.saveChange)
        ActionChains(self.driver).click(click).perform()
        self.wait1
        valitext = self.driver.find_element_by_xpath("//h2[contains(text(),'转平台操作已成功')]").text
        context_expxcted = "转平台操作已成功"
        self.assertEqual(context_expxcted, valitext)
        self.findElement(*self.changeConfirm).click()

    def ChangePlatformVerify(self,changePlatformName):
        self.wait5
        click = self.driver.find_element_by_xpath("//a[contains(text(),'首页')]")
        ActionChains(self.driver).click(click).perform()
        self.wait1
        click = self.driver.find_element_by_xpath("//a[@data-target='#OrderManagement']")
        ActionChains(self.driver).click(click).perform()
        self.wait1
        ActionChains(self.driver).click(click).perform()

        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        ActionChains(self.driver).key_up(Keys.DOWN).perform()
        self.wait1
        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        ActionChains(self.driver).key_up(Keys.DOWN).perform()
        self.wait5
        click = self.driver.find_element_by_xpath("//ul[@id='OrderManagement']/li[5]")
        ActionChains(self.driver).click(click).perform()
        self.wait5

        count = 1
        pos = 0
        n = 1
        count = len(self.driver.find_elements_by_xpath("//tr[@ng-repeat='row in PlatformListFrom']"))

        while (n <= count):
            tableLines = "//table[@st-pipe='getCrmPlatformList']/tbody/tr[" + str(n) + "]/td[1]"
            name = self.driver.find_element_by_xpath(tableLines).text
            tableLines = "//table[@st-pipe='getCrmPlatformList']/tbody/tr[" + str(n) + "]/td[3]"
            status = self.driver.find_element_by_xpath(tableLines).text

            if ((changePlatformName == name) and (status == "待转出审核")):
                pos = n
                break;
            n = n + 1

        operation = "//a[@id='nw+" + str(n - 1) + "']"
        click = self.driver.find_element_by_xpath(operation)
        ActionChains(self.driver).click(click).perform()
        self.wait

        click = self.findElement(*self.verifyChange)
        ActionChains(self.driver).click(click).perform()
        self.wait5
        click = self.findElement(*self.changeButton)
        ActionChains(self.driver).click(click).perform()
        self.wait

        valitext = self.driver.find_element_by_xpath("//h2[contains(text(),'操作成功')]").text
        context_expxcted = "操作成功"
        self.assertEqual(context_expxcted, valitext)
        click = self.findElement(*self.verifyConfirm)
        ActionChains(self.driver).click(click).perform()
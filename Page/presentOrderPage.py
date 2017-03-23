__author__ = 'liuhf'
# coding:utf-8
import sys,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .BasePage import WebUI
import datetime
from selenium.webdriver.support.select import Select

class presentOrderPage(WebUI):
    orderCkeck = (By.XPATH, "//input[@name='orderRestitution']")  # 订单选择
    productType = (By.XPATH, "//select[@name='productId']")  # 产品类型
    courseType = (By.XPATH, "//select[@name='courseTypeId']")  # 课程类型
    courseGrade = (By.XPATH, "//select[@name='gradeId']")  # 课程年级
    subjectProduct = (By.XPATH, "//select[@name='subjectId']")  # 产品科目
    presentNum = (By.XPATH,"//input[@name='originalNum']") #返课课时
    subjectReason = (By.XPATH, "//select[@name='reason']")  # 返课原因
    addCource = (By.XPATH, "//button[@ng-click='addRestitutionCourse()']")#添加课程
    saveCource = (By.XPATH, "//button[@ng-click='saveRestitution()']")  # 保存课程
    addConfirm = (By.XPATH, "//button[@class='confirm']")  # 成功提示

    def testPresent(self,presentOrderName):
        self.wait
        click = self.driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")
        ActionChains(self.driver).click(click).perform()
        self.wait5

        self.driver.find_element_by_link_text("学员管理").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='noMar']").send_keys(presentOrderName)
        self.wait
        self.driver.find_element_by_xpath("//a[@ng-click='getStudentBySome()']").click()
        self.wait5
        self.driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        self.driver.find_element_by_link_text("返课").click()
        self.wait5

        self.findElement(*self.orderCkeck).click()
        self.wait1
        self.findElement(*self.productType).send_keys('常规课程')
        self.wait1
        self.findElement(*self.courseType).send_keys('金牌课程')
        self.wait1
        self.findElement(*self.courseGrade).send_keys('小学一年级')
        self.wait1
        self.findElement(*self.subjectProduct).send_keys('英语')
        self.wait1
        self.findElement(*self.presentNum).send_keys('2')
        self.wait1
        self.findElement(*self.subjectReason).send_keys('保障学提升赠课')
        self.wait1
        self.findElement(*self.addCource).click()
        self.wait5

        self.findElement(*self.saveCource).click()
        self.wait5
        self.findElement(*self.addConfirm).click()
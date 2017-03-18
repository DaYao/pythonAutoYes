__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# from selenium import webdriver
from selenium.webdriver.common.by import By
from .homePage import HomePage
from .BasePage import WebUI
from .BaseLoginPage import BaseLogin
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

'''删除排课页面'''
class DeletePlanHourPage(WebUI,BaseLogin):
    subjectId_loc=(By.XPATH, "//*[@name='subjectId']")#选择科目
    radiomultiPlan_loc=(By.XPATH, "//div[@ng-click='checkedShowCycle('week')'/input']")#选择定制排课时间规则
    radioSinglePlan_loc=(By.XPATH, "//div[@ng-click='checkedShowCycle('day')'/input']")#选择精准日期排课
    singleTeacher_loc=(By.XPATH, "//a[text()='陈雪薇']")#选择单个老师


    #学员管理列表删除
    def singleDelete01(self,studentName):
        driver=self.driver
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        driver.find_element_by_xpath("//*[@id='noMar']").clear()
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        self.wait
        driver.find_element_by_xpath(
            "//*[@id='body']/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/table/tbody[1]/tr[1]/td[12]/a").click()
        self.wait
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'排课记录')]")).perform()
        self.wait
        driver.find_element_by_xpath("//*[@id='nwt+0']/span").click()
        self.wait
        # 删除消课
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[3]/a").click()
        self.wait
        driver.find_element_by_class_name("confirm").click()
        self.wait
if __name__=='__main__':
    pass


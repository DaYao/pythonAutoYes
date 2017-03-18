__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# from selenium import webdriver
from selenium.webdriver.common.by import By
from .homePage import HomePage
from .BasePage import WebUI
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

'''消课取消页面'''
class CancelPlanCoursePage(WebUI):

    unSatisfy_loc=(By.XPATH, "//a[contains(text(),'不满意')]']")#不满意
    dealError_loc=(By.XPATH, "//a[contains(text(),'消课错误')]")#选择教师
    other_loc=(By.XPATH, "//a[contains(text(),'其他原因')]")#上课时间
    otherReason_loc=(By.XPATH, "//textarea[@id='invitationContent']")#请输入原因
    submitButton_loc=(By.XPATH, "//button[@type='submit']")#确定
    continueCancel_loc=(By.XPATH, "//button[@type='button']")#取消
    submitButton2_loc=(By.XPATH, "//button[@class='submit']")#二次确定
    continueCancel2_loc=(By.XPATH, "//button[@class='cancel']")#二次取消
    valiText_loc=(By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']/h2")#排课成功
    ok_loc=(By.XPATH, "//button[@class='submit']")#ok


    def getUnSatisfyField(self):
        self.findElement(*self.unSatisfy_loc).click()
        self.wait
    def getDealErrorField(self):
        self.findElement(*self.dealError_loc).click()
        self.wait
    def getOtherField(self):
        self.findElement(*self.other_loc).click()
        self.wait
    def getOtherReasonField(self, reason):
        self.findElement(*self.otherReason_loc).send_keys(reason)
    def getSubmitButtonField(self):
        self.findElement(*self.submitButton_loc).click()
        self.wait
    def getContinueCancelField(self):
        self.findElement(*self.continueCancel_loc).click()
        self.wait
    def getSubmitButton2Field(self):
        self.findElement(*self.submitButton2_loc).click()
        self.wait
    def getContinueCancel2Field(self):
        self.findElement(*self.continueCancel2_loc).click()
        self.wait
    def geOkField(self):
        self.findElement(*self.ok_loc).click()
        self.wait
    def getValiTextField(self):
        return self.findElement(*self.valiText_loc).text

    ##不满意
    def cancelPlan01(self):
        self.unSatisfy_loc()
        self.getSubmitButtonField()
        self.getSubmitButton2Field
        valiText=self.getValiTextField()
        return valiText
if __name__=='__main__':
    pass


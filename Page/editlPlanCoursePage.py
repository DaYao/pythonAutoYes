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

'''编辑排课页面'''
class EditPlanChargePage(WebUI):
    subjectId_loc=(By.XPATH, "//*[@ng-model='OmsCoursePlanVoForEdit.subjectId']")#科目
    selectTeacher_loc=(By.XPATH, "//table[@st-pipe='getCSShooleTeacherByFilters']/tbody/tr/td/input")#选择教师
    starTime_loc=(By.XPATH, "//input[@ng-model='select.time']")#上课时间
    startLen_loc=(By.XPATH, "//select[@name='select.timeSize']")#选择上课时长
    SubmitButton_loc=(By.XPATH, "//button[@ng-click='EditCoursePlanNow()']")#确定
    continueCancel_loc=(By.XPATH, "//button[@ng-click='channleEdit()']") # 取消
    valiText_loc=(By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']/h2")#排课成功

    def getSubjectIdField(self, startIndex):
        selectLen = Select(self.findElement(*self.subjectId_loc))
        selectLen.select_by_index(startIndex)
        self.wait
    def getSelectTeacherField(self):
        self.findElement(*self.selectTeacher_loc).click()
        self.wait
    def getStarTimeField(self, putStarHour):
        self.findElement(*self.starTime_loc).send_keys(putStarHour)
    def getStartLenField(self, startIndex):
        selectLen = Select(self.findElement(*self.startLen_loc))
        selectLen.select_by_index(startIndex)
    def getSubmitButtonField(self):
        self.findElement(*self.SubmitButton_loc).click()
        self.wait
    def getContinueCancelField(self):
        self.findElement(*self.continueCancel_loc).click()
        self.wait
    def getValiTextField(self):
        return self.findElement(*self.valiText_loc).text
    def getStartDateField(self,startValue):
        startTime = "$(\"input[id='startDate']\").removeAttr('readonly');$(\"input[id='startDate']\").attr('value', \"" + startValue + "\" ).trigger('change')"
        return startTime
    def EditPlan01(self):
        self.getSubjectIdField(2)
        self.getSelectTeacherField()
        startValue = '2016-06-21'
        startTime=self.getPTimeStartField(startValue)
        self.driver.execute_script(startTime)
        self.starTime_loc(12)
        self.startLen_loc(3)
        self.SubmitButton_loc()
        valiText=self.getValiTextField()
        return valiText
if __name__=='__main__':
    pass


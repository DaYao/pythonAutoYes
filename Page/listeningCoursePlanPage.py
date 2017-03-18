__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from selenium.webdriver.common.by import By
from .homePage import HomePage
from .BasePage import WebUI
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
'''试听课排课页面'''
class ListeningCoursePlanPage(WebUI):
    subjectId_loc=(By.XPATH, "//*[@name='subjectId']")#选择科目
    radiomultiPlan_loc=(By.XPATH, "//div[@ng-click='checkedShowCycle('week')'/input']")#选择定制排课时间规则
    radioSinglePlan_loc=(By.XPATH, "//div[@ng-click='checkedShowCycle('day')'/input']")#选择精准日期排课
    singleTeacher_loc=(By.XPATH, "//a[text()='陈雪薇']")#选择单个老师
    #startDate2_loc=(By.XPATH,"")#精准排课选择上课日期
    starttime2_loc=(By.XPATH,"//input[@ng-model='select.time1']")#精准排课选择上课时间时
    startmini2_loc=(By.XPATH,"//input[@ng-model='select.time2']")#精准排课选择上课时间分
    timeSize2_loc=(By.XPATH,"//select[@id='timeSize']")#精准排课选择上课时长
    selectTeacher_loc=(By.XPATH, "//div[@ng-if='subjectTeacherGroup.length']/div/div[2]/div[1]/a")#选择教师
    clickAddTime_loc=(By.XPATH,"//a[@ng-click='showAddCoursePlanTime()']")#点击添加日期
    selectWeek_loc=(By.XPATH, "//input[@ng-model='selected.dayShowOfWeek1']")#选择星期一
    putStarHour_loc=(By.XPATH, "//input[@id='time1']")#键入上课开始时
    putEndMinute_loc=(By.XPATH, "//input[@id='time2']")#键入上课开始分
    startLen_loc=(By.XPATH, "//select[@name='timeSize']")#选择上课时长
    timeOk_loc=(By.XPATH, "//button[@ng-click='addPlans()']")#点击确定ok
    thisWeek_loc=(By.XPATH, '''//span[@ng-click="show.judgeType('0')"]''')#点击本周
    SubmitButton_loc=(By.XPATH, "//button[@ng-click='show.submitPlan()']")#排课提交
    SubmitButton02_loc=(By.XPATH, "//button[@class='confirm']")
    confirmValiText_loc=(By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']/h2")
    continueCancel_loc=(By.XPATH, "//button[@class='cancel']") # 点击"OK,不继续排课"

    def getSubjectIdField(self, startIndex):
        selectLen = Select(self.findElement(*self.subjectId_loc))
        selectLen.select_by_index(startIndex)
        self.wait
    def getRadiomultiPlanField(self):
        self.findElement(*self.radiomultiPlan_loc).click()
        self.wait
    def getRadioSingleField(self):
        self.findElement(*self.radioSinglePlan_loc).click()
        self.wait
    def getSingleTeacherField(self):
        self.findElement(*self.singleTeacher_loc).click()
        self.wait
    def getStartDate2Field(self,startValue):
        startTime = "$(\"input[ng-model='select.startDate']\").removeAttr('readonly');$(\"input[ng-model='select.startDate']\").attr('value', \"" + startValue + "\" ).trigger('change')"
        return startTime
    def getStarttime2Field(self, starttime):
        self.findElement(*self.starttime2_loc).send_keys(starttime)
    def getStartmini2Field(self, startmini):
        self.findElement(*self.startmini2_loc).send_keys(startmini)
    def getTimeSize2Field(self, startIndex):
        selectLen = Select(self.findElement(*self.timeSize2_loc))
        selectLen.select_by_index(startIndex)
    def getSelectTeacherField(self):
        self.findElement(*self.selectTeacher_loc).click()
        self.wait
    def getClickAddTimeField(self):
        self.findElement(*self.clickAddTime_loc).click()
        self.wait
    def getSelectWeekField(self):
        self.findElement(*self.selectWeek_loc).click()
    def getPutStarHourField(self, putStarHour):
        self.findElement(*self.putStarHour_loc).send_keys(putStarHour)
    def getPutEndMinuteField(self, putEndMinute):
        self.findElement(*self.putEndMinute_loc).send_keys(putEndMinute)
    def getStartLenField(self, startIndex):
        selectLen = Select(self.findElement(*self.startLen_loc))
        selectLen.select_by_index(startIndex)
    def getTimeOkField(self):
        self.findElement(*self.timeOk_loc).click()
        self.wait
    def getThisWeekField(self):
        self.findElement(*self.thisWeek_loc).click()
        self.wait
    def getSubmitButtonField(self):
        self.findElement(*self.SubmitButton_loc).click()
        self.wait
    def getSubmitButton02Field(self):
        self.findElement(*self.SubmitButton02_loc).click()
        self.wait
    def getConfirmValiTextField(self):
        return self.findElement(*self.confirmValiText_loc).text
    def getContinueCancelField(self):
        self.findElement(*self.continueCancel_loc).click()
        self.wait
    def coursePlan01(self,studentName,teacherName):
        self.docoursePlan(studentName,teacherName)
        return HomePage(self.driver)
    def listenPlan01(self):
        self.getSubjectIdField(2)
        self.getSingleTeacherField()
        startTime =self.getStartDate2Field("2017-11-11")
        self.driver.execute_script(startTime)
        self.getStarttime2Field('12')
        self.getStartmini2Field('12')
        self.getTimeSize2Field(2)
        self.getSubmitButtonField()
        self.getSubmitButton02Field()
        valiText=self.getConfirmValiTextField()
        self.getContinueCancelField()
        return valiText
if __name__=='__main__':
    pass


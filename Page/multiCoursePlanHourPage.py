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

'''班组课时排课页面'''
class multiCoursePlanHourPage(WebUI):

    selectCourse01_loc=(By.XPATH, "//*[@id='orderInfo']/tr[1]/td[2]/a")#选择课程
    selectCourse02_loc=(By.XPATH, "//*[@id='orderInfo']/tr[2]/td[2]/a")#选择课程
    selectCourse03_loc=(By.XPATH, "//*[@id='orderInfo']/tr[3]/td[2]/a")#选择课程
    courseConfirm_loc=(By.XPATH,"//button[@ng-click='selectOrderCourse()']")#点击课程确认
    selectTeacher_loc=(By.XPATH, "//div[@ng-if='subjectTeacherGroup.length']/div/div[2]/div[1]/a")#选择教师
    clickAddTime_loc=(By.XPATH,"//a[@ng-click='showAddCoursePlanTime()']")#点击添加日期
    selectWeek_loc=(By.XPATH, "//input[@ng-model='selected.dayShowOfWeek1']")#选择星期一
    putStarHour_loc=(By.XPATH, "//input[@id='time1']")#键入上课开始时
    putEndMinute_loc=(By.XPATH, "//input[@id='time2']")#键入上课开始分
    startLen_loc=(By.XPATH, "//select[@name='timeSize']")#选择上课时长
    timeOk_loc=(By.XPATH, "//yanxuebutton[@ng-click='addPlans()']")#点击确定ok
    thisWeek_loc=(By.XPATH, '''//span[@ng-click="show.judgeType('0')"]''')#点击本周
    SubmitButton_loc=(By.XPATH, "//button[@ng-click='show.submitPlan()']")#排课提交
    valiText_loc=(By.XPATH, "//*[@id='body']/div[6]/h2")
    SubmitButton02_loc=(By.XPATH, "//button[@class='confirm']")
    confirmValiText_loc=(By.XPATH, "//*[@id='body']/div[6]/h2")
    continueCancel_loc=(By.XPATH, "//button[@class='cancel']") # 点击"OK,不继续排课"

    def getSelectCourse01Field(self):
        self.findElement(*self.selectCourse01_loc).click()
        self.wait
    def getSelectCourse02Field(self):
        self.findElement(*self.selectCourse02_loc).click()
        self.wait
    def getSelectCourse03Field(self):
        self.findElement(*self.selectCourse03_loc).click()
        self.wait
    def getCourseConfirmField(self):
        self.findElement(*self.courseConfirm_loc).click()
        self.wait
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
    def getValiTextField(self):
        return self.findElement(*self.valiText_loc).text
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
    def multiCourse01(self):
        self.getSelectCourse01Field()
        self.getCourseConfirmField()
        self.getSelectCourse02Field()
        self.getCourseConfirmField()
        self.getSelectCourse03Field()
        self.getCourseConfirmField()
        self.getSelectTeacherField()
        self.getClickAddTimeField()
        self.getSelectWeekField()
        self.getPutStarHourField('8')
        self.getPutEndMinuteField('00')
        self.getStartLenField(2)
        self.getTimeOkField()
        self.getThisWeekField()
        self.getSubmitButtonField()
        # self.getValiTextField()=="即将排课1次(1小时),是否确定?"
        self.getSubmitButton02Field()
        # self.getConfirmValiTextField()=="排课成功!共排课1次(1小时)"
        self.getContinueCancelField()
if __name__=='__main__':
    pass


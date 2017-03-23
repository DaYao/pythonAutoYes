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
from selenium.webdriver.support import expected_conditions as EC
from model.logConsole import  LogConsole
import  logging
from selenium.webdriver.support.wait import WebDriverWait
'''一对一课时排课页面'''
class SingleCoursePlanHourPage(WebUI):
    selectCourse_loc=(By.XPATH, "//button[@ng-click='showOrderCourseList(detail)']")#选择课程
    courseConfirm_loc=(By.XPATH,"//button[@ng-click='selectOrderCourse()']")#点击课程确认
    subjectId_loc=(By.XPATH, "//*[@name='subjectId']")#选择排课科目
    teacherName_loc=(By.XPATH, "//input[@name='teacherName']")#授课教师
    teachingStyle_loc=(By.XPATH,"//input[@ng-model='coursePlanFilter.teachingStyle']")#课程方式
    coefficient_loc=(By.XPATH, "//input[@id='coefficient']")#折算系数
    setingSelectTeacher_loc=(By.XPATH, "//input[@id='timeSearch']")#按时间查询可用老师
    allTeacher_loc=(By.XPATH, "//a[@ng-click='showTeacherList(detail)']")#选择"全部老师"
    # singleTeacher_loc=(By.XPATH, "//a[text()='陈雪薇']")#选择单个老师
    radiomultiPlan_loc=(By.XPATH, '''//div[@ng-click="checkedShowCycle('week')"]/input ''')#选择定制排课时间规则
    radioSinglePlan_loc=(By.XPATH, '''//div[@ng-click="checkedShowCycle('day')"]/input ''')#选择精准日期排课
    starttime2_loc=(By.XPATH,"//input[@ng-model='select.time1']")#精准排课选择上课时间时
    startmini2_loc=(By.XPATH,"//input[@ng-model='select.time2']")#精准排课选择上课时间分
    timeSize2_loc=(By.XPATH,"//select[@id='timeSize']")#精准排课选择上课时长
    # selectTeacher_loc=(By.XPATH, "//div[@ng-if='subjectTeacherGroup.length']/div/div[2]/div[1]/a")#选择教师
    clickAddTime_loc=(By.XPATH,"//a[@ng-click='showAddCoursePlanTime()']")#点击添加日期
    selectWeek_loc=(By.XPATH, "//input[@ng-model='selected.dayShowOfWeek1']")#选择星期一
    putStarHour_loc=(By.XPATH, "//input[@id='time1']")#键入上课开始时
    putEndMinute_loc=(By.XPATH, "//input[@id='time2']")#键入上课开始分
    startLen_loc=(By.XPATH, "//select[@name='timeSize']")#选择上课时长
    timeOk_loc=(By.XPATH, "//button[@ng-click='addPlans()']")#点击确定ok
    weekNumber_loc = (By.XPATH, "//input[@name='weekNumber']")  #最多排课次数
    allTime_loc = (By.XPATH, '''//span[@ng-click="show.judgeType('3')"]''')  #批量排课
    thisWeek_loc=(By.XPATH, '''//span[@ng-click="show.judgeType('0')"]''')#点击只排本周
    nextWeek_loc = (By.XPATH, '''//span[@ng-click="show.judgeType('1')"]''')#点击只排下周
    SubmitButton_loc=(By.XPATH, "//button[@ng-click='show.submitPlan()']")#排课提交
    SubmitButton02_loc=(By.XPATH, "//button[@class='confirm']")
    confirmValiText_loc=(By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']/h2")
    continueCancel_loc=(By.XPATH, "//button[@class='cancel']") # 点击"OK,不继续排课"

    def getSelectCourseField(self):
        self.wait
        buttonSe_Click=self.findElement(*self.selectCourse_loc)
        ActionChains(self.driver).click(buttonSe_Click).perform()
        self.wait
    def getCourseConfirmField(self):
        buttonper_Click=self.findElement(*self.courseConfirm_loc)
        ActionChains(self.driver).click(buttonper_Click).perform()
        self.wait
    def getSubjectIdField(self, startIndex):
        selectLen = Select(self.findElement(*self.subjectId_loc))
        selectLen.select_by_index(startIndex)
        self.wait1
    def getRadiomultiPlanField(self):
        self.findElement(*self.radiomultiPlan_loc).click()
        self.wait
    def getRadioSingleField(self):
        self.findElement(*self.radioSinglePlan_loc).click()
        self.wait
    def getTeacherNameField(self):
        self.findElement(*self.teacherName_loc).text
    def getTeachingStyleField(self):
        self.findElement(*self.teachingStyle_loc).text
    def getCoefficientField(self, coefficient):
        self.findElement(*self.coefficient_loc).send_keys(coefficient)
    def getSetingSelectTeacherField(self):
        self.findElement(*self.setingSelectTeacher_loc).click()
        self.wait
    def getSingleTeacherField(self,teacherName):
        # loc=r"//a[text()='"+teacherName+r"']"
        loc="//a[text()='自动化教']"
        singleTeacher_loc=(By.XPATH, loc)#选择单个老师
        click=self.findElement(*singleTeacher_loc)
        ActionChains(self.driver).click(click).perform()
        self.wait
    def getAllTeacherField(self):
        self.findElement(*self.allTeacher_loc).click()
        self.wait
    '''精准排课 上课日期'''
    def getStartDate2Field(self,startValue):
        startTime = "$(\"input[ng-model='select.startDate']\").removeAttr('readonly');$(\"input[ng-model='select.startDate']\").attr('value', \"" + startValue + "\" ).trigger('change')"
        return startTime
    '''批量排课 开始日期'''
    def getPTimeStartField(self,startValue):
        startTime = "$(\"input[ng-model='select.pTimeStart']\").removeAttr('readonly');$(\"input[ng-model='select.pTimeStart']\").attr('value', \"" + startValue + "\" ).trigger('change')"
        return startTime
    '''批量排课 结束日期'''
    def getPTimeEndField(self,endValue):
        stopTime = "$(\"input[ng-model='select.pTimeStart']\").removeAttr('readonly');$(\"input[ng-model='select.pTimeEnd']\").attr('value', \"" + endValue + "\" ).trigger('change')"
        return stopTime
    def getStarttime2Field(self, starttime):
        self.findElement(*self.starttime2_loc).send_keys(starttime)
    def getStartmini2Field(self, startmini):
        self.findElement(*self.startmini2_loc).send_keys(startmini)
    def getTimeSize2Field(self, startIndex):
        selectLen = Select(self.findElement(*self.timeSize2_loc))
        selectLen.select_by_index(startIndex)
    def getAllTimeField(self):
        self.findElement(*self.allTime_loc).click()
        self.wait
    def getThisWeekField(self):
        self.findElement(*self.thisWeek_loc).click()
        self.wait
    def geNextWeekField(self):
        self.findElement(*self.nextWeek_loc).click()
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
    def getWeekNumberField(self, num):
        self.findElement(*self.weekNumber_loc).send_keys(num)
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
    #批量排课
    def hourCours01(self,teacherName):
        self.getSelectCourseField()
        self.getCourseConfirmField()
        self.getSubjectIdField(2)
        self.getSingleTeacherField(teacherName)
        self.getRadiomultiPlanField()
        self.getClickAddTimeField()
        self.getSelectWeekField()
        self.getPutStarHourField('8')
        self.getPutEndMinuteField('00')
        self.getStartLenField(2)
        self.getTimeOkField()
        startValue = '2014-06-21'
        endValue = '2016-06-21'
        startTime=self.getPTimeStartField(startValue)
        endTime=self.getPTimeEndField(endValue)
        self.driver.execute_script(startTime)
        self.driver.execute_script(endTime)
        self.getWeekNumberField(1)
        self.getSubmitButtonField()
        self.getSubmitButton02Field()
        valiText=self.getConfirmValiTextField()
        self.getContinueCancelField()
        return valiText
    #本周排课
    def hourCours02(self,teacherName):
        self.getSelectCourseField()
        self.getCourseConfirmField()
        self.getSubjectIdField(2)
        self.getSingleTeacherField(teacherName)
        self.getRadiomultiPlanField()
        self.getClickAddTimeField()
        self.getSelectWeekField()
        self.getPutStarHourField('8')
        self.getPutEndMinuteField('00')
        self.getStartLenField(2)
        self.getTimeOkField()
        self.getThisWeekField()
        self.getSubmitButtonField()
        self.getSubmitButton02Field()
        valiText=self.getConfirmValiTextField()
        self.getContinueCancelField()
        return valiText
    #下周排课
    def hourCours03(self):
        self.getSelectCourseField()
        self.getCourseConfirmField()
        self.getSubjectIdField(2)
        self.getSingleTeacherField()
        self.getClickAddTimeField()
        self.getSelectWeekField()
        self.getPutStarHourField('8')
        self.getPutEndMinuteField('00')
        self.getStartLenField(2)
        self.getTimeOkField()
        self.geNextWeekField()
        self.getSubmitButtonField()
        self.getSubmitButton02Field()
        valiText=self.getConfirmValiTextField()
        self.getContinueCancelField()
        return valiText
    #精准排课
    def hourCours04(self,teacherName):
        self.getSelectCourseField()
        self.getCourseConfirmField()
        self.getSubjectIdField(2)
        self.getSingleTeacherField(teacherName)
        self.getRadioSingleField()
        startTime =self.getStartDate2Field("2017-11-11")
        self.driver.execute_script(startTime)
        self.getStarttime2Field('12')
        self.getStartmini2Field('12')
        self.getTimeSize2Field(1)
        self.getSubmitButtonField()
        self.getSubmitButton02Field()
        valiText=self.getConfirmValiTextField()
        self.getContinueCancelField()
        return valiText
    #跨校区排课
    def hourCours05(self):
        pass
    #按时间段查询可用教师排课
    def hourCours06(self):
        pass
    #排课时间冲突测试
    def hourCours07(self):
        pass
    #教师不可排课时间冲突测试
    def hourCours08(self):
        pass



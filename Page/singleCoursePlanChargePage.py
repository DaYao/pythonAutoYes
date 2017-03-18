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
'''一对一储值排课页面'''
class SingleCoursePlanChargePage(WebUI):
    changeTab_loc = (By.XPATH, "//span[@ng-click='showPaikeView(1)']")#切换储值tab
    orderNo_loc = (By.XPATH, "//input[@id='storedOrderId']")#订单编号
    selectCourse_loc = (By.XPATH, "//button[@ng-click='showStoredOrderList(detail)']")#查看订单
    studentGrade_loc=(By.XPATH, "//input[@id='grade_id']")#学员年级
    teacherLevel_loc=(By.XPATH, "//input[@id='teacherLevel']")#排课师资
    orderCharge_loc=(By.XPATH, "//input[@id='orderCharge']")#课时单价
    subjectId_loc=(By.XPATH, "//select[@id='subjectId']")#选择科目
    teacherName_loc=(By.XPATH, "//input[@name='teacherName']")#授课教师
    teachingStyle_loc=(By.XPATH,"//input[@ng-model='coursePlanFilter.teachingStyle']")#课程方式
    coefficient_loc=(By.XPATH, "//input[@id='coefficient']")#折算系数
    setingSelectTeacher_loc=(By.XPATH, "//input[@id='timeSearch']")#按时间查询可用老师
    allTeacher_loc=(By.XPATH, "//a[@ng-click='showTeacherList(detail)']")#选择"全部老师"
    singleTeacher_loc=(By.XPATH, "//a[text()='陈雪薇']")#选择单个老师
    radiomultiPlan_loc=(By.XPATH, "//div[@ng-click='checkedShowCycle('week')'/input']")#选择定制排课时间规则
    radioSinglePlan_loc=(By.XPATH, "//div[@ng-click='checkedShowCycle('day')'/input']")#选择精准日期排课
    clickAddTime_loc = (By.XPATH, "//a[@ng-click='showAddCoursePlanTime()']")  # 点击添加日期
    selectWeek_loc = (By.XPATH, "//input[@ng-model='selected.dayShowOfWeek1']")  # 选择星期一
    putStarHour_loc = (By.XPATH, "//input[@id='time1']")  # 键入上课开始时
    putEndMinute_loc = (By.XPATH, "//input[@id='time2']")  # 键入上课开始分
    startLen_loc = (By.XPATH, "//select[@name='timeSize']")  # 选择上课时长
    timeOk_loc = (By.XPATH, "//button[@ng-click='addPlans()']")  # 点击确定ok
    allTime_loc = (By.XPATH, '''//span[@ng-click="show.judgeType('3')"]''')  #批量排课
    thisWeek_loc = (By.XPATH, '''//span[@ng-click="show.judgeType('0')"]''')  # 点击本周
    nextWeek_loc = (By.XPATH, '''//span[@ng-click="show.judgeType('1')"]''')  # 点击下周
    pTimeStart_loc = (By.XPATH, "//input[@ng-model='select.pTimeStart']")  #批量开始时间
    pTimeEnd_loc = (By.XPATH, "//input[@ng-model='select.pTimeEnd']")  #批量开始时间
    weekNumber_loc = (By.XPATH, "//input[@name='weekNumber']")  #批量开始时间
    SubmitButton_loc = (By.XPATH, "//button[@ng-click='show.submitPlan()']")#排课提交
    valiText_loc = (By.XPATH, "//*[@id='body']/div[6]/h2")
    SubmitButton02_loc = (By.XPATH, "//button[@class='confirm']")
    confirmValiText_loc=(By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']/h2")
    continueCancel_loc = (By.XPATH, "//button[@class='cancel']")  #"OK,不继续排课"
    timeToday_loc=(By.XPATH, "//input[@id='dpTodayInput']")

    def getTimeTodayField(self):
        self.findElement(*self.timeToday_loc).click()
        self.wait
    def getChangeTabField(self):
        self.findElement(*self.changeTab_loc).click()
        self.wait
    def getOrderNoField(self):
        self.findElement(*self.orderNo).text
    def getSelectCourseField(self):
        self.findElement(*self.selectCourse_loc).click()
        self.wait
    def getStudentGradeField(self,startIndex):
        selectLen = Select(self.findElement(*self.studentGrade_loc))
        selectLen.select_by_index(startIndex)
        self.wait
    def getTeacherLevelField(self):
        self.findElement(*self.teacherLevel_loc).text
    def getOrderChargeField(self):
        self.findElement(*self.orderCharge_loc).text
    def getTeacherNameField(self):
        self.findElement(*self.teacherName_loc).text
    def getSubjectIdField(self,startIndex):
        selectLen = Select(self.findElement(*self.subjectId_loc))
        selectLen.select_by_index(startIndex)
        self.wait
    def getTeachingStyleField(self):
        self.findElement(*self.teachingStyle_loc).text
    def getCoefficientField(self, coefficient):
        self.findElement(*self.coefficient_loc).send_keys(coefficient)
    def getSetingSelectTeacherField(self):
        self.findElement(*self.setingSelectTeacher_loc).click()
        self.wait
    def getSingleTeacherField(self):
        self.findElement(*self.singleTeacher_loc).click()
        self.wait
    def getAllTeacherField(self):
        self.findElement(*self.allTeacher_loc).click()
        self.wait
    def getRadiomultiPlanField(self):
        self.findElement(*self.radiomultiPlan_loc).click()
        self.wait
    def getRadioSingleField(self):
        self.findElement(*self.radioSinglePlan_loc).click()
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
    def getWeekNumberField(self, num):
        self.findElement(*self.weekNumber_loc).send_keys(num)
    def getTimeOkField(self):
        self.findElement(*self.timeOk_loc).click()
        self.wait
    def getAllTimeField(self):
        self.findElement(*self.allTime_loc).click()
        self.wait
    def getThisWeekField(self):
        self.findElement(*self.thisWeek_loc).click()
        self.wait
    def geNtextWeekField(self):
        self.findElement(*self.nextWeek_loc).click()
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
    def docoursePlan01(self):
        self.getChangeTabField()
        self.getSubjectIdField(2)
        self.getSingleTeacherField()
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
    def docoursePlan02(self):
        self.getChangeTabField()
        self.getSubjectIdField(2)
        self.getSingleTeacherField()
        self.getClickAddTimeField()
        self.getSelectWeekField()
        self.getPutStarHourField('8')
        self.getPutEndMinuteField('00')
        self.getStartLenField(2)
        self.getTimeOkField()
        startValue = '2012-06-21'
        endValue = '2012-06-21'
        startTime=self.getPTimeStartField(startValue)
        endTime=self.getPTimeEndField(endValue)
        self.driver.execute_script(startTime)
        self.driver.execute_script(endTime)
        self.getWeekNumberField(3)
        self.getSubmitButtonField()
        # self.getValiTextField()=="即将排课1次(1小时),是否确定?"
        self.getSubmitButton02Field()
        # self.getConfirmValiTextField()=="排课成功!共排课1次(1小时)"
        self.getContinueCancelField()


if __name__=='__main__':
    pass


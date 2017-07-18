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
'''创建班组页面'''
class CreateGroupPage(WebUI):
    groupName_loc=(By.XPATH, "//input[@placeholder='班组名称']")#班组名称
    orderRule_loc=(By.XPATH,"//*[@id='orderRule']")#课程规则
    groupType_loc=(By.XPATH,"//*[@id='groupType']")#类型
    studentCount_loc=(By.XPATH,"//input[@ng-model='myCrmCustomerStudentListForAddGroupFilter.student_count']")#人数
    studentName_loc=(By.XPATH, "//input[@placeholder='学生姓名']")#学生姓名
    studentPhone_loc=(By.XPATH, "//input[@placeholder='电话']")#学生电话
    gradeId_loc=(By.XPATH, "//select[@name='myCrmCustomerStudentListForAddGroupFilter.grade_id']")#年级
    selectButton_loc=(By.XPATH, "//a[@ng-click='getMyCrmCustomerStudentListForAddGroup(studentListForAddGroupTableState)']")#查询
    resetParam_loc=(By.XPATH, "//a[@ng-click='resetParam()']")#重置
    selectStudent01_loc=(By.XPATH, "//*[@id='getHeight']/div[2]/table/tbody[1]/tr[1]/td[1]/label")#选择教师
    selectStudent02_loc=(By.XPATH, "//*[@id='getHeight']/div[2]/table/tbody[1]/tr[4]/td[1]/label")#选择教师
    selectStudent03_loc=(By.XPATH, "//*[@id='getHeight']/div[2]/table/tbody[1]/tr[7]/td[1]/label")#选择教师
    submitButton_loc=(By.XPATH, "//button[@ng-click='btnTrue()']")
    confirmValiText_loc=(By.XPATH, "//h1[@class='f24 ng-binding']")
    ok_loc=(By.XPATH,"//button[@class='btn btn-success c5-lable ng-scope']")

    def getGroupNameField(self, groupName):
        self.findElement(*self.groupName_loc).send_keys(groupName)
    def getOrderRuleField(self, orderRule):
        selectLen = Select(self.findElement(*self.orderRule_loc))
        selectLen.select_by_index(orderRule)
    def getGroupTypField(self, groupTyp):
        selectLen = Select(self.findElement(*self.groupType_loc))
        selectLen.select_by_index(groupTyp)
    def getStudentCountField(self, studentCount):
        self.findElement(*self.studentCount_loc).send_keys(studentCount)
    def getStudentNameField(self, studentName):
        self.findElement(*self.studentName_loc).clear()
        self.findElement(*self.studentName_loc).send_keys(studentName)
    def getStudentPhoneField(self, studentPhone):
        self.findElement(*self.studentPhone_loc).clear()
        self.findElement(*self.studentPhone_loc).send_keys(studentPhone)
    def getGradeId_locField(self, gradeId):
        selectLen = Select(self.findElement(*self.gradeId_loc))
        selectLen.select_by_index(gradeId)
    def getSelectButtonField(self):
        self.findElement(*self.selectButton_loc).click()
        self.wait
    def getresetParamField(self):
        self.findElement(*self.resetParam_loc).click()
        self.wait
    def getSelectStudent01Field(self):
        self.findElement(*self.selectStudent01_loc).click()
        self.wait
    def getSelectStudent02Field(self):
        self.findElement(*self.selectStudent02_loc).click()
    def getSelectStudent03Field(self):
        self.findElement(*self.selectStudent03_loc).click()
        self.wait
    def getSubmitButtonField(self):
        self.findElement(*self.submitButton_loc).click()
        self.wait
    def getOkField(self):
        self.findElement(*self.ok_loc).click()
        self.wait
    def getonfirmValiText_locField(self):
        return self.findElement(*self.confirmValiText_loc).text
    def createGroup(self,groupName,orderRule,groupType):
        self.createGroup01(groupName,orderRule,groupType)
        return HomePage(self.driver)
    def createGroup01(self,groupName,orderRule,groupType):
        self.getGroupNameField(groupName)
        self.getOrderRuleField(orderRule)
        self.getGroupTypField(groupType)
        self.getSelectStudent01Field()
        self.getSelectStudent02Field()
        self.getSelectStudent03Field()
        self.getSubmitButtonField()
        self.getOkField()
    def createSelectGroup(self,groupName,orderRule,groupType,studentName,studentPhone,grade):
        self.getGroupNameField(groupName)
        self.getOrderRuleField(orderRule)
        self.getGroupTypField(groupType)
        self.getStudentNameField(studentName)
        self.getStudentPhoneField(studentPhone)
        self.getGradeId_locField(grade)
        self.getSelectStudent01Field()
        self.getSubmitButtonField()
        self.getOkField()
        return HomePage(self.driver)

    def createSelectGroup1(self, groupName, orderRule, groupType, studentName, studentPhone, grade):
        self.getGroupNameField(groupName)
        self.getOrderRuleField(orderRule)
        self.getGroupTypField(groupType)
        self.getStudentNameField(studentName)
        self.getStudentPhoneField(studentPhone)
        self.getGradeId_locField(grade)
        self.getSelectStudent01Field()
        self.getSubmitButtonField()
        self.getOkField()
        return HomePage(self.driver)

if __name__=='__main__':
    pass
   # createGroupPage.createGroup("班组新增",1,2)


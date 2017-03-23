__author__ = 'xueyan'
# coding:utf-8
import  unittest
import sys,os,logging
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import  HomePage
from Page.BasePage import WebUI
from model import Model
from model.pyMysqlDB import myDB

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.logConsole import  LogConsole
# import  logging
from Page.editlPlanCoursePage import EditPlanChargePage
# from model.Model import  DataHelper
from ddt import  ddt,data,unpack
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import  NoSuchElementException
from  selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions

class editHourCoursePlan60(BaseLogin,EditPlanChargePage):

    #通过一对一排课管理进入排课编辑
    def testEditCoursePlan60_001(self):
        logging.info("-------通过对一排课管理入口进入排课编辑------")
        #数据初始化,新增学员教师
        returnNum=myDB.connect_function(myDB,'func_autoInsertCoursePlan(1006)')
        studentName='自动化学员'+returnNum
        teacherName='自动化教师'+returnNum
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        #一对一管理列表
        self.wait1
        studentList_loc=(By.XPATH,"//*[@id='CoursePlanManagement']/li[1]/a")
        click =self.findElement(*studentList_loc)
        ActionChains(driver).click(click).perform()
        #学生姓名查询
        self.wait1
        studenNameSe_loc=(By.XPATH,"//input[@ng-model='mtSeach.student_name']")
        try:
            WebDriverWait(driver, 10, 0.2).until(EC.presence_of_element_located(studenNameSe_loc))
        except Exception as e:
            driver.get_screenshot_as_file('../Report/image/testEditCoursePlan60_001.png')
            logging.error("找不到【学员姓名】元素")
        self.findElement(*studenNameSe_loc).send_keys(studentName)
        ##查询按钮
        self.wait1
        startValue='2017-03-01'
        endValue='2017-03-01'
        startTime = "$(\"input[ng-model='mtSeach.start_time']\").removeAttr('readonly');$(\"input[ng-model='mtSeach.start_time']\").attr('value', \"" + startValue + "\" ).trigger('change')"
        endTime = "$(\"input[ng-model='mtSeach.end_time']\").removeAttr('readonly');$(\"input[ng-model='mtSeach.end_time']\").attr('value', \"" + startValue + "\" ).trigger('change')"
        self.driver.execute_script(startTime)
        self.driver.execute_script(endTime)
        self.wait1
        ##查询
        driver.find_element_by_xpath("//a[@id='keydown-query']").click()
        self.wait
        ##操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        driver.find_element_by_xpath("//a[contains(text(),'编辑')]").click()
        self.wait
        self.EditPlan01()
        #删除测试数据
        myDB.connect_function(myDB,'func_del_autoInsertStudent('+returnNum+')')

if __name__ == '__main__':
    unittest.main(verbosity=2)

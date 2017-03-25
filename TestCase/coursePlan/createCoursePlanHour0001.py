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
from Page.singleCoursePlanHourPage import SingleCoursePlanHourPage
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

class StudentHourCoursePlan60(BaseLogin,SingleCoursePlanHourPage):

    #通过学员管理入口进入排课
    @unittest.skip('test')
    def testHourCoursePlan60_001(self):
        logging.info("-------通过学员管理入口进入排课------")
        #数据初始化,新增学员教师
        returnNum=myDB.connect_function(myDB,'func_autoInsertStudent(1006)')
        studentName='自动化学员'+returnNum
        teacherName='自动化教师'+returnNum
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        #学员管理列表
        self.wait1
        studentList_loc=(By.XPATH,"//*[@id='CustomerStudentManagement']/li[1]/a")
        click =self.findElement(*studentList_loc)
        ActionChains(driver).click(click).perform()
        #学生姓名查询
        self.wait1
        studenNameSe_loc=(By.XPATH,"//*[@id='noMar']")
        try:
            WebDriverWait(driver, 10, 0.2).until(EC.presence_of_element_located(studenNameSe_loc))
        except Exception as e:
            driver.get_screenshot_as_file('../Report/image/testHourCoursePlan60_001_02.png')
            logging.error("找不到【学员姓名】元素")
        self.findElement(*studenNameSe_loc).send_keys(studentName)
        ##查询按钮
        self.wait1
        buttonSe_Click =driver.find_element_by_xpath("//*[@id='keydown-query']")
        ActionChains(driver).click(buttonSe_Click).perform()
        #学员列表操作
        self.wait1
        oper_loc=(By.XPATH,"//a[@id='nw+0']/span")
        self.findElement(*oper_loc).click()
        #点击排课操作
        self.wait1
        coursePlan_loc=(By.XPATH,"//*[@id='body']/popup/div/div/div/ul/li[6]/a")
        self.findElement(*coursePlan_loc).click()
        #调用公共一对一排课界面
        valitext=self.hourCours01(teacherName)
        context_expxcted="排课成功!共排课1次(1小时)"
        self.assertEqual(context_expxcted, valitext)
        #删除测试数据
        myDB.connect_function(myDB,'func_del_autoInsertStudent('+returnNum+')')

    @unittest.skip('test')
    def testHourCoursePlan60_002(self):
        returnNum=myDB.connect_function(myDB,'func_autoInsertStudent(1006)')
        studentName='自动化学员'+returnNum
        teacherName='自动化教师'+returnNum
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        self.wait
        # 点击学员列表操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        # 点击排课操作
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[6]/a").click()
        # driver.find_element_by_xpath("//a[contains(text(),'排课')]").click()
        self.wait
        #调用公共一对一排课界面
        valitext=self.hourCours02(teacherName)
        context_expxcted="排课成功!共排课1次(1小时)"
        self.assertEqual(context_expxcted, valitext)
        #删除测试数据
        myDB.connect_function(myDB,'func_del_autoInsertStudent('+returnNum+')')
    #@unittest.skip('test')
    def testHourCoursePlan60_003(self):
        returnNum=myDB.connect_function(myDB,'func_autoInsertStudent(1006)')
        studentName='自动化学员'+returnNum
        teacherName='自动化教师'+returnNum
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        self.wait
        # 点击学员列表操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        # 点击排课操作
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[6]/a").click()
        # driver.find_element_by_xpath("//a[contains(text(),'排课')]").click()
        self.wait
        #调用公共一对一排课界面
        valitext=self.hourCours04(teacherName)
        context_expxcted="排课成功!共排课1次(0.5小时)"
        self.assertEqual(context_expxcted, valitext)
        myDB.connect_function(myDB,'func_del_autoInsertStudent('+returnNum+')')
if __name__=='__main__':
	unittest.main(verbosity=2)

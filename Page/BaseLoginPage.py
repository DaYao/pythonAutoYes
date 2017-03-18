__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
import unittest,time
from appium import  webdriver as appwebdriver
from selenium import webdriver as webdriver
from .BasePage import  WebUI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
# from model.logConsole import  LogConsole
# import  logging


'''后台公共登录页面'''
class BaseLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(30)
        self.driver.get('http://172.168.101.83/')
        try:
            WebDriverWait(self.driver, 10, 0.2).until(EC.presence_of_element_located((By.ID,"login-name")))
        except Exception as e:
            self.driver.get_screenshot_as_file('../Report/image/loginErro.png')
            # logging.error("找不到【登录用户名】元素")
        self.driver.find_element_by_id('login-name').send_keys('qiqi1')
        self.driver.find_element_by_id('login-pass').send_keys('password')
        self.driver.find_element_by_name('user.verifyCode').send_keys('1234')
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

class AppBaseLogin(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'Google Nexus 4-4.4.4'
        desired_caps['appPackage'] = 'com.youwinedu.student'
        desired_caps['appActivity'] = '.ui.activity.LauncherActivity'
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True
        self.driver = appwebdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(1)
        button01 = self.driver.find_element_by_id("com.youwinedu.student:id/r_three")
        button01.click()
        time.sleep(1)
        # WebDriverWait(self.driver,10000).until(EC.invisibility_of_element_located((By.ID,"com.youwinedu.student:id/rl_login_model")))
        button02 = self.driver.find_element_by_id("com.youwinedu.student:id/rl_login_model")
        button02.click()
        time.sleep(1)
        # 登录
        name = self.driver.find_element_by_id('com.youwinedu.student:id/et_name')
        name.send_keys('18699123456')  # 输入用户名
        psd = self.driver.find_element_by_id('com.youwinedu.student:id/et_password')
        psd.send_keys('123456')  # 输入密码
        buton03 = self.driver.find_element_by_id('com.youwinedu.student:id/bt_login')
        # 单击登录按钮
        # self.driver.save_screenshot("lognApp.png")
        buton03.click()
        time.sleep(2)
    def tearDown(self):
        time.sleep(2)
        my_loc = self.driver.find_element_by_id("com.youwinedu.student:id/r_three")
        my_loc.click()
        time.sleep(2)
        valit_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_use_name").text
        time.sleep(2)
        sysSet_loc=self.driver.find_element_by_id('com.youwinedu.student:id/ll_sysset')
        sysSet_loc.click()
        time.sleep(2)
        logout_loc=self.driver.find_element_by_id('com.youwinedu.student:id/logon')
        logout_loc.click()
        time.sleep(2)
        self.driver.quit()
__author__ = 'xueyan'
#coding:utf-8
import unittest
from selenium import webdriver
import  time,os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
'''浏览器和app启动页'''
class BaseTestCase(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://172.168.101.83/')
		time.sleep(2)
	def tearDown(self):
		self.driver.quit()
class AppTestCase(unittest.TestCase):
	def setUp(self):
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']='4.4.4'
		desired_caps['deviceName']='Google Nexus 4-4.4.4'
		desired_caps['appPackage']='com.youwinedu.student'
		desired_caps['appActivity']='.ui.activity.LauncherActivity'
		# desired_caps['app'] = PATH(
		#     'F:/web/appiumn_auto/res/student_v1.8.4_2017-03-10_youwinedu.apk'
		# )
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

	def tearDown(self):
		self.driver.quit()
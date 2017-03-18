__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from selenium.webdriver.common.by import By
from .homePage import HomePage
from Page.BasePage import AppUI
import  time as t

'''学生端登录页面'''
class AppStudentLoginPage(AppUI):

	username_loc=(By.ID,'com.youwinedu.student:id/et_name')
	password_loc=(By.ID,'com.youwinedu.student:id/et_password')
	loginButton_loc=(By.ID,'com.youwinedu.student:id/bt_login')
	loginDiv_loc=(By.ID,'com.youwinedu.student:id/title_bar_back_button')

	def getUsername(self,username):
		self.wait
		self.findElement(*self.username_loc).send_keys(username)
	def getPassword(self,password):
		self.findElement(*self.password_loc).send_keys(password)
	def clickLoginButton(self):
		self.findElement(*self.loginButton_loc).click()
	def getLoginDiv(self):
		self.wait
		return self.findElement(*self.loginDiv_loc).text
	def login(self,username,password):
		self.getUsername(username)
		self.getPassword(password)
		self.clickLoginButton()
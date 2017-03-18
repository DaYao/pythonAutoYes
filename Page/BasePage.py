__author__ = 'xueyan'
#coding:utf-8
from selenium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import  By
# from model.logConsole import  LogConsole
# import  logging
import  time as t

'''工厂方法'''
class Factory(object):
	def __init__(self,driver):
		self.driver=driver

	#工厂方法
	def createWebDdriver(self,webDdriver):
		if webDdriver=='web':
			return WebUI(self.driver)
		elif webDdriver=='app':
			return AppUI(self.driver)

class WebDdriver(object):
	def __init__(self,driver):
		self.driver=driver

	def __str__(self):
		return 'webDdriver'

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			pass
			# logging.error('Error details :%s'%(e.args[0]))
	@property
	def wait(self):
		t.sleep(3)
	@property
	def wait1(self):
		t.sleep(1)
	@property
	def wait5(self):
		t.sleep(5)
	@property
	def wait10(self):
		t.sleep(10)
class WebUI(WebDdriver):
	def __str__(self):
		return 'WEB UI'
class AppUI(WebDdriver):
	def __str__(self):
		return 'App UI'





















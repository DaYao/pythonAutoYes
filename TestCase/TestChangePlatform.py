__author__ = 'lhf'
# coding:utf-8
import unittest
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import HomePage
from Page.changePlatformPage import ChangePlatformPage
from model.pyMysqlDB import myDB
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ChangePlatformTest(BaseLogin,ChangePlatformPage,HomePage):
    def testChangePlatform(self):#添加转平台
        returnNum = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        studentChangeName = '自动化学员' + returnNum

        self.ChangePlatform(studentChangeName)
        self.ChangePlatformVerify(studentChangeName)

        myDB.connect_function(myDB, 'func_del_autoInsertStudent(' + returnNum + ')')
        '''self.driver.refresh()
        self.wait10
        self.driver.find_element_by_xpath("//*[@id='body']/div[2]/div[1]/div[1]").click()
        #ActionChains(self.driver).click(click).perform()
        self.wait
        click = self.driver.find_element_by_xpath("//a[@ng-click='logout()']")
        ActionChains(self.driver).click(click).perform()
        self.wait'''
if __name__ == '__main__':
    unittest.main(verbosity=2)

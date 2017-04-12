__author__ = 'lhf'
# coding:utf-8
import unittest
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import HomePage
from Page.activityChargePage import ActivityChargePage
from model.pyMysqlDB import myDB


class ActivityChargeTest(BaseLogin,ActivityChargePage,HomePage):

    def testActivityCharge(self):#添加活动消课
        returnNum = myDB.connect_function(myDB, 'func_autoInsertStudent(1)')
        studentChargeName = '自动化学员' + returnNum

        self.ActivityCharge(studentChargeName)
        self.ActivityChargeVerify(studentChargeName)
        self.ActivitySumCharge(studentChargeName)
        self.ActivityChargeReverse(studentChargeName)

        myDB.connect_function(myDB, 'func_del_autoInsertStudent(' + returnNum + ')')
if __name__ == '__main__':
    unittest.main(verbosity=2)

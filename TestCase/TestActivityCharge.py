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

    studentChargeName = '自动化学员1490258994'

    def testActivityCharge(self):#添加活动消课
        self.ActivityCharge(self.studentChargeName)
        self.ActivityChargeVerify(self.studentChargeName)
if __name__ == '__main__':
    unittest.main(verbosity=2)

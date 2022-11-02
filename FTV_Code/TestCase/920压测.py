#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 16:19
# @Author  : wudong7182
# @Site    : 
# @File    : 920压测.py
# @Software: PyCharm


import re
import TestCase
import unittest
from TV import 按键相关
from Android.xbug import *
from airtest.core.api import *
from notify.通知到企业邮箱 import mail
T1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


class TestDemo(unittest.TestCase):
    def setUp(self) -> None:  # 方法预期的返回值为None 非强制
        print("测试准备...")
        TestCase.DEVICES()
        self.ser = TestCase.Ser()
        self.TV = 按键相关.操作TV(serialno=self.ser)
        self.file = os.path.basename(__file__)
        self.filename = self.file.split('.')

    def tearDown(self) -> None:
        # self.ser
        self.task_name = self.filename[0] + "_" + self.Launcher和各种APP互相切换压测.__name__
        mail(self.task_name)
        print("完成测试： ", self.ser)



    def test_01(self):
        print("测试开始时间：" + T1)
        for i in range(1, 9999):
            print("================执行第%d次压测================" % i)
            print("测试时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            self.Launcher和各种APP互相切换压测()
            print("恭喜！！！第 " + str(i) + " 次压测没有检测到黑屏")
        # t2.start()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemo("test_01"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    T2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print("测试结束时间：" + T2)

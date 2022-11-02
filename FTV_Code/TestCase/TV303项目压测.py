#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/12 17:56
# @Author  : wudong7182
# @Site    : 
# @File    : TV303项目压测.py
# @Software: PyCharm

import TestCase
import time

import unittest
from airtest.core.api import *
from TV import 按键相关
# from Android.监测指定进程是否会挂掉 import *
T1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


class TestDemo(unittest.TestCase):
    def setUp(self) -> None:  # 方法预期的返回值为None 非强制
        print("测试准备...")
        TestCase.DEVICES()
        self.ser = TestCase.Ser()
        self.TV = 按键相关.操作TV(serialno=self.ser)

    def tearDown(self) -> None:
        # self.ser
        print("断开adb设备 ", self.ser)

    def 切换通道压测(self, direction):  # direction  选择通道切换时的方向
        if int(direction % 2 == 0):
            for i in range(4):
                self.TV.按下通道按键()
                self.TV.按下向下按键()
                self.TV.按下向左按键()
                self.TV.按下enter按键()
                sleep(3)
        else:
            for i in range(4):
                self.TV.按下通道按键()
                self.TV.按下向下按键()
                self.TV.按下向右按键()
                self.TV.按下enter按键()
                sleep(3)

    def Launcher和ATV通道互相切换压测(self):
        shell("am start com.cvte.tv.launcher.saturn/com.cvte.tv.launcher.saturn.MainActivity")
        self.TV.按下HOME键()
        self.TV.按下向左按键()
        self.TV.按下enter按键()
        sleep(10)

    def Launcher和Browser互相切换压测(self):
        self.TV.按下HOME键()
        sleep(7)
        snapshot()
        self.TV.按下向右按键()
        self.TV.按下向右按键()
        self.TV.按下向右按键()
        self.TV.按下向右按键()
        self.TV.按下enter按键()
        sleep(5)
        snapshot()

    def test_01(self):
        print("测试开始时间：" + T1)
        for i in range(1, 9999):
            print("================执行第%d次压测================" % i)
            print("测试时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            self.Launcher和ATV通道互相切换压测()
        # t2.start()

    def test_02(self):
        snapshot()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemo("test_01"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    T2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print("测试结束时间：" + T2)

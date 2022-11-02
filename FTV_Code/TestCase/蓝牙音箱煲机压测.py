#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 20:24
# @Author  : wudong7182
# @Site    : 
# @File    : 蓝牙音箱煲机压测.py
# @Software: PyCharm
import TestCase
import unittest
import threading
from Android.监测指定进程是否会挂掉 import *
from audio.player import Player
class TestDemo(unittest.TestCase):
    def setUp(self) -> None:  # 方法预期的返回值为None 非强制
        print("setUp")
        ser = TestCase.DEVICES()

    def tearDown(self) -> None:
            print("断开db设备")


    def Wd_02(self):
            bluetooth = 监测指定进程是否会挂掉(psname="com.android.bluetooth")
            bluetooth.检测进程()

    def test_01(self):
            t1 = threading.Thread(target=self.Wd_02)
            t1.start()

if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(TestDemo("test_01"))
        # 执行测试
        runner = unittest.TextTestRunner()
        runner.run(suite)
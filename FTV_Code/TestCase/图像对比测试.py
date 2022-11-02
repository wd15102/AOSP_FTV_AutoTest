#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 20:24
# @Author  : wudong7182
# @Site    :
# @File    : 蓝牙音箱煲机压测.py
# @Software: PyCharm
import TestCase
from airtest.core.api import *
import unittest
import threading
class TestDemo(unittest.TestCase):
    def setUp(self) -> None:  # 方法预期的返回值为None 非强制
        print("开始测试，执行前置操作")
        self.ser = TestCase.DEVICES()

    def tearDown(self) -> None:
        Dev = self.ser.serialno
        print("结束测试，断开adb设备：", Dev)

    def test_02(self):
        # exists(Template(r"tpl1661409777024.png", record_pos=(-0.168, -0.163), resolution=(1920, 1080)))
        exists(Template(r"tpl1661409789982.png", record_pos=(-0.155, -0.128), resolution=(1920, 1080)))
        # exists(Template(r"tpl1661409806097.png", record_pos=(-0.028, -0.018), resolution=(1920, 1080)))


    def test_01(self):
            t1 = threading.Thread(target=self.Wd_02)
            t1.start()

if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(TestDemo("test_02"))
        # 执行测试
        runner = unittest.TextTestRunner()
        runner.run(suite)
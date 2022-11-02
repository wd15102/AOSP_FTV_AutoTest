#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 11:22
# @Author  : wudong7182
# @Site    : 
# @File    : 语音压测.py
# @Software: PyCharm
import TestCase
from Android.Logcat import Speech_Log
import unittest
import threading
from Android.监测指定进程是否会挂掉 import *
from audio.player import Player
class TestDemo(unittest.TestCase):
    def setUp(self) -> None:  # 方法预期的返回值为None 非强制
        print("测试准备...")
        TestCase.DEVICES()
        self.ser = TestCase.Ser()

    def tearDown(self) -> None:
        # self.ser
        print("断开adb设备 ", self.ser)

    def Wd_01(self):
        Path = "E:\\FTV_Code\\audio\\wakeTest\\"
        mp = Player()
        mp.player(Path, delay=5, timeout=9999)

    def 监测进程(self):
        Process = 监测指定进程是否会挂掉(psname="com.cvte.tv.ftvspeech")
        Process.检测进程()

    def 唤醒次数(self):
        Speech_Log(tagFilter="ResearchReceiver ", keywordFilter="wakeupWordIndex").WakeupLog()

    def test_01(self):
        t1 = threading.Thread(target=self.Wd_01)
        t2 = threading.Thread(target=self.监测进程)
        t1.start()
        # self.唤醒次数()
        t2.start()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemo("test_01"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

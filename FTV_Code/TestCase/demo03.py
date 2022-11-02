#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 19:40
# @Author  : wudong7182
# @Site    : 
# @File    : TwoSum.py
# @Software: PyCharm
import TestCase
import unittest
import threading
# from Android.Logcat import *
from Android.GetCurrentFocus import GetCurrentFocus
from audio.musicplayer import *
from airtest.core.android.adb import ADB
from Android.监测指定进程是否会挂掉 import *
from audio.player import Player


class TestDemo(unittest.TestCase):
    def setUp(self) -> None:  # 方法预期的返回值为None 非强制
        print("用例前置：未执行任何操作")

    def tearDown(self) -> None:

        print("断开adb设备" + str(ADB.devices()))

    def Wd_01(self):
        Path = "E:\\972\\FTV\\FTV_AutoTest_wudong\\audio\\MovieTest\\"
        mp = Player()
        mp.player(Path, delay=15, timeout=9999)

    def Wd_02(self):
        Speech = 监测指定进程是否会挂掉(psname="com.cvte.tv.ftvspeech")
        Speech.检测进程()


    def test_01(self):
        # t1 = threading.Thread(target=self.Wd_01)
        t2 = threading.Thread(target=self.Wd_02)
        t2.start()
        # t2.start()

    def wtest_02(self):
        CurrentFocusapp = GetCurrentFocus().GetCurrentFocusName()
        print(CurrentFocusapp)


if __name__ == '__main__':
    unittest.main()


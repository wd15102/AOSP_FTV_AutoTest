#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 16:39
# @Author  : wudong7182
# @Site    : 
# @File    : 按键相关.py
# @Software: PyCharm

import time
from airtest.core.android.adb import *

class 操作TV(ADB):
    """
        通过发送按键操作TV到达指定状态
        基于adb 发送 shell命令操作
        example：adb  shell keyevent HOME
        初始化参数：  self.serialno  待操作设备
                    self.delay  按键发送后延迟 x秒
    """
    def __init__(self, serialno, delay=2):
        self.serialno = serialno
        self.delay = delay
        self.devices = ADB(serialno=self.serialno)

    def 按下HOME键(self):
        self.devices.keyevent("HOME")
        time.sleep(self.delay)
        print("操作TV按下HOME")

    def 按下向上按键(self):
        self.devices.keyevent("19")
        time.sleep(self.delay)
        print("操作TV按向上按键")

    def 按下向下按键(self):
        self.devices.keyevent("20")
        time.sleep(self.delay)
        print("操作TV按向下按键")

    def 按下向左按键(self):
        self.devices.keyevent("21")
        time.sleep(self.delay)
        print("操作TV按向左按键")

    def 按下向右按键(self):
        self.devices.keyevent("22")
        time.sleep(self.delay)
        print("操作TV按向右按键")

    def 按下menu按键(self):
        self.devices.keyevent("82")
        time.sleep(self.delay)
        print("操作TV按menu按键")

    def 按下通道按键(self):
        self.devices.keyevent("178")
        time.sleep(self.delay)
        print("操作TV按通道按键")

    def 按下数字按键(self, number):
        key_number_list = ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        if 0 < number < 9:
            key_number = key_number_list[number]
            self.devices.keyevent(key_number)
            time.sleep(self.delay)
            print("操作TV按%d按键" % number)
        else:
            raise ValueError("数字按键必须是[0-9]的数字")

    def 按下enter按键(self):
        self.devices.keyevent("23")
        time.sleep(self.delay)
        print("操作TV按下enter按键")

    def 按下back按键(self):
        self.devices.keyevent("4")
        time.sleep(self.delay)
        print("操作TV按下back按键")

    def 按下语音按键(self):
        self.devices.keyevent("84")
        time.sleep(self.delay)
        print("操作TV按下语音按键")







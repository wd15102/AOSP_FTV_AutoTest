#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 14:57
# @Author  : wudong7182
# @Site    : 
# @File    : xbug.py
# @Software: PyCharm

import time
from airtest.core.android.adb import *

class XBUG(object):
    """
    ##########抓取xbug##########
    ##########需要提前准备U盘，U盘根目录创建文件夹，命令为：bug
    需要传入参数（设备ip）：ser
    example：ser=172.19.101.28
    """
    def __init__(self, ser):
        self.device = ADB(serialno=ser)
        self.device.cmd("root")
        print("已获取 adb 权限...")
        time.sleep(3)

    def 抓取xbug到U盘(self):
        x_log = self.device.shell("xbug")
        print(x_log)
        Xbug_date = self.device.shell("date")
        print("于TV系统时间" + Xbug_date + "抓取Xbug")





# XBUG(ser="172.19.101.28").抓取xbug到U盘()

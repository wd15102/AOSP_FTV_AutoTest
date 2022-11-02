# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 12:44
# @Author  : wudong7182
# @Site    :
# @File    : 监测指定进程是否会挂掉.py
# @Software: PyCharm
import TestCase
from airtest.core.api import *
from notify.通知到企业邮箱 import *

from Android.xbug import *
CrashCount = {}
class 监测指定进程是否会挂掉(object):
    """
    ##########监测指定进程是否会挂,挂掉后抓取xbug##########
    ##########需要提前准备U盘，U盘根目录创建文件夹，命令为：bug
    """

    def __init__(self, psname):
        self.psname = psname
        self.adb = TestCase.DEVICES()
        self.ser = TestCase.Ser()
        self.检测进程()

    def 检测进程(self):
        while True:
            print("已捕获到" + str(len(CrashCount)) + "次挂掉，具体挂掉的PID：" + str(CrashCount))
            speech_01 = shell("ps  | grep " + self.psname)
            res_01 = speech_01[14:19]
            sleep(5)
            speech_02 = shell("ps  | grep " + self.psname)
            res_02 = speech_02[14:19]
            if res_01 == res_02:
                date = shell("date")
                print("恭喜--" + self.psname + "进程还在，没挂！！，进程号：" + res_01)
                print("TV系统时间为：" + date)
            else:
                print("哦豁，进程：" + self.psname + "&&&进程号：" + res_01 + "好像挂了,不过别担心，已抓xbug....")
                Xbug_date = shell("date")
                CrashCount[res_01] = Xbug_date
                mail(speech_01)
                XBUG(ser=self.ser).抓取xbug到U盘()



# 监测指定进程是否会挂掉(psname="com.dangbei.mimir.lightos.home")

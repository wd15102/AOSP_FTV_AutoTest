#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 18:20
# @Author  : wudong7182
# @Site    : 
# @File    : DTV和launcher切换压测.py
# @Software: PyCharm
import TestCase
import time
from TV import 按键相关

def DTV_Launcher互切换压测():
    TV = 按键相关.操作TV(serialno="172.19.131.20")
    TV.按下向右按键()
    TV.按下enter按键()
    TV.按下enter按键()
    time.sleep(8)
    TV.按下HOME键()
    time.sleep(8)
    TV.按下语音按键()



T1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print("测试开始时间：" + T1)

for i in range(1, 9999):
    print("================执行第%d次压测================" % i)
    DTV_Launcher互切换压测()

T2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print("测试结束时间：" + T2)

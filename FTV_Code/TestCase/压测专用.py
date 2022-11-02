#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 16:49
# @Author  : wudong7182
# @Site    : 
# @File    : 压测专用.py
# @Software: PyCharm
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 19:18
# @Author  : wudong7182
# @Site    :
# @File    : 搜台压测.py
# @Software: PyCharm
import time
from TV import 按键相关
import TestCase
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import  sys
poco = AndroidUiautomationPoco()
Count = []
TV = 按键相关.操作TV(serialno="172.19.131.25")



def ATV自动搜台():
    TV.按下menu按键()
    TV.按下向右按键()
    TV.按下向右按键()
    TV.按下向右按键()
    TV.按下enter按键()
    TV.按下enter按键()
    TV.按下enter按键()
    time.sleep(260)

def 进入手动搜台界面():
    TV.按下back按键()
    TV.按下back按键()
    TV.按下back按键()
    TV.按下menu按键()
    TV.按下向右按键()
    TV.按下向右按键()
    TV.按下向右按键()
    TV.按下enter按键()
    TV.按下enter按键()
    TV.按下向下按键()
    TV.按下enter按键()

def 判断是否漏台():
    P_ID = poco("com.cvte.tv.setting:id/menufragment").child("android.widget.FrameLayout").offspring(
        "com.cvte.tv.setting:id/channel_list_detail").child("android.widget.LinearLayout").offspring(
        "android.support.v7.widget.RecyclerView").child("android.widget.FrameLayout")[-1].offspring(
        "com.cvte.tv.setting:id/tv_channel_id").get_text()
    P_NUM = poco("com.cvte.tv.setting:id/menufragment").child("android.widget.FrameLayout").offspring(
        "com.cvte.tv.setting:id/channel_list_detail").child("android.widget.LinearLayout").offspring(
        "android.support.v7.widget.RecyclerView").child()

    if len(P_NUM) == 8 and P_ID == "008":
        print("恭喜，本次ATV搜台搜到全部节目没有漏台 即将开始检查制式")
        判断制式()
    else:
        print("漏台了，快来看看吧")
        snapshot()

def 判断制式():
    进入手动搜台界面()
    for i in range(0, 8):
        sleep(2)
        Current_P = poco("com.cvte.tv.setting:id/menufragment").offspring("com.cvte.tv.setting:id/menulist").child(
            "android.widget.RelativeLayout")[0].child("com.cvte.tv.setting:id/summary").get_text()
        Current_video = poco("com.cvte.tv.setting:id/menufragment").offspring("com.cvte.tv.setting:id/menulist").child(
            "android.widget.RelativeLayout")[1].child("com.cvte.tv.setting:id/summary").get_text()
        Current_audio = poco("com.cvte.tv.setting:id/menufragment").offspring("com.cvte.tv.setting:id/menulist").child(
            "android.widget.RelativeLayout")[2].child("com.cvte.tv.setting:id/summary").get_text()
        if str(Current_P) == "1" and Current_video == "PAL" and Current_audio == "BG":
            print("当前频道：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        elif str(Current_P) == "2" and Current_video == "NTSC" and Current_audio == "M/N":
            print("当前频道：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        elif str(Current_P) == "3" and Current_video == "PAL" and Current_audio == "M/N":
            print("当前频道：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        elif str(Current_P) == "4" and Current_video == "NTSC" and Current_audio == "M/N":
            print("当前频道：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        elif str(Current_P) == "5" and Current_video == "SECAM" and Current_audio == "DK":
            print("当前频道：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        elif str(Current_P) == "6" and Current_video == "PAL" and Current_audio == "I":
            print("当前频道：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        elif str(Current_P) == "7" and Current_video == "NTSC" and Current_audio == "M/N":
            print("当前频道：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        elif str(Current_P) == "8" and Current_video == "PAL" and Current_audio == "DK":
            print("当前频道" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
        else:
            snapshot()
            print("识别错误的当前频道号：" + str(Current_P) + " 的视频制式为：" + Current_video+" 声音制式为："+Current_audio)
            sys.exit()

        TV.按下向右按键()

for i in range(1, 1000):
    print("开始执行第%d次压测" % i)
    sleep(2)
    ATV自动搜台()
    TV.按下enter按键()
    判断是否漏台()
    TV.按下back按键()
    TV.按下back按键()
    TV.按下back按键()
    TV.按下back按键()
    TV.按下back按键()

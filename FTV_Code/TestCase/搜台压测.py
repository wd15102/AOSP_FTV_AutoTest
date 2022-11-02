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
ser = TestCase.Ser()
device = TestCase.DEVICES()
TV = 按键相关.操作TV(serialno=ser)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()
Count = []

HISI_352_ATV_Programe_ID = poco("com.cvte.tv.setting:id/menufragment"
                                ).child("android.widget.FrameLayout").offspring(
         "com.cvte.tv.setting:id/channel_list_detail").child(
         "android.widget.LinearLayout").offspring(
         "android.support.v7.widget.RecyclerView").child(
         "android.widget.FrameLayout")[8].offspring(
          "com.cvte.tv.setting:id/tv_channel_id").get_text()

HISI_352_ATV_Programe_Name =  poco("com.cvte.tv.setting:id/menufragment"
                                   ).child("android.widget.FrameLayout").offspring(
        "com.cvte.tv.setting:id/channel_list_detail").child(
        "android.widget.LinearLayout").offspring(
        "android.support.v7.widget.RecyclerView").child(
        "android.widget.FrameLayout")[8].offspring(
        "com.cvte.tv.setting:id/tv_channel_name").get_text()




def HISI_352ATV自动搜台压测():
    TV.按下menu按键()
    TV.按下向右按键()
    TV.按下向右按键()
    TV.按下向下按键()
    TV.按下enter按键()
    TV.按下enter按键()
    time.sleep(150)


def 判断第009号节目():
    P_ID = HISI_352_ATV_Programe_ID
    P_NAME = HISI_352_ATV_Programe_Name

    if P_ID == "009" and P_NAME == "高清翡翠台":
        print("恭喜，第一页频道列表中最后一个节目是%s" % P_NAME)
    else:
        snapshot()


def 判断第012号节目():
    try:
        P_ID = poco("com.cvte.tv.setting:id/menufragment").child("android.widget.FrameLayout").offspring(
            "com.cvte.tv.setting:id/channel_list_detail").child("android.widget.LinearLayout").offspring(
            "android.support.v7.widget.RecyclerView").child("android.widget.FrameLayout")[8].offspring(
            "com.cvte.tv.setting:id/tv_channel_id").get_text()
        P_NAME = poco("com.cvte.tv.setting:id/menufragment").child("android.widget.FrameLayout").offspring(
            "com.cvte.tv.setting:id/channel_list_detail").child("android.widget.LinearLayout").offspring(
            "android.support.v7.widget.RecyclerView").child("android.widget.FrameLayout")[8].offspring(
            "com.cvte.tv.setting:id/tv_channel_name").get_text()
    except Exception as e:
        raise e
        snapshot()

    if P_ID == "012" and P_NAME == "cs-cctv-1":
        print("恭喜，频道列表中最后一个节目是%s" % P_NAME)
    else:
        print("哎呀，频道列表中最后一个节目是%s" % P_NAME)
        snapshot()


def 判断ATV搜台是否漏台(T):
    '''
    方法：打开频道列表判断列表中存储的节目元素数量是否==8
    :param T: 用于统计第T次搜台压测
    :return:
    '''
    try:
        P_ID = poco("android.widget.FrameLayout").offspring("com.cvte.tv.setting:id/channel_content").child(
            "android.widget.LinearLayout").offspring("com.cvte.tv.setting:id/channel_list").child(
            "android.widget.FrameLayout")[-1].offspring("com.cvte.tv.setting:id/tv_channel_id").get_text()

        P_NUM = poco("android.widget.FrameLayout").offspring("com.cvte.tv.setting:id/channel_content")\
            .child("android.widget.LinearLayout").offspring("com.cvte.tv.setting:id/channel_list").child()

        P_NAME = poco("android.widget.FrameLayout").offspring("com.cvte.tv.setting:id/channel_content").child(
            "android.widget.LinearLayout").offspring("com.cvte.tv.setting:id/channel_list").child(
            "android.widget.FrameLayout")[-1].offspring("com.cvte.tv.setting:id/tv_channel_name").get_text()

    except Exception as e:
        raise e
        snapshot(msg="出现异常")
    if len(P_NUM) == 8 and P_ID == "008" or P_NAME == "CH8" or P_NAME == "VT4":
        print(">>本次搜台累计搜到%s个节目" % len(P_NUM))
        print(">>>本次搜台最后一个节目号是%s" % P_ID)
        print("最后一个节目名是%s" % P_NAME)
        print("恭喜龙哥!!!!，本次ATV搜台搜到全部节目没有漏台")
    else:
        Xbug_date = shell("date")
        Count.append(T)
        print("哎呀，好像漏台了啊 最后一个节目号是%s" % P_ID)
        # snapshot()
        print("最后一个节目名是%s" % P_NAME)
        print("已累计漏台%d次" % len(Count))
        shell("root")
        print("于TV系统时间" + Xbug_date + "抓取Xbug")
        shell("xbug")


# r = snapshot()
# print(r)

for i in range(1, 10000):
    print("开始执行第%d次压测" % i)
    HISI_352ATV自动搜台压测()
    TV.按下enter按键()
    判断ATV搜台是否漏台(i)
    TV.按下back按键()
    TV.按下back按键()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 16:59
# @Author  : wudong7182
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from Android.设备ip地址及串口信息 import *

Serialno = "172.19.101.23"

def DEVICES():
    # print(Ser)
    device = 设备IP地址及串口信息(ip=Serialno).ADB连接TV()
    print("==>已经连接adb设备：" + Serialno)
    return device

def Ser():
    return Serialno

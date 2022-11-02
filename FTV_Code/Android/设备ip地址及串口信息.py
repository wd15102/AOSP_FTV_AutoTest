#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:31
# @Author  : wudong7182
# @Site    : 
# @File    : 设备ip地址及串口信息.py
# @Software: PyCharm
"""
  运行前必要的配置
"""
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class 设备IP地址及串口信息(object):
    # 往这里添加设备的IP地址和对应端口号(串口还未做支持)
    def __init__(self, ip, port="5555"):
        if ip is None:
            self.ip = None
        else:
            self.ip = ip
            self.port = port
            self.ADB连接TV()

    def ADB连接TV(self):
        """
                需要输入IP和端口号
                ip：172.19.103.21
                port：5555
            """
        print("正在连接adb设备：%s" % self.ip)
        if not cli_setup():
            Device = auto_setup(__file__, logdir=True, devices=[
                "Android://127.0.0.1:5037/" + self.ip + ":" + self.port+"?cap_method=JAVACAP"])
            return Device


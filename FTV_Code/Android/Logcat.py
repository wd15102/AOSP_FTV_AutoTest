#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 12:44
# @Author  : wudong7182
# @Site    : 
# @File    : Logcat.py
# @Software: PyCharm
import os
import re
import subprocess
import time
import serial
import TestCase
from airtest.core.api import *


class 串口操作(object):
    def __init__(self, PORT, BPS, TIMEOUT=5):
        """
        :param PORT:     COM4
        :param BPS:      115200
        :param TIMEOUT:  5   超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        """
        try:
            # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM4 等
            self.PORT = PORT

            # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
            self.BPS = BPS

            # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
            self.TIMEOUT = TIMEOUT

            # 打开串口，并得到串口对象
            self.ser = serial.Serial(self.PORT, self.BPS, timeout=self.TIMEOUT)
            self.ser.write("xu 7411\r\n".encode("gbk"))  # 提权
            self.ser.write("su 7411\r\n".encode("gbk"))
            self.ser.write("cd /\r\n".encode("gbk"))  # 进入 根目录
            print("串口状态：", self.ser)
        except Exception as e:
            print("---异常---：%s" % e)

    def 后台抓取logcat(self):
        cmd = "logcat -v threadtime -f data/logcat.log&\r\n"
        self.run(cmd)  # 执行cmd命令
        print("执行串口命令抓取logcat:", cmd)

    def 停止抓取Logcat(self):
        cmd = "kill % 1\r\n"
        self.run(cmd)
        print("已停止抓取logcat，保存路径：data/logcat.log")

    def read(self):
        pass
        # every_time = time.strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
        # while True:
        #     data = self.ser.readline()
        #     print(every_time, data.decode('utf-8'))

    def run(self, cmd):
        if cmd:
            CMD = cmd + "\r\n"
            print("执行串口命令:", CMD)
            if self.ser.is_open:
                try:
                    self.ser.write(CMD.encode("gbk"))  # 写数据
                    # self.read()
                except Exception as e:
                    print("---串口操作异常---：%s" % e)
            else:
                self.ser = serial.Serial(self.PORT, self.BPS, timeout=self.TIMEOUT)
                self.run()
        self.exit()

    def exit(self):
        self.ser.close()  # 关闭串口
        print("已关闭串口")


# ser = 串口操作(PORT="COM4", BPS=115200)
# ser.后台抓取logcat()
# ser.read()
# ser.exit()

class Speech_Log(object):
    def __init__(self, tagFilter, keywordFilter):
        """
        adb  logcat 处理类
        """
        self.ser = TestCase.Ser()
        print(self.ser)
        self.Count = 0
        shell("logcat -c")
        self.tagFilter = tagFilter  # 唤醒："ResearchReceiver"
        self.keywordFilter = keywordFilter
        self.keyword_reg = r".*" + self.keywordFilter + ".*"  # 正则表达式
        self.ExcShell = "adb -s " + self.ser + " logcat -v threadtime raw -s " + self.tagFilter + " | grep " + self.keywordFilter

    def WakeupLog(self):
        """
                FTV 唤醒次数日志处理
                :return:
                """
        WakeCount = 0
        print("执行命令：", self.ExcShell)
        p_obj = subprocess.Popen(
            args=self.ExcShell,
            stdin=None, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=False)

        # 实时监控并过滤每一行生成的日志里的关键字
        print("开始实时监控...")
        # fn = "aa.csv"
        # f = open(fn, 'a+', newline='')
        with p_obj:
            for line in p_obj.stdout:
                if re.match(self.keyword_reg, line.decode("utf-8")):
                    line_res = line.decode("utf-8")
                    WakeCount += 1
                    print("—>已唤醒次数：" + str(WakeCount) + ", 唤醒词：" + (line_res[-6:-1]))
                    print("—>>>>当前TV时间是：" + (line_res[0:20]))
            # f.close()
        os.system("pause")

    def SpeechLog(self):
        """
        FTV 语音日志处理
        :return:
        """
        CountDic = {}
        WakeupWord_list = [
            "小源小源",
            "播放",
            "暂停",
            "继续播放",
            "上一曲",
            "下一曲",
            "上一集",
            "下一集",
            "静音",
            "增大音量",
            "打开声音",
            "退出",
            "返回主页"
        ]
        for i in WakeupWord_list:
            CountDic[i] = 0
        #
        print("执行命令：", self.ExcShell)
        p_obj = subprocess.Popen(
            args=self.ExcShell,
            stdin=None, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=False)

        # 实时监控并过滤每一行生成的日志里的关键字
        c = 0
        count = []
        print("开始实时监控...")
        resfile = "result.txt"
        # Out_file = open(resfile, 'w', encoding="utf8")
        fn = "aa.csv"
        f = open(fn, 'a+', newline='')
        with p_obj:
            for line in p_obj.stdout:
                if re.match(self.keyword_reg, line.decode("utf-8")):
                    line_res = line.decode("utf-8")
                    c = c + 1
                    count.append(c)
                    r = count[-1]
                    print(line_res)
                    print("===================已查询到 %d 次天气==========" % r)
                    # csv_write = csv.writer(f)
                    # data_row = [line_res]
                    # csv_write.writerow(data_row)
                    # WakeupTime = line_res[6:14]
                    # WakeupWord = line_res[-6:-1]
                    # print(line_res[0:14])
                    # Out_file.close()
                    # print("命令词: %s" % WakeupWord)
                    # print("于TV时间：%s" % WakeupTime, "被误触发....")
                    # WakeupWord = line_res[-6:-1]
                    # Out_file.writelines(WakeupWord)
            f.close()
        os.system("pause")


# registerHotWord
# Logcat(tagFilter="ResearchReceiver ", keywordFilter="wakeupWordIndex").WakeupLog()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 16:19
# @Author  : wudong7182
# @Site    : 
# @File    : 972压测.py
# @Software: PyCharm


import re
import TestCase
import unittest
from TV import 按键相关
from Android.xbug import *
from airtest.core.api import *
from notify.通知到企业邮箱 import mail
T1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


class TestDemo(unittest.TestCase):
    def setUp(self) -> None:  # 方法预期的返回值为None 非强制
        print("测试准备...")
        TestCase.DEVICES()
        self.ser = TestCase.Ser()
        self.TV = 按键相关.操作TV(serialno=self.ser)
        self.file = os.path.basename(__file__)
        self.filename = self.file.split('.')

    def tearDown(self) -> None:
        # self.ser
        self.task_name = self.filename[0] + "_" + self.Launcher和各种APP互相切换压测.__name__
        mail(self.task_name)
        print("完成测试： ", self.ser)

    def Launcher和各种APP互相切换压测(self):
        res = True
        packages = [
            # "com.cvte.tv.weather/com.cvte.tv.weather.MainActivity",
            # "com.cvte.settings",
            "com.mgtv.tv.intl/com.mgtv.tv.oversea.launcher.module.OverseaChannelActivity"
            # "com.seraphic.openinet.cvte",
            # "com.droidlogic.miracast/com.droidlogic.miracast.WiFiDirectMainActivity",
            # "com.cvte.tv.media",
            # "com.maxhub.screenshare.server.tv",
            # "com.cvte.tv.pictorial/com.cvte.screensaver.activity.ElephantGroupActivity",
            # " com.stark.store/com.stark.store.applist.ui.AppListActivity",
            # "com.stark.store",
            # "com.spotify.tv.android",
            # "com.google.android.youtube.tv",
            # "com.bstar.intl.tv/com.bstar.intl.tv.MainActivity"
            # "com.tencent.qqlivei18n",
            # "com.ted.android.tv/com.ted.android.tv.view.MainActivity"
        ]
        for p in packages:
            exe = "am start " + p
            shell(exe)
            print("已启动应用：%s" % p)
            sleep(30)
            self.TV.按下向下按键()
            self.TV.按下enter按键()
            sleep(10)
            self.TV.按下back按键()
            self.TV.按下向右按键()
            self.TV.按下enter按键()
            sleep(10)
            self.TV.按下back按键()
            self.TV.按下向右按键()
            self.TV.按下enter按键()
            exe = "am force-stop " + p
            shell(exe)
            print("已强制停止应用：%s" % p)
            sleep(2)
            self.TV.按下HOME键()
            self.TV.按下HOME键()
            self.TV.按下向右按键()
            try:
                # exists(Template(r"tpl1661409789982.png", record_pos=(-0.155, -0.128), resolution=(1920, 1080)))
                res = assert_exists(
                    Template(r"tpl1661485295905.png", record_pos=(-0.157, -0.156), resolution=(1920, 1080)),
                    "多媒体标签页黑屏检测")
                if res:
                    print("恭喜！！！本次打开应用：%s 回到主页之后没有检测到黑屏" % p)


            except Exception as e:
                print("可能黑屏了 快来看看吧！！")
                snapshot()
                XBUG(ser=self.ser).抓取xbug到U盘()
                break


    def test_01(self):
        print("测试开始时间：" + T1)
        XBUG(self.ser)
        for i in range(1, 9999):
            print("================执行第%d次压测================" % i)
            print("测试时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            self.Launcher和各种APP互相切换压测()
            print("恭喜！！！第 " + str(i) + " 次压测没有检测到黑屏")
        # t2.start()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemo("test_01"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    T2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print("测试结束时间：" + T2)

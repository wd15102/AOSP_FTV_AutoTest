#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 11:38
# @Author  : wudong7182
# @Site    : 
# @File    : player.py
# @Software: PyCharm

from playsound import playsound
import os
import time

"""
播放音频文件
"""


class Player(object):

    def player(self, Path, delay, timeout):
        print(Path)
        path_list1 = os.listdir(Path)
        path_list1.sort()  # 对读取的路径进行排序
        Count = 1
        while True:
            if Count == timeout:
                break
            for filename1 in path_list1:  # 遍历该文件夹下所有音频文件并进行播放
                sound = Path + filename1
                if filename1.endswith(".mp3"):
                    print("第%d次循环" % Count)
                    print("正在播放音频：", filename1)
                    playsound(sound)
                    print("==================================  %s 秒后播放下一曲==============================\n" % delay)
                    time.sleep(delay)
                    # Count = Count + 1
                else:
                    break
            Count = Count + 1


# Path = "E:\\FTV_Code\\audio\\SongerTest\\"
# p = Player()
# p.player(Path, delay=5, timeout=9999)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 9:28
# @Author  : wudong7182
# @Site    : 
# @File    : Pic.py
# @Software: PyCharm


import cv2
import time

def Filename():
    F = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    filename = "E:/Rof/DEBUG/" + F + ".png"
    return filename

def 截屏(delay):
    """
    截屏次数：delay次
    下一次截屏延迟：默认5s
    """
    cap = cv2.VideoCapture(1)  # 打开摄像头:
    ret, frame = cap.read()
    time.sleep(5)
    while delay:   # 截屏次数：delay次
        filename = Filename()
        time.sleep(5)  # 截屏延迟：5秒
        cv2.imwrite(filename, frame)  # 保存路径
        print("已保存截图"+filename)
        delay = delay - 1
    cap.release()
    cv2.destroyAllWindows()

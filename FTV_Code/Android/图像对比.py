#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 15:44
# @Author  : wudong7182
# @Site    : 
# @File    : 图像对比.py
# @Software: PyCharm

from airtest.core.api import *
from airtest.core.cv import Predictor
class 图像对比():

    def __init__(self, Temp, pos):
        self.Temp = Temp
        self.pos = pos
        self.resolution = (1920, 1080)

        """
        参数   Temp: target to be checked
        """
        exists(Template(self.Temp, record_pos=(-0.155, -0.128), resolution=self.resolution))

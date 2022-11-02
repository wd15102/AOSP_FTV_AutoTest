#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 9:26
# @Author  : wudong7182
# @Site    : 
# @File    : musicplayer.py
# @Software: PyCharm
import time

"""
 Google Text-to-Speech：gTTS
 该类：musicplayer  旨在实现自动将歌手、电影类型 名单转换为单独的音频文件 用于自动化测试、压力测试、问题回归
"""
import os
from gtts import gTTS
from audio.player import *


class MusicPlayer(object):

    def __init__(self, path):
        """
        :param path : 在这个路径下创建歌手测试音频
        """
        self.path = path
        print(self.path)
        self.folder = os.path.exists(self.path)
        if not self.folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(self.path)
        os.chdir(self.path)  # 切换当前路径到path路径下

    def 创建测试音频(self, file):
        """
        :param file:  读取源文件
        :return:
        """
        for line in open(file, 'r', encoding="utf8"):  # 循环读取源文件歌手名
            audio = gTTS(text=line, lang="zh-cn")  # 转TTS
            Filename = line.replace("\n", "")
            print("已保存音频文件===> %s.mp3 !!!!!!!" % Filename)  # 文件名需要去掉换行符号
            audio.save(Filename + ".mp3")  # 保存成mp3音频
        print("创建成功，在===> " + self.path + " 文件夹看看吧...")

    def SongerTestMaker(self, ref):
        """
        ref:歌手名单   格式要求：一个歌手独占一行
        :return: None
        """

        Out_file_filename = "music_nlp.txt"
        From_file = open(ref, 'r', encoding="utf8")
        Out_file = open(Out_file_filename, 'w', encoding="utf8")
        for each_line in From_file:
            each_line_list = list(each_line)
            # print(each_line_list)
            each_line_list.insert(0, "1,小源小源")
            # each_line_list.insert(-1, "的歌")
            Out_file.writelines("".join(each_line_list))
        From_file.close()
        Out_file.close()
        self.创建测试音频(Out_file_filename)

    def MovieTestMaker(self, ref):
        """
        ref:待测电影类型名单   格式要求：一个电影类型独占一行：比如：美剧
        :return: None
        """

        Out_file_filename = "MovieTest.txt"
        From_file = open(ref, 'r', encoding="utf8")
        Out_file = open(Out_file_filename, 'w', encoding="utf8")
        for each_line in From_file:
            each_line_list = list(each_line)
            # print(each_line_list)
            each_line_list.insert(0, "1,小源小源，我要看")  # 加入"1," 是为了避免起播时第一个音发不出来，没找到原因
            each_line_list.insert(-1, "的电影")
            Out_file.writelines("".join(each_line_list))
        From_file.close()
        Out_file.close()
        self.创建测试音频(Out_file_filename)



if __name__ == '__main__':
    Path = "E:\\FTV_Code\\audio\\"
    mp = MusicPlayer(path=Path)
    mp.创建测试音频("eshare.txt")
    # mp.SongerTestMaker("true_audio.txt")
    # mp.MovieTestMaker("movie.txt")
    # mp = Player()
    # mp.player(Path, delay=5, timeout=9999)

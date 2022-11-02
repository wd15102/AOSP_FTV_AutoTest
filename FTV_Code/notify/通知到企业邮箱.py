#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 20:13
# @Author  : wudong7182
# @Site    : 
# @File    : 通知到企业邮箱.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人邮箱账号
发件人 = 'wudong7182@cvte.com'
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
my_pass = 'CVte15102'
# 收件人邮箱账号
收件人 = '1693181103@qq.com'



def mail(task):
    ret = True
    try:
        # 邮件内容
        msg = MIMEText("您所执行的压测任务 " + str(task) + "已停止 已抓取log 请及时关注....", 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["软件设计平台/系统测试部：吴东", 发件人])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["Dear：", 发件人])
        # 邮件的主题
        msg['Subject'] = task

        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(发件人, my_pass)
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(发件人, [发件人, ], msg.as_string())
        # 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception:
        ret = False
        print("邮件发送失败")
    else:
        print("邮件发送成功")
    return ret



import time
import random
import datetime
import os
import sys
import re
import json
import requests
import pandas as pd
from tkinter import messagebox


class WeiboUserPosted:
    """微博用户主页帖子采集模块

    负责：
    1. 遍历用户链接列表
    2. 分页获取用户发布的微博列表
    3. 支持关键词/时间筛选
    4. 长微博文本展开
    5. CSV输出
    """

    def __init__(self, user_link_list, top_num, keyword, start_date, end_date, txt_msglist, logger):
        self.user_link_list = user_link_list
        self.top_num = int(top_num)
        self.keyword = keyword
        self.start_date = start_date
        self.end_date = end_date
        self.txt_msglist = txt_msglist
        self.logger = logger
        self.describe = []
        self.cookie = self.get_cookie()
        self.wait_sec = self.get_config_pub()
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.result_file = '微博博主帖子_{}.csv'.format(now)

    def get_cookie(self):
        """[专有代码已移除] 从 cookie.txt 读取cookie"""
        return ""

    def get_config_pub(self):
        try:
            with open('config_pub.json', 'r') as file:
                text = json.load(file)
            wait_sec = text['wait_sec']
            if wait_sec < 1:
                self.tk_show('\n等待时长需至少1秒，请重新配置！')
                exit(1)
            self.tk_show(f'\n读取config_pub成功, 等待间隔是:{wait_sec}s')
        except Exception as e:
            wait_sec = ''
            self.tk_show('\n读取config_pub失败！请检查config_pub.json')
            self.tk_show(str(e))
            exit(1)
        return wait_sec

    def tk_show(self, context):
        self.logger.info(context)
        self.txt_msglist.delete('1.0', 'end')
        self.describe.append(context)
        self.txt_msglist.insert('insert', '\n'.join(self.describe))
        self.txt_msglist.see("end")

    def trans_time(self, v_time_str):
        timeArray = time.strptime(v_time_str, "%a %b %d %H:%M:%S +0800 %Y")
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    def trans_time2(self, v_date_str):
        timeArray = time.strptime(v_date_str, "%Y-%m-%d")
        return int(time.mktime(timeArray))

    def get_long(self, mid):
        """[专有代码已移除] 获取长微博完整文本"""
        return ""

    def get_user_posted(self):
        """[专有代码已移除] 采集用户主页微博列表

        原实现核心流程：
        1. 从用户链接提取uid
        2. 构造用户帖子搜索API请求参数
        3. 支持关键词/时间范围筛选
        4. 分页请求帖子列表
        5. 解析帖子JSON（内容、互动数据、图片等）
        6. 检测长微博并展开完整文本
        7. 写入CSV
        """
        self.tk_show('\n[专有代码已移除] 用户帖子采集功能需要专有实现')
        messagebox.showinfo('提示', '用户帖子采集功能需要专有实现，未包含在本开源版本中')

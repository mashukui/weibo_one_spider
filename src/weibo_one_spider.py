import time
import random
import datetime
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import logging
from logging.handlers import TimedRotatingFileHandler
import threading
import webbrowser
import json
import re
import sys
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

from weibo_search import WeiboSearchSpider
from weibo_user_post import WeiboUserPosted
from weibo_comment import WeiboCommentSpider
from weibo_userinfo import WeiboUserInfoSpider


class Log_week():
    def get_logger(self):
        self.logger = logging.getLogger(__name__)
        formatter = '[%(asctime)s-%(filename)s][%(funcName)s-%(lineno)d]--%(message)s'
        self.logger.setLevel(logging.DEBUG)
        sh = logging.StreamHandler()
        log_formatter = logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M:%S')
        info_file_name = time.strftime("%Y-%m-%d") + '.log'
        case_dir = r'./logs/'
        info_handler = TimedRotatingFileHandler(filename=case_dir + info_file_name,
                                                when='MIDNIGHT',
                                                interval=1,
                                                backupCount=7,
                                                encoding='utf-8')
        self.logger.addHandler(sh)
        sh.setFormatter(log_formatter)
        self.logger.addHandler(info_handler)
        info_handler.setFormatter(log_formatter)
        return self.logger


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        self.func = func
        self.args = args
        self.setDaemon(True)
        self.start()

    def run(self):
        self.func(*self.args)


def validate_date_format(date_str, label=''):
    date_str = date_str.strip()
    if not date_str:
        return True
    if not re.match(r'^\d{4}-\d{2}-\d{2}( \d{2}:\d{2}:\d{2})?$', date_str):
        messagebox.showerror('时间格式错误',
                             f'{label}时间格式不正确！\n\n要求格式: YYYY-MM-DD 或 YYYY-MM-DD HH:MM:SS\n\n当前输入: {date_str}')
        return False
    return True


def compare_start_end_dates(start_date, end_date):
    if not start_date or not end_date:
        return True
    try:
        start_dt = datetime.datetime.strptime(start_date.strip(), '%Y-%m-%d %H:%M:%S')
        end_dt = datetime.datetime.strptime(end_date.strip(), '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            start_dt = datetime.datetime.strptime(start_date.strip(), '%Y-%m-%d')
            end_dt = datetime.datetime.strptime(end_date.strip(), '%Y-%m-%d')
        except ValueError:
            return True
    if start_dt >= end_dt:
        messagebox.showerror('时间范围错误', '起始时间不能晚于或等于结束时间！')
        return False
    return True


def open_sugg():
    webbrowser.open("https://docs.qq.com/sheet/DVGxzT0VVSkVzSW1u?tab=cc8q6g", new=0)


class WeiboSpiderTool:
    def __init__(self, root):
        self.root = root
        self.root.title('爬微博聚合软件v2.0 | 马哥python说 | 公众号: 老男孩的平凡之路')
        self.root.minsize(width=850, height=715)
        try:
            self.root.iconbitmap('mage.ico')
        except:
            pass
        self.create_menu()
        self.create_tabs()
        self.create_bottom_info()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="关于软件", command=self.show_about)
        file_menu.add_command(label="使用协议", command=self.show_agreement)
        if 'open_sugg' in globals():
            file_menu.add_command(label="意见收集", command=open_sugg)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def create_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="搜索微博")
        self.notebook.add(self.tab2, text="博主主页")
        self.notebook.add(self.tab3, text="微博评论")
        self.notebook.add(self.tab4, text="用户信息")
        self.init_tab1()
        self.init_tab2()
        self.init_tab3()
        self.init_tab4()

    def init_tab1(self):
        """初始化微博搜索Tab页"""
        pass

    def init_tab2(self):
        """初始化博主主页Tab页"""
        pass

    def init_tab3(self):
        """初始化微博评论Tab页"""
        pass

    def init_tab4(self):
        """初始化用户信息Tab页"""
        pass

    def create_bottom_info(self):
        claim = tk.Label(self.root,
                         text='免责声明: 禁止使用该软件从事任何违法活动，否则由此产生的一切法律后果由软件使用者自行承担，与软件开发作者无关！',
                         font=('微软', 10), fg='red')
        claim.place(x=50, y=660)
        copyright = tk.Label(self.root, text='@马哥python说 All rights reserved.', font=('仿宋', 10), fg='grey')
        copyright.place(x=290, y=675)

    def task1(self, txt_msglist):
        """[专有代码已移除] 微博搜索任务"""
        txt_msglist.delete('1.0', 'end')
        txt_msglist.insert('insert', '[专有代码已移除] 搜索采集功能需要专有实现')

    def task2(self, txt_msglist):
        """[专有代码已移除] 博主主页采集任务"""
        txt_msglist.delete('1.0', 'end')
        txt_msglist.insert('insert', '[专有代码已移除] 用户帖子采集功能需要专有实现')

    def task3(self, txt_msglist):
        """[专有代码已移除] 微博评论采集任务"""
        txt_msglist.delete('1.0', 'end')
        txt_msglist.insert('insert', '[专有代码已移除] 评论采集功能需要专有实现')

    def task4(self, txt_msglist):
        """[专有代码已移除] 用户信息采集任务"""
        txt_msglist.delete('1.0', 'end')
        txt_msglist.insert('insert', '[专有代码已移除] 用户信息采集功能需要专有实现')

    def open_url(self, event):
        webbrowser.open("https://www.zhihu.com/zvideo/1831601214263021568", new=0)

    def show_about(self):
        messagebox.showinfo("关于软件",
                            '版本记录:\nv1.0-v2.0: 微博聚合工具\n\n最新版软件包获取：\n公众号 "老男孩的平凡之路" 后台回复：微博')

    def show_agreement(self):
        messagebox.showinfo("使用协议",
                            """欢迎使用本软件！在使用前，请仔细阅读以下使用协议：

授权与许可：本软件仅授权用户用于合法的个人或商业用途。禁止使用本软件进行任何违法活动，包括但不限于未经授权的数据采集、侵犯知识产权和侵犯隐私权等。
责任限制：本软件开发者不对用户因使用本软件而导致的任何直接或间接损失负责。用户在使用过程中应遵守相关法律法规，并自行承担因使用本软件而产生的风险和责任。
数据隐私：本软件不会收集、存储或分享用户的个人数据。用户采集的数据应严格遵守数据保护法律和目标网站的使用政策。
更新与维护：我们有权随时对本软件进行更新和维护，用户应及时下载并安装更新，以确保软件的正常使用。
协议修改：我们保留随时修改本使用协议的权利，修改后的协议将在发布后立即生效。用户继续使用本软件即表示接受新的协议条款。

作为软件使用者，您默认接受以上协议条款。感谢理解与支持。如有疑问，请联系作者。""")


def create_login_root():
    root_login = tk.Tk()
    root_login.title('爬微博聚合软件v2.0 | 马哥python说')
    root_login.minsize(width=400, height=300)
    try:
        root_login.iconbitmap('mage.ico')
    except:
        pass
    menu_bar = tk.Menu(root_login)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="关于软件", command=lambda: messagebox.showinfo("关于软件",
                          '版本记录:\nv1.0-v2.0: 微博聚合工具\n\n最新版软件包获取：\n公众号 "老男孩的平凡之路" 后台回复：微博'))
    file_menu.add_command(label="使用协议", command=lambda: messagebox.showinfo("使用协议",
                          """欢迎使用本软件！在使用前，请仔细阅读以下使用协议：

授权与许可：本软件仅授权用户用于合法的个人或商业用途。禁止使用本软件进行任何违法活动，包括但不限于未经授权的数据采集、侵犯知识产权和侵犯隐私权等。
责任限制：本软件开发者不对用户因使用本软件而导致的任何直接或间接损失负责。用户在使用过程中应遵守相关法律法规，并自行承担因使用本软件而产生的风险和责任。
数据隐私：本软件不会收集、存储或分享用户的个人数据。用户采集的数据应严格遵守数据保护法律和目标网站的使用政策。
更新与维护：我们有权随时对本软件进行更新和维护，用户应及时下载并安装更新，以确保软件的正常使用。
协议修改：我们保留随时修改本使用协议的权利，修改后的协议将在发布后立即生效。用户继续使用本软件即表示接受新的协议条款。

作为软件使用者，您默认接受以上协议条款。感谢理解与支持。如有疑问，请联系作者。"""))
    if 'open_sugg' in globals():
        file_menu.add_command(label="意见收集", command=open_sugg)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root_login.config(menu=menu_bar)
    label_title = ttk.Label(root_login, text="用户登录", font=("Helvetica", 20, "bold"), background="#f0f4f7")
    label_title.pack(pady=20)
    frame_username = ttk.Frame(root_login)
    frame_username.pack(pady=10)
    label_username = ttk.Label(frame_username, text="账号:", font=("Helvetica", 12), width=10)
    label_username.pack(side="left", padx=5)
    entry_username = ttk.Entry(frame_username, font=("Helvetica", 12), width=20)
    entry_username.pack(side="right")
    frame_password = ttk.Frame(root_login)
    frame_password.pack(pady=10)
    label_password = ttk.Label(frame_password, text="密码:", font=("Helvetica", 12), width=10)
    label_password.pack(side="left", padx=5)
    entry_password = ttk.Entry(frame_password, font=("Helvetica", 12), width=20, show="*")
    entry_password.pack(side="right")

    def login():
        messagebox.showinfo('登录成功', '开源版本无需验证，直接进入主界面')
        root_login.destroy()
        create_spider_root()

    frame_buttons = ttk.Frame(root_login)
    frame_buttons.pack(pady=20)
    btn_login = ttk.Button(frame_buttons, text="登录", command=login, width=10)
    btn_login.grid(row=0, column=0, padx=10)
    btn_quit = ttk.Button(frame_buttons, text="退出", command=lambda: [root_login.destroy(), sys.exit()], width=10)
    btn_quit.grid(row=0, column=1, padx=10)
    copyright = tk.Label(root_login, text='@马哥python说 All rights reserved.', font=('仿宋', 10), fg='grey')
    copyright.place(x=80, y=275)
    root_login.protocol("WM_DELETE_WINDOW", lambda: [root_login.destroy(), sys.exit()])
    root_login.mainloop()


def create_spider_root():
    work_path = os.getcwd()
    if not os.path.exists(work_path + "/logs"):
        os.makedirs(work_path + "/logs")
    root = tk.Tk()
    app = WeiboSpiderTool(root)
    root.protocol("WM_DELETE_WINDOW", lambda: [root.destroy(), sys.exit()])
    root.mainloop()


if __name__ == "__main__":
    if not os.path.exists('logs'):
        os.mkdir('logs')
    log = Log_week()
    logger = log.get_logger()
    create_login_root()

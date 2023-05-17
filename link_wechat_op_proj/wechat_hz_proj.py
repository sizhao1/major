# import pyautogui
# import pyperclip
# import time
# from openpyxl import load_workbook
#
#
# def get_msg():
#     # txt文件设置要发送的内容，每条信息空行分开
#     file = open(r'D:\\abc.txt', 'r', encoding='utf-8')
#     reder = file.read()
#     content = reder.split('\n')
#     return content
#
#
# def send(msg):
#     # 赋值需要发送的内容到粘贴板
#     pyperclip.copy(msg)
#     # 模拟键盘复制粘贴动作
#     pyautogui.hotkey('ctrl', 'v')
#     # 发送信息
#     pyautogui.press('enter')
#
#
# def send_msg(friend):
#     # 模拟打开微信
#     pyautogui.hotkey('ctrl', 'alt', 'w')
#     # 搜索好友
#     pyautogui.hotkey('ctrl', 'f')
#     # 复制好友到粘贴板
#     pyperclip.copy(friend)
#     # 模拟复制粘贴
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(1)
#     # 回车进入
#     pyautogui.press('enter')
#     # 一条一条的发送信息
#     for msg in get_msg():
#         send(msg)
#         # 时间间隔
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     wb = load_workbook(r'D:\\名单.xlsx')
#     ws = wb.active
#     for row in ws.iter_rows(min_row=2, values_only=True):
#         send_msg(row[0])
#         pyautogui.hotkey('ctrl', 'alt', 'w')
#         time.sleep(1)


# 最简单的微信刷屏程序
import time
from pynput import mouse, keyboard
time.sleep(5)  # 预留5秒用于准备
m_mouse = mouse.Controller()
m_keyboard = keyboard.Controller()  # 创建鼠标及键盘
# 请确保鼠标在聊天框内
m_mouse.click(mouse.Button.left)  # 点击鼠标左键，这里可要可不要
for a in range(10000):  # 这里输入轰炸的次数
    m_keyboard.type('你妈死了，大傻逼！')  # 这里输入你要刷屏的字
    m_keyboard.press(keyboard.Key.enter)  # 按下enter发送
    m_keyboard.release(keyboard.Key.enter)  # 释放enter
    time.sleep(0.05)  # 这里调整频率(一次发送后的等待时间)
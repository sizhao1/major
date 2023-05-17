# 0.导包
from selenium import webdriver
import time

def pre_test(url,browser):
    if browser=='ff':
        # 1.实例化一个对应的浏览器类(打开浏览器)
        # ff浏览器 版本 过老 和 selenium3.14.0 兼容性问题很多
        dr = webdriver.Firefox()
        # 2.在浏览器对象中调用对应的方法(输入被访问网站的网址)
        dr.get(url)
    elif browser=='chrome':
        dr = webdriver.Chrome()
        dr.get(url)
        # 3.把窗口最大化
        dr.maximize_window()
    dr.implicitly_wait(10)
    return dr

def end_test(dr):
    # 5.关闭窗口
    dr.quit()
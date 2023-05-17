'''
八种元素定位:
利用标签的属性来定位:
id属性:  唯一性  优选的  find_element_by_id('id属性值')
name属性: 用于前端往后端传值时, 也相对比较唯一  find_element_by_name('name属性值')
class类属性:  使用find_element_by_class_name()只允许单个的类属性值.   find_element_by_class_name('class属性值')

利用标签名本身来定位:
find_element_by_tag_name('标签名')

利用超链接(a标签)的文本来定位:
find_element_by_link_text('全文本')
find_element_by_partial_link_text('部分文本')

find_element_by_XXX(id/name/class_name属性值): 返回单个查找到的标签

find_elemnts_by_XXX(id/name/class_name属性值):
返回查找到的标签的列表

元素操作方法:
send_keys(): 输入数据
click(): 点击按钮,标签
clear(): 清除输入框中的数据

'''
# 0.导包
from selenium import webdriver
import time

def open_browser():
    # 1.打开浏览器
    dr = webdriver.Chrome()
    # 2.输入对应的url地址
    url = 'http://127.0.0.1:85/index.php?m=user&c=public&a=login'
    dr.get(url)
    # 3.最大化窗口
    dr.maximize_window()
    # 4.设置隐式等待 10秒
    dr.implicitly_wait(10)
    return dr


def login(dr, usr, pwd):
    # 4.执行登录的步骤
    # 定位到用户名输入框   使用id查找标签,需要传入id属性值
    ele_li = dr.find_elements_by_tag_name('input')
    # 在用户名输入框输入用户名
    ele = ele_li[5]
    ele.send_keys(usr)

    # 输入密码   name="password"
    ele = ele_li[6]
    # ele = dr.find_element_by_name('password')
    ele.send_keys(pwd)

    # 点击登录  class="login_btn fl"
    ele = dr.find_element_by_class_name('login_btn')
    ele.click()
    # 线程休眠3秒
    time.sleep(3)

def end_test(dr):
    # 5.关闭窗口
    dr.close()
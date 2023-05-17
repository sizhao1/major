'''
webdriver中其它的属性和方法:
dr.title: 获取了窗口的标题信息.   对应html文档中head中的title标签
dr.current_url: 获取窗口的当前url地址.  对应地址栏中的url地址
窗口设置的方法:
maximize_window(): 让窗口最大化
set_window_size(): 设置窗口的大小(宽和高)
set_window_position(): 设置窗口的位置(窗口最左上的点离坐标原点的距离)
窗口进行刷新,前进后退的方法:
refresh(): 相等于手动点了一下F5
back():    相等于手动点了一下'<--'
forward(): 相等于手动点了一下'-->'
窗口的关闭和进程的退出:
close():  关闭的是一个窗口, 并不会真正的关闭进程
quit():   浏览器进程的退出,相等于执行 kill 进程的命令

webelement对应的一些其它的属性和方法:
size:  获取的是标签的宽和高
text:  获取的是文本信息(双标签之间的部分)
判断方法:
is_displayed(): 判断标签可不可见.  如果不可见(display:none;), 返回Fasle,可见返回True.
is_enabled(): 判断标签可不可用.  如果不可用(disabled=''),返回Fasle, 可用返回True.
其它方法:
get_attribute(): 获取标签的属性, 需要传入属性名, 返回对应的属性值.
'''
# 第二个作业
from selenium import webdriver
from day1.basic import *
import time

def test_other_method(dr):
    # 当前窗口的标题信息
    print(dr.title)
    # 当前窗口地址栏的url信息
    print(dr.current_url)

    # 对窗口进行设置
    # 窗口最大化
    # dr.maximize_window()
    # time.sleep(2)
    # # 窗口设置一定的宽和高
    # dr.set_window_size(500,500)
    # time.sleep(2)
    # # 窗口设置一定的位置
    # dr.set_window_position(300,0)
    # time.sleep(2)
    # dr.set_window_position(300, 300)
    # time.sleep(2)

    # 窗口的刷新,后退,前进
    # dr.refresh()
    # time.sleep(2)
    # dr.find_element_by_link_text('访问 新浪 网站').click()
    # time.sleep(2)
    # dr.back()
    # time.sleep(2)
    # dr.forward()
    # time.sleep(2)

    # 获取一个标签
    ele = dr.find_element_by_tag_name('button')
    # 打印标签的尺寸
    print(ele.size)
    # 打印标签的文本
    print(ele.text)
    # 打印标签的属性
    print(ele.get_attribute('title'))

    ele1 = dr.find_element_by_css_selector('#byA')
    ele2 = dr.find_element_by_css_selector('#cancelA')
    # 判断标签可不可见
    print('button标签可不可见:',ele.is_displayed())
    print('备用A输入框标签可不可见:', ele1.is_displayed())
    # 判断标签可不可用
    print('button标签可不可用:',ele.is_enabled())
    print('取消A标签可不可用:', ele2.is_enabled())

if __name__ == '__main__':
    url = "file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html"
    dr = pre_test(url,'chrome')
    test_other_method(dr)
    end_test(dr)
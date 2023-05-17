'''
iframe: html5仍然在使用,但是只支持原生的src属性.
作用: 在现有的html页面中,嵌入新的html页面,丰富网页的内容, 增强网页的功能.
典型使用场景:
1.提升用户的易用性.  (类似于QQ邮箱首页嵌入QQ登录和微信登录两个html页面)
2.提升性能. (类似于海盗的后台中iframe使用,动静分离.)

webdriver提供的方法:
dr.switch_to.frame(): 从Top Window--->iframe中, 需要传参, 传入iframe标签的name或id属性.
dr.switch_to.default_content(): 从iframe--->Top Window, 不需要传参, 因为Top Window只有一个, 而且是确定唯一的.
'''
from selenium import webdriver
import time
from day1.basic import *

# CSDN下载页面,进行登录

def test_csdn_login(dr):
    # 检查是否在Top Window中
    print(dr.find_element_by_css_selector('.hot-search').text)

    # 点击登录注册
    dr.find_element_by_css_selector('.upload-button>.btn').click()
    time.sleep(4)

    # 切换表单
    dr.switch_to.frame('passport_iframe')

    # 点击密码登录
    dr.find_element_by_xpath('//*[text()="密码登录"]').click()
    time.sleep(2)

    # 输入账号
    ele=dr.find_element_by_css_selector("[placeholder$='用户名']")
    ele.send_keys('yxp8210@eyou.com')
    time.sleep(2)

    # 输入密码
    ele=dr.find_element_by_css_selector('[placeholder="密码"]')
    ele.send_keys('Pass1234')
    time.sleep(2)

    # 点击登录
    ele=dr.find_element_by_css_selector('.base-button')
    ele.click()
    time.sleep(4)

def test_zcsl_login(dr):
    # 1.在 Top Window下,可以直接登录
    # 输入用户名,密码,电话号码,邮箱
    dr.find_element_by_css_selector('#user').send_keys('admin11')
    dr.find_element_by_css_selector('#password').send_keys('123456')
    dr.find_element_by_css_selector('#tel').send_keys(13324002300)
    dr.find_element_by_css_selector('#email').send_keys('13324002300@qq.com')
    dr.find_element_by_css_selector('button').click()
    time.sleep(2)

    # 切换到注册A.html这个iframe中
    dr.switch_to.frame('idframe1')
    # 点击一个超链接"我是a标签"
    dr.find_element_by_partial_link_text('a标签').click()
    time.sleep(1)

    # 切换到注册B.html这个iframe中
    dr.switch_to.default_content()
    dr.switch_to.frame('myframe2')
    # 点击一个超链接"我是b标签"
    dr.find_element_by_partial_link_text('b标签').click()
    time.sleep(1)

if __name__ == '__main__':
    url = 'file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
    dr = pre_test(url,'chrome')
    test_zcsl_login(dr)
    end_test(dr)

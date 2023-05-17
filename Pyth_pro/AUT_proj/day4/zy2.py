from selenium import webdriver
import time
from random import *

# 2.海盗的后台, 添加十个新会员
#点击会员管理
url = 'http://127.0.0.1:85/admin.php'
dr = webdriver.Chrome()
dr.get(url)
dr.maximize_window()
dr.implicitly_wait(10)

#输入用户名密码
ele = dr.find_element_by_css_selector('[placeholder="请输入用户名"]')
ele.send_keys('admin')
ele = dr.find_element_by_css_selector('[placeholder="请输入密码"]')
ele.send_keys('password')
ele = dr.find_element_by_css_selector('[placeholder="验证码"]')
ele.send_keys('1234')
#点击登录
dr.find_element_by_css_selector('.Btn').click()

# 点击 会员管理 菜单
dr.find_element_by_link_text('会员管理').click()

#点击添加会员
dr.find_element_by_css_selector('.n12.z_side').click()

#切换到添加会员
dr.switch_to.frame('mainFrame')

#添加会员信息
for i in range(10):
    #循环输入用户名,手机号,邮箱,qq
    username = 'lgn'+str(randint(100,9999999))
    phone = randint(13111111111, 13999999999)
    qq = randint(111111, 99999999999)
    lis = dr.find_elements_by_css_selector('.text_input')
    lis[0].send_keys(username)
    lis[1].send_keys(phone)
    lis[2].send_keys(str(phone)+'@qq.com')
    lis[3].send_keys(qq)
    dr.find_element_by_id('birthday').click()
    dr.find_element_by_css_selector('#laydate_y').click()
    dr.find_element_by_css_selector('#laydate_YY>label').click()
    ele = dr.find_element_by_css_selector('.laydate_tab.laydate_chtop')
    ele.click()
    ele.click()
    dr.find_element_by_xpath('//*[text()="1990年"]').click()
    dr.find_element_by_css_selector('#laydate_MM>label').click()
    dr.find_element_by_xpath('//*[text()="01月"]').click()
    dr.find_element_by_css_selector('#laydate_table tr:first-child>[d="1"]').click()
    dr.find_element_by_css_selector('.button_search').click()
    time.sleep(5)
    dr.find_element_by_xpath('//*[text()="添加"]').click()
dr.quit()
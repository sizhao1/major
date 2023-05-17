# 0.导包
from selenium import webdriver
import time

# 1.预置条件
dr = webdriver.Chrome()
url = 'file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html'
dr.get(url)
dr.maximize_window()

# 2.测试步骤
# 输入用户名
ele = dr.find_element_by_id('uA')
ele.send_keys('tong123')
time.sleep(1)
# 输入密码  第一个class="pwdA"
ele_list = dr.find_elements_by_class_name('pwdA')
ele = ele_list[0]
ele.clear()
ele.send_keys('123456')
time.sleep(1)
# 输入确认密码  第二个class="pwdA"
# ele = dr.find_elements_by_class_name('pwdA')
ele = ele_list[1]
ele.clear()
ele.send_keys('123456')
time.sleep(1)
# 输入邮箱
ele = dr.find_element_by_id('emailA')
ele.send_keys('tong123@qq.com')
time.sleep(1)
# 点击登录
ele = dr.find_element_by_id('btn')
ele.click()
time.sleep(1)

# 3.结束,关闭浏览器
dr.close()
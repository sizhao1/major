from selenium import webdriver
import time

url = 'file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html'
dr = webdriver.Chrome()
dr.get(url)
dr.maximize_window()

# 输入用户名
ele_li=dr.find_elements_by_tag_name('input')
ele=ele_li[0]
ele.send_keys('s123')
time.sleep(1)

# 输入密码
ele=ele_li[2]
ele.clear()
ele.send_keys('s123456')
time.sleep(1)

# 确认密码
ele=ele_li[3]
ele.clear()
ele.send_keys('s123456')
time.sleep(1)

# 输入邮箱
ele=ele_li[4]
ele.send_keys('s123@456.com')
time.sleep(1)

# 点击注册
ele=dr.find_element_by_tag_name('button')
ele.click()

dr.close()

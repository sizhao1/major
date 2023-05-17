from selenium import webdriver
import time

# 2.注册网易邮箱(注意业务流程)
# https://mail.163.com/register/index.htm?from=force/&cmd=register.entrance
# 预置条件
dr = webdriver.Chrome()
url='https://mail.163.com/register/index.htm?from=force/&cmd=register.entrance'
dr.get(url)
dr.maximize_window()

# 输入邮箱地址
ele=dr.find_element_by_id('username')
ele.send_keys('yyyxpppp')
time.sleep(1)

# 输入密码
ele=dr.find_element_by_id('password')
ele.send_keys('Pass1234')
time.sleep(1)

# 输入手机号
ele=dr.find_element_by_id('phone')
ele.send_keys('13195896030')
time.sleep(1)

# 勾选同意服务  触发鼠标失焦事件
li = dr.find_elements_by_tag_name('span')
ele = li[9]
ele.click()
time.sleep(2)

# 点击发送验证码
dr.find_element_by_id('phoneCodeButton').click()
time.sleep(1)
# 输入验证码
dr.find_element_by_id('phoneCode').send_keys(1234)

# 勾选同意服务
li = dr.find_elements_by_tag_name('span')
ele = li[9]
ele.click()

# # 点击注册
ele=dr.find_element_by_class_name('j-register')
ele.click()
dr.close()
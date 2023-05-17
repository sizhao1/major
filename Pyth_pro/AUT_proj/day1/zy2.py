# 0.导包
from selenium import webdriver
import time

# 1.实例化一个对应的浏览器类(打开浏览器)
dr = webdriver.Chrome()
# ff浏览器 版本 过老 和 selenium3.14.0 兼容性问题很多
# dr = webdriver.Firefox()
# 2.在浏览器对象中调用对应的方法(输入被访问网站的网址)
url = 'http://127.0.0.1:85/index.php?m=user&c=public&a=reg'
dr.get(url)
# 3.把窗口最大化
dr.maximize_window()

# 4.执行测试步骤
# 输入用户名  username
dr.find_element_by_name('username').send_keys('lgn10001')
# 输入密码  password
dr.find_element_by_name('password').send_keys('123456')
# 输入确认密码 userpassword2
dr.find_element_by_name('userpassword2').send_keys('123456')
# 输入手机号  mobile_phone
dr.find_element_by_name('mobile_phone').send_keys(13324882499)
# 输入邮箱  email
dr.find_element_by_name('email').send_keys('13324882499@qq.com')
# 点击注册按钮  class="reg_btn"
dr.find_element_by_class_name('reg_btn').click()
# 线程休眠3秒
time.sleep(3)

# 5.关闭窗口
dr.close()
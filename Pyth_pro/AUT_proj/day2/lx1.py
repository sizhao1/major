# 0.导包
from selenium import webdriver
import time

# 1.实例化一个对应的浏览器类(打开浏览器)
dr = webdriver.Chrome()

# 2.在浏览器对象中调用对应的方法(输入被访问网站的网址)
url = 'http://127.0.0.1:85'
dr.get(url)

# 3.把窗口最大化
dr.maximize_window()
# # 线程休眠3秒
# time.sleep(3)

# 4.执行测试步骤
# 前两个: 登录 注册
dr.find_element_by_link_text('登录').click()  #弹开一个新窗口, 登录页面
time.sleep(1)
dr.find_element_by_link_text('注册').click()  #弹开一个新窗口, 注册页面
time.sleep(1)
# 后两个: 会员中心  我的订单
dr.find_element_by_partial_link_text('会员').click()  #原来的页面刷新, 刷到登录页面
time.sleep(1)
dr.find_element_by_partial_link_text('订单').click()  #登录页面点的订单,刷回登录页面
time.sleep(1)
# 5.关闭窗口  关闭首页的窗口
# dr.close()    #只是用于单独一个窗口的关闭
dr.quit()       #这个方法用于进程的退出(关闭进程,释放资源)
# 0.导包
from selenium import webdriver
import time

# 1.实例化一个对应的浏览器类(打开浏览器)
dr = webdriver.Chrome()
# ff浏览器 版本 过老 和 selenium3.14.0 兼容性问题很多
# dr = webdriver.Firefox()
# 2.在浏览器对象中调用对应的方法(输入被访问网站的网址)
url = 'http://127.0.0.1:85'
dr.get(url)
# 3.把窗口最大化
dr.maximize_window()


# 4.执行测试步骤
# 输入搜索关键字
dr.find_element_by_name('keyword').send_keys('苹果')
# 点击搜索按钮
dr.find_element_by_class_name('btn1').click()
# 线程休眠3秒
time.sleep(3)

# 5.关闭窗口
dr.close()
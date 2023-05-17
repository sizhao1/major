# 0.导包
from selenium import webdriver
import time

# 1.实例化一个对应的浏览器类(打开浏览器)
dr = webdriver.Chrome()
# ff浏览器 版本 过老 和 selenium3.14.0 兼容性问题很多
# dr = webdriver.Firefox()
# 2.在浏览器对象中调用对应的方法(输入被访问网站的网址)
url = 'file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html'
dr.get(url)
# 3.把窗口最大化
dr.maximize_window()

# 4.执行测试步骤
# 链式写法
# dr.find_element_by_link_text('访问 新浪 网站').click()
dr.find_element_by_partial_link_text('访问 新浪').click()
# 线程休眠3秒
time.sleep(3)

# 5.关闭窗口
dr.close()
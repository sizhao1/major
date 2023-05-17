from selenium import webdriver
import time
# 3.百度贴吧, 左边分类打印
# 打印贴吧热议榜
url='https://tieba.baidu.com/index.html'
# 预置条件
dr=webdriver.Chrome()
dr.get(url)
dr.maximize_window()

# 左边分类打印
print(dr.find_element_by_css_selector('#left-cont-wraper>.u-f-t.ufw-gap').text)
print(dr.find_element_by_css_selector('#f-d-w').text)
# 打印贴吧热议榜
print(dr.find_element_by_css_selector('.topic_list_box').text)

# 关闭
dr.close()
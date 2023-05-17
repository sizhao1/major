from selenium import webdriver
import time

dr = webdriver.Chrome()
#预置条件
url = ('file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html')
dr.get(url)
# 最大化浏览器
dr.maximize_window()
# 隐式等待
dr.implicitly_wait(30)
#练习2: 注册A.html中, 去掉 取消A btn的disabled属性, 使得它可以点击, 点击它,处理弹框.
#删除
js = 'window.scrollTo(0,1000)'
dr.execute_script(js)
js="document.getElementById('cancelA').removeAttribute('disabled');document.getElementById('cancelA').setAttribute('style','background:blue;');"
dr.execute_script(js)
time.sleep(3)
#点击
dr.find_element_by_css_selector('#cancelA').click()
time.sleep(2)
#处理js
alert=dr.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
#推出
dr.quit()
time.sleep(2)
'''
元素定位的第七种方法:
css选择器:
--简单选择器:
----标签选择器:  直接用标签名
----id选择器:    #id值
----类选择器:    .class值  多个值的情况: .第一个类属性值.第二个类属性值
----属性选择器:  [属性名=属性值]  这个可以定位到除上面三种的情况

--复杂选择器:
----父子选择器: 父标签>子标签  关系仅限于父子关系
----后代选择器: 祖先标签 后代标签--空格  关系不限,只要是后代都行

延伸:
属性选择器的扩展:
1.属性值以什么开头
[属性名^=属性值开头的一段]
2.属性值以什么结尾
[属性名$=属性值结尾的一段]
3.属性值包含什么
[属性名*=属性值包含的一段]

补充:
序数写法: 第一个子标签: :first-child
第二个到第N个子标签: :nth-child(2)......:nth-child(n)
css选择器, 序数写法论关系(父子,祖先后代),论排行(同辈之间排行, 不论标签一样不一样)

使用的webdriver的方法:
find_element_by_css_selector('css选择器')
'''
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
ele = dr.find_element_by_css_selector('#uA')
ele.send_keys('tong123')
time.sleep(1)
# 输入密码  第一个class="pwdA"
ele_list = dr.find_elements_by_css_selector('.pwdA')
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
ele = dr.find_element_by_css_selector('#emailA')
ele.send_keys('tong123@qq.com')
time.sleep(1)
# 点击登录
ele = dr.find_element_by_css_selector('#btn')
ele.click()
time.sleep(1)

# 3.结束,关闭浏览器
dr.close()
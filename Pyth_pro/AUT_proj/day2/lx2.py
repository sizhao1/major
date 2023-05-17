'''
京东商品的详情页面:
信息打印
'''
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
url = 'https://item.jd.com/10043601916419.html'
dr.get(url)
dr.maximize_window()

# 2.测试步骤
# 京东详情中左上的信息打印一下
# 标题 部分
ele = dr.find_element_by_css_selector('.sku-name')
print(ele.text)
# 中间部分
print(dr.find_element_by_css_selector('.summary-price-wrap').text)
# 底下部分
print(dr.find_element_by_css_selector('.summary.p-choose-wrap').text)

# 3.结束,关闭浏览器
dr.close()
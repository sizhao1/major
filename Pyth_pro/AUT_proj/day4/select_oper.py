'''
下拉选框的处理:
html里面的结构:
select是外框, 使用select标签表示
option是里面的选项,用option标签表示
select和option是嵌套和从属的关系,不能分离.

webdriver提供的处理方法:
Select类来处理下拉选框(需要导包)
1.实例化类
se = Select()
2.调用方法
se.select_by_index():  通过索引来选择选项,从0开始,按照选项的位置来顺序往下选.
se.select_by_value():  通过option标签的value属性值来选
se.select_by_visible_text():  通过页面上可见的文本来选  优选  所见即所得
'''
from day1.basic import *
from selenium.webdriver.support.select import Select

def test_select(dr):
    # 定位第一个下拉选框
    ele = dr.find_element_by_css_selector('#selectA')
    # 利用工具导包: ctrl+alt+space(空格键) 导入和selenium有关的包.
    se =Select(ele)
    # 通过索引来选选项
    # se.select_by_index(2)
    # 通过value属性值来选
    # se.select_by_value('cq')
    # 通过页面可见的文本来选
    se.select_by_visible_text('A重庆')
    time.sleep(6)

if __name__ == '__main__':
    url = "file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html"
    dr=pre_test(url,'chrome')
    test_select(dr)
    end_test(dr)
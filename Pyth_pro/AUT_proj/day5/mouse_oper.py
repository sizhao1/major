'''
鼠标事件:
除了在元素操作中,单击,输入数据,擦除数据这几个,我们其它的鼠标事件我们暂时是没法处理.

webdriver中处理鼠标事件:
ActionChains类:  专门处理鼠标事件
1.实例化类  act = ActionChains()
2.调用方法
double_click(): 模拟的是鼠标的双击事件
move_to_element(): 模拟的是鼠标的悬浮事件
drag_and_drop():  模拟的是鼠标的拖拽事件
context_click():  模拟的是鼠标的右键事件  bug+autoit(自动化工具)
3.执行方法
perform():  控制鼠标的执行方法的真正执行
'''
from selenium.webdriver import ActionChains
from day1.basic import *

def test_clear_cart_box(dr):
    # 完成登录
    dr.find_element_by_link_text('会员中心').click()
    dr.find_element_by_css_selector('#username').send_keys('lgn1')
    dr.find_element_by_css_selector('#password').send_keys('123456')
    dr.find_element_by_css_selector('.login_btn').click()
    time.sleep(3)
    # 悬浮购物车
    ele = dr.find_element_by_css_selector('#cart_box>dt')
    act = ActionChains(dr)
    act.move_to_element(ele).perform()
    time.sleep(4)
    # 清空购物车
    dr.find_element_by_xpath('//*[text()="清空购物车"]').click()

def test_drag_and_drop(dr):
    sr = dr.find_element_by_css_selector('#div1')
    tg = dr.find_element_by_css_selector('#div2')
    act = ActionChains(dr)
    act.drag_and_drop_by_offset(
        sr,500,500).perform()
    time.sleep(3)

def test_category(dr,category):
    ele = dr.find_element_by_css_selector('.listli_01-p')
    ActionChains(dr).move_to_element(ele).perform()
    dr.find_element_by_xpath(f'//*[text()="{category}"]').click()
    time.sleep(3)
    print(dr.title)
    print(dr.find_element_by_css_selector('.MilknavBox').text)

if __name__ == '__main__':
    url  = "http://127.0.0.1:85/"
    # url = 'file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/drop.html'
    dr = pre_test(url,'chrome')
    # # test_clear_cart_box(dr)
    # test_drag_and_drop(dr)
    test_category(dr,'手机')
    end_test(dr)


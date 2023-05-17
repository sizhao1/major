'''
键盘事件:
ctrl+a,ctrl+c,ctrl+v,ctrl+x, enter, tab, 键盘上下键, 等等这些都是典型的键盘事件

webdriver提供的方法:
Keys类: 记录了各种键盘的键
使用方法:
由于Keys类中都是常量属性, Keys就会处理成静态类的用法.
类名.属性
例: 调用Ctrl键:
Keys.CONTROL

键盘事件一般用在send_keys()方法中,作为参数去使用.
例: 发送Ctrl+a键盘事件:
send_keys(Keys.CONTROL,'a')
'''
from selenium.webdriver.common.keys import Keys
from day1.basic import *

def test_keys_oper(dr):
    ele = dr.find_element_by_css_selector('.input_ss')
    ele.send_keys('苹果')
    ele.send_keys(Keys.CONTROL,'a')
    ele.send_keys(Keys.CONTROL, 'x')
    ele.send_keys(Keys.CONTROL, 'v')
    ele.send_keys(Keys.CONTROL, 'v')
    time.sleep(3)
    dr.find_element_by_css_selector('.btn1').click()
    time.sleep(2)

def test_keys_oper2(dr,phone):
    # 用户名处输入手机号
    lis = dr.find_elements_by_css_selector('.input_100')
    ele = lis[0]
    ele.send_keys(phone)
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(Keys.CONTROL, 'c')
    # 密码和确认密码使用复制的手机号
    lis[1].send_keys(Keys.CONTROL, 'v')
    lis[2].send_keys(Keys.CONTROL, 'v')
    lis[3].send_keys(Keys.CONTROL, 'v')
    ele = lis[4]
    ele.send_keys(Keys.CONTROL, 'v')
    ele.send_keys('@qq.com')
    dr.find_element_by_css_selector('.reg_btn').click()
    time.sleep(3)

if __name__ == '__main__':
    # url = 'http://127.0.0.1:85/index.php'
    url = 'http://127.0.0.1:85/index.php?m=user&c=public&a=reg'
    dr = pre_test(url,'chrome')
    # test_keys_oper(dr)
    test_keys_oper2(dr,13324782478)
    end_test(dr)
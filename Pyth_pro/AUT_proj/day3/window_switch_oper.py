'''
窗口切换:
浏览器会打开很多窗口,每个窗口会有一个唯一标识, 叫handle(相当于窗口id)
webdriver提供了获取窗口的handle值的两个属性:
dr.current_window_handle:  提供的是当前的窗口句柄(默认在get(url)打开的那个窗口上)
dr.window_handles:         提供的就是所有的窗口句柄(列表的方式返回)
webdriver提供的窗口切换的方法:
dr.switch_to.window():   需要传参,传入要切换到的窗口的句柄

'''
from day1.basic import *

def test_open_new_window(dr,title):
    print('之前:',dr.window_handles)
    print(dr.title)
    dr.find_element_by_link_text('登录').click()
    dr.find_element_by_link_text('注册').click()
    dr.find_element_by_xpath('//*[text()="有商品上架咯..."]').click()
    dr.find_element_by_xpath('//*[text()="欢饮来到汇智动力..."]').click()
    li = dr.window_handles
    for item in li:
        dr.switch_to.window(item)
        if title in dr.title:
            break
    print('之后:',dr.window_handles)
    print(dr.title)


if __name__ == '__main__':
    url="http://127.0.0.1:85"
    dr = pre_test(url)
    test_open_new_window(dr,'用户注册')
    end_test(dr)
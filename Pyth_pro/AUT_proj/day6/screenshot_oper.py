'''
屏幕截图:
用于出错时,帮助做定位分析问题

webdriver提供的方法:
get_screenshot_as_file():  需要传参, 传入截图文件要保存到的目录. 必须是png图片文件.

其它方法:
get_screenshot_as_png():   返回的是保存的二进制数据. 没法看也没法用.
get_screenshot_as_base64():  返回的是base64编码的字符串,没法直接用,只能用在html网页文件中当做image文件源来使用.

补充:
时间格式化的格式化码:
    %Y  十进制的世纪年.
    %m  十进制的月份表示, [01,12].
    %d  十进制的月份下的日期表示, [01,31].
    %H  十进制表示的24小时制的小时表示, [00,23].
    %M  十进制的分钟表示, [00,59].
    %S  十进制的秒表示, [00,61].
'''
from day1.basic import *

def test_login(dr,usr,pwd):
    dr.find_element_by_css_selector('#username').send_keys(usr)
    dr.find_element_by_css_selector('#password').send_keys(pwd)
    dr.find_element_by_css_selector('.login_btn').click()
    raise Exception('强制出错!')
    dr.find_element_by_xpath('//*[text()="正在进行中的交易"]')

if __name__ == '__main__':
    try:
        url = "http://127.0.0.1:85/index.php?m=user&c=public&a=login"
        dr = pre_test(url,'chrome')
        test_login(dr,'lgn1','123456')
    except Exception as e:
        print(e)
        print('登录出问题了...')
        time_str = time.strftime('%Y-%m-%d_%H-%M-%S')
        dr.get_screenshot_as_file(f'./screenshot/{time_str}.png')
    finally:
        end_test(dr)
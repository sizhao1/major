'''
JS弹框和非JS弹框的区分:
使用鼠标拾取器点击弹框中的内容,如果能选中就不是js弹框,而只是利用html的标签弹出内容.
如果拾取不了,那就多半是js弹框.

JS弹框的切换:
webdriver提供的方法:
alert = dr.switch_to.alert: 切换到js弹框的这个图层,这个图层和底下的html的图层是独立的两个图层.  两个图层多半做的效果都是蒙态的效果. js弹框起作用的话,底下的html图层就是蒙起来的,不能起作用.
获取文字:      alert.text
点击确认按钮:  alert.accept()
点击取消按钮:  alert.dismiss()
输入文字:      alert.send_keys()
'''
from day1.basic import *
import time
def test_switch_frame(dr,sw_id):
    dr.switch_to.frame(sw_id)
    time.sleep(2)


def test_alert(dr,element,behavior,send_info=None):
    # 点击'alerta'这个按钮,触发js弹框
    dr.find_element_by_css_selector(element).click()
    # 获取到js弹框对象
    al = dr.switch_to.alert
    # 打印警告内容
    print(al.text)
    time.sleep(1)
    # # 输入一段文字
    if send_info:
        al.send_keys(send_info)
        time.sleep(3)
    if behavior=='accept':
        # 点击确认按钮
        al.accept()
    else:
        # 点击取消按钮
        al.dismiss()
    time.sleep(3)


if __name__ == '__main__':
    url="file:///D:/a01-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E4%B8%8A%E8%AF%BE%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/python+selenium/%E4%B8%BB%E8%A6%81%E8%AF%BE%E4%BB%B6/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
    dr = pre_test(url,'chrome')
    test_switch_frame(dr,'myframe2')
    test_alert(dr,'#alertB','accept')
    # test_alert(dr,'#alerta','accept','OK!Bye!')
    end_test(dr)
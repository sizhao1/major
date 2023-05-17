'''
滚动条的处理:
懒加载处理的首页,web网页,需要把滚动条拉到底部.

webdriver的代码本身不能操作处理滚动条, 利用js代码来完成这个工作.
webdriver支持js脚本的执行:
execute_script(): 仅支持js脚本的执行,不支持其它语言.  需要传参, 参数是处理成字符串的js脚本.

js脚本:
#给id为nice的元素 增加 title属性并赋值为“测试title”
js='document.getElementById("nice").setAttribute("title","测试title")'
#给id为nice的元素 删除 title属性
js='document.getElementById("nice").removeAttribute("title")'
#获取id为nice的元素 title属性的值
js='document.getElementById("nice").getAttribute("title")'
#修改id为nice的元素 title属性的值
js='document.getELementById("nice").title="测试"'
'''
from day1.basic import *
from day1.login import *

def test_js_script1(dr):
    dr.execute_script('window.scrollTo(0,1000)')
    time.sleep(3)
def test_js_script2(dr):
    # 先做登录
    login(dr,'lgn1',123456)
    # 定位到日期输入框 #date,修改日期输入框为可写
    js = "document.getElementById('date').removeAttribute('readonly')"
    dr.execute_script(js)
    time.sleep(2)
    ele = dr.find_element_by_css_selector('#date')
    ele.clear()
    ele.send_keys('2000-01-01')
    time.sleep(2)

if __name__ == '__main__':
    # url = 'http://127.0.0.1:85/'
    url = 'http://127.0.0.1:85/index.php?m=user&c=user&a=userinfo'
    dr = pre_test(url,'chrome')
    test_js_script2(dr)
    end_test(dr)
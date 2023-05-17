'''
cookie:
用于用户身份识别鉴权, 保存一份服务器返回的session文件的一个凭证.

利用cookie欺骗的原理:
A客户端先登录上, 服务器返回对应的sessionid(session文件的凭证,可以证明A客户端已经登录上了).
sessionid给B客户端, B客户端在访问服务器时, 拿着这个sessionid去和服务器交互, 让服务器误以为客户端B就是客户端A, 把B当成是已经登录了的客户端, B可以绕过登录去和服务器交互.

webdriver提供的方法:
get_cookie():  获取本客户端的一项cookie信息, 需要传参, 传入单项cookie中name键的值.
get_cookies(): 获取本客户端的所有cookie信息, 不需要传参
add_cookie():  往请求头中添加cookie信息.  需要传参, 传入cookie的键值对信息
cookie键值对的写法: {"name":"phpsessid","value":"XXXXXXXXXXXXXXXX"}

服务器:
多点登录: 默认多个客户端可以用同个账号同时访问服务器.
单点登录: 只允许一个客户端使用一个账号访问服务器. 单独开发, 安全性更高.

session文件绕过登录失效:
1.客户端用户主动登出后, 它的登录信息在session文件中销毁
2.session文件有一定的有效时间,在服务器设置(去问开发), 如果超过有效时间,session文件绕过登录也会失败.
'''
# cookie欺骗, 绕过登录
# from selenium import webdriver
# import time
#
# url = 'http://127.0.0.1:85/admin.php'
# # 1.打开浏览器
# dr = webdriver.Chrome()
# # 2.访问后台首页
# dr.get(url)
# # 3.把窗口最大化
# dr.maximize_window()
# # 4.设置隐式等待
# dr.implicitly_wait(10)
#
# # 5.设置cookie信息
# dic1 = {'name':'PHPSESSID','value':'vohkl15ei6hrc78rjmvehg9794'}
# dic2 = {'name':'user_key','value':'3654yFeblNSamTJQhcJXsXSIrrH%2FHC3QJZe%2FZCk2'}
# dr.add_cookie(dic1)
# dr.add_cookie(dic2)
#
# # 6.发出请求
# dr.refresh()
# time.sleep(5)
#
# # 7.关闭浏览器
# dr.quit()

# 前台登录,可以获取到登录后的cookie信息
# 0.导包
# from selenium import webdriver
# import time
#
# # 1.打开浏览器
# dr = webdriver.Chrome()
# # 2.输入对应的url地址
# url = 'http://127.0.0.1:85/index.php?m=user&c=public&a=login'
# dr.get(url)
# # 3.最大化窗口
# dr.maximize_window()
#
# # 打印一下cookie信息
# print('登录前:',dr.get_cookies())
#
# # 4.执行登录的步骤
# # 定位到用户名输入框   使用id查找标签,需要传入id属性值
# ele_li = dr.find_elements_by_tag_name('input')
# # 在用户名输入框输入用户名
# ele = ele_li[5]
# ele.send_keys('lgn1')
#
# # 输入密码   name="password"
# ele = ele_li[6]
# # ele = dr.find_element_by_name('password')
# ele.send_keys('123456')
#
# # 点击登录  class="login_btn fl"
# ele = dr.find_element_by_class_name('login_btn')
# ele.click()
# # 线程休眠3秒
# time.sleep(3)
#
# # 查看本客户端的cookie信息
# print(dr.get_cookie('PHPSESSID'))
# print(dr.get_cookie('user_key'))
#
# # 5.关闭窗口
# dr.close()

# 前台绕过登录
from selenium import webdriver
import time

# 1.打开浏览器
dr = webdriver.Chrome()
# 2.输入对应的url地址
url = 'http://127.0.0.1:85/index.php'
dr.get(url)
# 3.最大化窗口
dr.maximize_window()
# 4.设置显示等待
dr.implicitly_wait(10)

# 添加cookie信息
dic1={'name':'PHPSESSID','value':'upjtijgqt8ltkjo10s2daa6bl4'}
dic2={'name':'user_key','value':'bd83lQuSA3QU3mpirRAyYy7JasXeO%2BlT7bnlQANU6A'}
dr.add_cookie(dic1)
dr.add_cookie(dic2)
# 发出请求
dr.refresh()
time.sleep(5)


# 退出浏览器
dr.quit()
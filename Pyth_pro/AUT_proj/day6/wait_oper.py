'''
等待:
1.强制等待:
time.sleep(): 需要传参, 传入等待时长, 单位为秒. 线程的强制等待.
2.隐式等待:
implicitly_wait(): 需要传参, 传入等待时长, 单位为秒.
当元素第一次定位不到的时候,就会触发隐式等待(全局元素), 就会等待相应的时长, 完了后再做一次元素定位, 如果能定位到, 代码就往下走, 定位不到, 抛错进入异常环节.
建议放在初始化环境的时候,跟在窗口最大化后,设置上.
3.显示等待:
智能等待, 设置等待时长(在等待时长之内, 设置一定的探测时间, 每隔一段时间探测一次,等待条件有没有达到, 等待条件达到后, 退出等待, 没有达到, 继续等), 设置等待条件.
设置等待时长: WebDriverWait类
设置等待条件: expected_conditions模块
定位标签的类: By类
1.实例化等待类
wait = WebDriverWait(): dr,等待时长, 探测时长默认为0.5秒.
2.调用方法
wait.until(等待条件)
wait.until(expected_conditions模块.等待条件方法())
3.定位元素
locator = (By.方式, '定位值')
例: locator = (By.ID, 'id值')

元素定位最终的定位:
locator = (By.ID, 'id值')
ele = WebDriverWait(dr,10).until(EC.presence_of_element_located(locator))
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

# # 例子一:
# # 初始化环境
# url = "http://127.0.0.1:85/index.php?m=user&c=public&a=login"
# dr = webdriver.Chrome()
# dr.get(url)
# dr.maximize_window()
# dr.implicitly_wait(10)
#
# # 进行登录
# # 定位到用户名输入框   使用id查找标签,需要传入id属性值
# ele_li = dr.find_elements_by_tag_name('input')
# # 在用户名输入框输入用户名
# ele = ele_li[5]
# ele.send_keys('lgn1')
#
# # 输入密码   name="password"
# ele = ele_li[6]
# # ele = dr.find_element_by_name('password')
# ele.send_keys(123456)
#
# # 点击登录  class="login_btn fl"
# ele = dr.find_element_by_class_name('login_btn')
# ele.click()
#
# # 使用显示等待, 等待页面跳转,  10秒, 条件: dr.title 用户登录--->我的会员中心
# wait = WebDriverWait(dr,10,poll_frequency=0.5)
# # wait.until(EC.title_contains('我的会员中心'))
# # wait.until(EC.url_to_be('http://127.0.0.1:85/index.php?m=user&c=index&a=index'))
# wait.until(EC.url_changes('http://127.0.0.1:85/index.php?m=user&c=index&a=index'))
#
# # 验证 页面是否出现 您好 lgn1 这个文本
# assert dr.find_element_by_xpath('//*[text()="您好 lgn1"]')
#
# # 结束,清理环境
# dr.quit()

# # 例子二:
# # 初始化环境
# url = "http://127.0.0.1:85/index.php?m=user&c=address&a=address"
# dr = webdriver.Chrome()
# dr.get(url)
# dr.maximize_window()
# dr.implicitly_wait(10)
#
# # 进行登录
# # 定位到用户名输入框   使用id查找标签,需要传入id属性值
# ele_li = dr.find_elements_by_tag_name('input')
# # 在用户名输入框输入用户名
# ele = ele_li[5]
# ele.send_keys('lgn1')
#
# # 输入密码   name="password"
# ele = ele_li[6]
# # ele = dr.find_element_by_name('password')
# ele.send_keys(123456)
#
# # 点击登录  class="login_btn fl"
# ele = dr.find_element_by_class_name('login_btn')
# ele.click()
#
# # 对收货地址进行删除
# dr.find_element_by_xpath('//*[text()="删除"]').click()
# al = dr.switch_to.alert
# print(al.text)
# al.accept()
# # 显示等待:  等待条件: 警告框的弹出
# wait = WebDriverWait(dr,10)
# wait.until(EC.alert_is_present())
#
# al = dr.switch_to.alert
# print(al.text)
# al.accept()

# time.sleep(3)
# dr.quit()

# # 例子三:
# # 初始化环境
# url = "http://127.0.0.1:85/index.php?m=user&c=public&a=login"
# dr = webdriver.Chrome()
# dr.get(url)
# dr.maximize_window()
# dr.implicitly_wait(10)
#
# # 进行登录
# # 定位到用户名输入框   使用id查找标签,需要传入id属性值
# ele_li = dr.find_elements_by_tag_name('input')
# # 在用户名输入框输入用户名
# ele = ele_li[5]
# ele.send_keys('lgn1')
#
# # 输入密码   name="password"
# ele = ele_li[6]
# # ele = dr.find_element_by_name('password')
# ele.send_keys(123456)
#
# # 点击登录  class="login_btn fl"
# ele = dr.find_element_by_class_name('login_btn')
# ele.click()
#
# # 刷新url,访问订单页面
# dr.get('http://127.0.0.1:85/index.php?m=goods&c=order&a=index')
# dr.find_element_by_xpath('//*[text()="添加新地址"]').click()
#
# # 省下拉框, 选择
# ele = dr.find_element_by_css_selector('#add-new-area-select')
# se = Select(ele)
# se.select_by_visible_text('陕西省')
#
# # 显示等待等待 市下拉框动态出现,  等待条件 市下拉框出现
# # 定位标签:  presence_of_element_located()
# # locator:  (by方式,定位值)  通过元祖传入
# wait = WebDriverWait(dr,10)
# locator = (By.CSS_SELECTOR,'.add-new-area>select:nth-child(3)')
# ele = wait.until(EC.presence_of_element_located(locator))
# se = Select(ele)
# se.select_by_visible_text('西安市')
#
# # 显示等待来对区元素进行定位
# wait = WebDriverWait(dr,10)
# locator = (By.CSS_SELECTOR,'.add-new-area>select:nth-child(4)')
# ele = wait.until(EC.presence_of_element_located(locator))
# se = Select(ele)
# se.select_by_visible_text('碑林区')
# time.sleep(5)
#
# dr.quit()
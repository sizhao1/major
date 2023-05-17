# 3.海盗电商后台,绕过登录,会员信息处查询一个并未创建过的会员信息,打印显示共查到多少条记录.
from selenium import webdriver
import time

# 设置初始化条件
url = "http://localhost:85/admin.php"
dr = webdriver.Chrome()
dr.maximize_window()
dr.get(url)
dr.implicitly_wait(10)

# 设置cookie绕过登录
dic = {'name':'PHPSESSID',"value":"fhb6i5ithlt1qd5cll8v94r2c0"}
dr.add_cookie(dic)

dr.refresh()
time.sleep(3)

# 点击会员管理
dr.find_element_by_xpath('//*[text()="会员管理"]').click()
time.sleep(2)

# 切换表单
dr.switch_to.frame('mainFrame')
# 进行搜索
dr.find_element_by_css_selector('.textbox-text.textbox-prompt').send_keys('lgn1002')
dr.find_element_by_css_selector('.l-btn-text').click()
time.sleep(3)
# 验证搜索的结果
assert '共0条记录' in dr.find_element_by_css_selector('.pagination-info').text
# 退出浏览器
dr.quit()

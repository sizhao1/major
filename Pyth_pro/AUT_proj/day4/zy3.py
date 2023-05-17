from selenium import webdriver
import time

# 3.海盗的前台, 修改会员的个人信息
url = 'http://127.0.0.1:85/'
dr = webdriver.Chrome()
dr.get(url)
dr.maximize_window()

# 单击登陆
dr.find_element_by_link_text('登录').click()
# 窗口切换
dr.switch_to.window(dr.window_handles[-1])
# 登录页面
dr.find_element_by_xpath('//*[@id="username"]').send_keys('lgn1')
dr.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
dr.find_element_by_xpath('//*[@class="login_btn fl"]').click()
time.sleep(3)
# 单击账号设置
dr.find_element_by_xpath('//*[text()="账号设置"]').click()
dr.find_element_by_xpath('//*[@class="chaozuo"]//li[2]/a').click()
# 修改信息
ele = dr.find_element_by_xpath('//*[@id="true_name"]')
ele.clear()
ele.send_keys('张三张三')
dr.find_element_by_xpath('//*[@id="xb" and @value="2"]').click()
dr.find_element_by_xpath('//*[@id="date"]').click()
# 单击今天
ele_today = dr.find_element_by_xpath('//*[@class="laydate_btn"]/a[2]').click()
# 再次单击输入框
dr.find_element_by_xpath('//*[@id="date"]').click()
# 选择年
dr.find_element_by_xpath('//*[@id="laydate_YY"]/label').click()
dr.find_element_by_xpath('//*[@class="laydate_tab laydate_chtop"]').click()
dr.find_element_by_xpath('//*[@class="laydate_tab laydate_chtop"]').click()
dr.find_element_by_xpath('//*[@id="laydate_ys"]/li[4]').click()
# 选择日
dr.find_element_by_xpath('//*[@id="laydate_MM"]//label').click()
dr.find_element_by_xpath('//*[@id="laydate_ms"]/span[1]').click()
dr.find_element_by_xpath('//*[@y="1990" and @m="1" and@ d="1"]').click()
# 修改QQ
ele = dr.find_element_by_xpath('//*[@id="qq"]')
ele.clear()
ele.send_keys('13290809080')
# 确定修改
dr.find_element_by_xpath('//*[@class="btn4"]').click()

# 处理弹框
time.sleep(1)
alert = dr.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()

time.sleep(2)
# 关闭浏览器
dr.quit()
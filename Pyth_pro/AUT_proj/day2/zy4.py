from selenium import webdriver
import time
# 4.登录QQ邮箱
# 预置条件
dr = webdriver.Chrome()
url='https://mail.qq.com/'
dr.get(url)
dr.maximize_window()
time.sleep(2)

# 检查是否在Top Window中
print(dr.find_element_by_css_selector('.header_logo').text)
print(dr.find_element_by_css_selector('.header_link').text)
print(dr.find_element_by_css_selector('.login_pictures_txt').text)
# 切换表单
dr.switch_to.frame('login_frame')

# 点击账号密码登录
dr.find_element_by_css_selector('#switcher_plogin').click()

# 输入账号
ele=dr.find_element_by_css_selector("#u")
ele.send_keys('2484055549@qq.com')
time.sleep(2)

# 输入密码
ele=dr.find_element_by_css_selector('#p')
ele.send_keys('SJL18792532939')
time.sleep(2)

# 点击登录
ele=dr.find_element_by_css_selector('#login_button')
ele.click()
time.sleep(2)

# 关闭浏览器
dr.quit()
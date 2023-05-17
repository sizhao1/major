# 1.海盗前台, 会员中心页面,给用户连续添加十个收货地址, 然后删除前两个.
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# 设置预置条件
dr=webdriver.Chrome()
dr.get("http://localhost:85/")
dr.maximize_window()
time.sleep(2)
dr.implicitly_wait(10)

# 登录
dr.find_element_by_xpath('//*[text()="会员中心"]').click()
time.sleep(2)
dr.find_element_by_css_selector("#username").send_keys("lgn1")
dr.find_element_by_css_selector("#password").send_keys("123456")
dr.find_element_by_css_selector(".login_btn.fl").click()
time.sleep(3)

# 会员中心处,点击账号设置
dr.find_element_by_xpath('//*[text()="账号设置"]').click()
dr.find_element_by_css_selector(".ico_nav8").click()
dr.find_element_by_xpath('//*[text()="收货地址"]').click()
# 添加10个收货地址
for i in range(10):
    dr.find_element_by_css_selector("#username").send_keys(f"user{i}")
    ele=dr.find_element_by_css_selector("#province")
    se=Select(ele)
    se.select_by_visible_text("陕西省")
    time.sleep(1)
    ele = dr.find_element_by_css_selector("#city")
    se = Select(ele)
    se.select_by_visible_text("西安市")
    time.sleep(1)
    ele = dr.find_element_by_css_selector("#district")
    se = Select(ele)
    se.select_by_visible_text("未央区")
    time.sleep(1)
    dr.find_element_by_css_selector("#address").send_keys(f"大明宫街道汇林华城A区{i+1}号楼")
    dr.find_element_by_css_selector("#zip").send_keys("710000")
    dr.find_element_by_css_selector("#mobile").send_keys(f"1871111222{i}")
    dr.find_element_by_css_selector(".btn3").click()
    time.sleep(2)
    alert=dr.switch_to.alert
    alert.accept()
    time.sleep(2)
# 删除前两个收货地址
for j in range(2):
    dr.find_element_by_xpath('//*[@class="ditable"]//tr[2]//a[3]').click()
    time.sleep(2)
    alert = dr.switch_to.alert
    print(alert.text)
    alert.accept()
    WebDriverWait(dr,10).until(EC.alert_is_present())
    alert = dr.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(2)
# 关闭
dr.quit()

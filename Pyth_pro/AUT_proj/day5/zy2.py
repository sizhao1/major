# 2.海盗前台,订单页面,给用户添加一个收货地址.  商品数量为2, 要求用鼠标或键盘事件实现.
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

# 设置预置条件
dr=webdriver.Chrome()
dr.get("http://localhost:85/")
dr.maximize_window()
time.sleep(2)

# 搜索
dr.find_element_by_css_selector('[name="keyword"]').send_keys("苹果 (Apple)")
dr.find_element_by_css_selector(".btn1").click()
dr.find_element_by_css_selector(".p1>a").click()
dr.switch_to.window(dr.window_handles[-1])
time.sleep(2)
# 加入购物车
dr.find_element_by_css_selector('[data-value="粉色"]').click()
dr.find_element_by_css_selector('[data-value="512G"]').click()
dr.find_element_by_css_selector('[data-value="套餐一"]').click()
ele=dr.find_element_by_css_selector(".goods-number")
ele.send_keys(Keys.CONTROL,"a")
ele.send_keys(2)
dr.find_element_by_css_selector("#joinCarButton").click()
time.sleep(2)
dr.find_element_by_css_selector(".shopCar_T_span3").click()
time.sleep(2)
dr.find_element_by_css_selector('.shopCar_btn_03.fl').click()
time.sleep(2)
# 登录
dr.find_element_by_css_selector("#username").send_keys("lgn1")
dr.find_element_by_css_selector("#password").send_keys("123456")
dr.find_element_by_css_selector(".login_btn.fl").click()
time.sleep(3)
# 添加收货地址
dr.find_element_by_css_selector(".add-address").click()
dr.find_element_by_css_selector('[name="address[address_name]"]').send_keys("张三")
dr.find_element_by_css_selector('[name="address[mobile]"]').send_keys("18711119999")
ele=dr.find_element_by_css_selector("#add-new-area-select")
se=Select(ele)
se.select_by_visible_text("陕西省")
time.sleep(1)
locator = (By.CSS_SELECTOR,'.add-new-area>select:nth-child(3)')
ele = WebDriverWait(dr,10).until(EC.presence_of_element_located(locator))
se = Select(ele)
se.select_by_visible_text("西安市")
time.sleep(1)
ele = dr.find_element_by_css_selector(".add-new-area>select:nth-child(4)")
se = Select(ele)
se.select_by_visible_text("未央区")
time.sleep(1)
dr.find_element_by_css_selector(".add-new-name-span-2").send_keys("大明宫街道汇林华城A区11号楼")
dr.find_element_by_css_selector(".add-new-name-span-3").send_keys("710000")
time.sleep(2)
dr.find_element_by_css_selector(".aui_state_highlight").click()
time.sleep(3)
# 关闭
dr.quit()
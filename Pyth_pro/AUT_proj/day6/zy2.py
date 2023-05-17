from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# # 2.12306网页, 利用js脚本从车票tab页切换成常用查询tab页,来完成一次查询 车站:上海, 车次:Z163

# 预置条件
url='https://www.12306.cn/index/'
dr=webdriver.Chrome()
dr.get(url)
dr.maximize_window()
dr.implicitly_wait(10)

# 修改display
js='var main_item = document.getElementsByClassName("search-main-item");main_item[0].style="display:none";main_item[1].style="display:block";'
dr.execute_script(js)
time.sleep(3)
# 车站
ele = dr.find_element_by_id('stationValueText')
ele.click()
locator1=(By.XPATH,'//*[text()="上海"]')
ele1=WebDriverWait(dr,10).until(EC.visibility_of_element_located(locator1))
ele1.click()
# 车次
ele = dr.find_element_by_id('numberValue')
ele.click()
dr.find_element_by_xpath('//*[text()="Z163"]').click()
# 查询按钮
dr.find_element_by_id('bie_button').click()
# 切换窗口
dr.switch_to.window(dr.window_handles[-1])
time.sleep(3)

# 检查一下结果
assert 'Z163' in dr.find_element_by_css_selector('#content_defaultwarningAlert_hearder').text
# 关闭
dr.quit()
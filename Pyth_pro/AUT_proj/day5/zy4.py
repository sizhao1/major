# 4.海盗电商前台,绕过登录,给会员修改一下默认地址. 最上面的一条是默认地址.
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 设置初始化条件
url = "http://127.0.0.1:85/index.php?m=user&c=address&a=address"
dr = webdriver.Chrome()
dr.maximize_window()
dr.get(url)
dr.implicitly_wait(10)

# 设置cookie绕过登录
time.sleep(3)
dic1 = {'name':'PHPSESSID',"value":"umlc89mm2h5qfh5dq9hqj973q4"}
dr.add_cookie(dic1)
dic2 = {'name':'user_key',"value":"b74996s8BujP%2Fdyth8WrI8hCbbI2aQfdNejgjM9HRQ"}
dr.add_cookie(dic2)

dr.get(url)
time.sleep(3)

# 修改默认地址为最上面一个
dr.find_element_by_link_text('设为默认').click()
time.sleep(3)

# 处理第一层弹框
alert = dr.switch_to.alert
print(alert.text)
alert.accept()

# 显示等待来处理第二层弹框
WebDriverWait(dr,10).until(EC.alert_is_present())
alert = dr.switch_to.alert
print(alert.text)
alert.accept()

# 校验是否最上面为默认
assert "默认地址" in dr.find_element_by_css_selector('.ditable>tbody>tr:nth-child(2) td:nth-child(5)').text

dr.quit()
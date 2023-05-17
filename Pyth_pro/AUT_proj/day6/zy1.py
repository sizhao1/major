from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 1.利用显示完成海盗电商的注册(要求:所有元素定位都用显示等待完成)
# 预置条件
url='http://127.0.0.1:85/index.php?m=user&c=public&a=reg'
dr=webdriver.Chrome()
dr.get(url)
dr.maximize_window()
dr.implicitly_wait(10)

# 用户名
locator1=(By.CSS_SELECTOR,'[name="username"]')
ele1=WebDriverWait(dr,10).until(EC.visibility_of_element_located(locator1))
ele1.send_keys('user01')
# 密码
locator2=(By.CSS_SELECTOR,'[name="password"]')
ele2=WebDriverWait(dr,10).until(EC.presence_of_element_located(locator2))
ele2.send_keys('123456')
# 确认密码
locator3=(By.CSS_SELECTOR,'[name="userpassword2"]')
ele3=WebDriverWait(dr,10).until(EC.presence_of_element_located(locator3))
ele3.send_keys('123456')
# 手机
locator4=(By.CSS_SELECTOR,'[name="mobile_phone"]')
ele4=WebDriverWait(dr,10).until(EC.presence_of_element_located(locator4))
ele4.send_keys('18298765432')
# 邮箱
locator5=(By.CSS_SELECTOR,'[name="email"]')
ele5=WebDriverWait(dr,10).until(EC.presence_of_element_located(locator5))
ele5.send_keys('13324578655@qq.com')
# 按钮
locator=(By.CLASS_NAME,'reg_btn')
WebDriverWait(dr,10).until(EC.element_to_be_clickable(locator)).click()

# 断言:检查用户是否注册成功
WebDriverWait(dr,10).until(EC.title_contains('会员中心'))
assert dr.find_element_by_xpath('//*[text()="user01"]')
# 关闭
dr.quit()
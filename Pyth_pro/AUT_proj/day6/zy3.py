from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# 3.海盗电商,继续完成订单
# 预置条件
url='http://127.0.0.1:85/index.php?m=user&c=public&a=login'
# 预置条件
dr=webdriver.Chrome()
dr.get(url)
dr.maximize_window()
dr.implicitly_wait(10)

# 登录
dr.find_element_by_id('username').send_keys('lgn1')
time.sleep(1)
dr.find_element_by_id('password').send_keys('123456')
time.sleep(1)
dr.find_element_by_class_name('login_btn').click()
time.sleep(4)

# 清空购物车
num = int(dr.find_element_by_xpath(".//*[@id='cart_box']//em").text)
if num !=0:
    ele = dr.find_element_by_css_selector('#cart_box>dt')
    act = ActionChains(dr).move_to_element(ele).perform()
    dr.find_element_by_xpath('//*[text()="清空购物车"]').click()
    time.sleep(2)
    ActionChains(dr).move_by_offset(150,90).perform()
# 返回首页
locator = (By.CSS_SELECTOR,'.menu.clearfix [href="/index.php"]')
ele1 = WebDriverWait(dr,10).until(EC.visibility_of_element_located(locator))
ele1.click()
time.sleep(1)
# 进入商品详情页
dr.find_element_by_css_selector('.module_pro_img>[src$="1432027851524213.jpg"]').click()
time.sleep(1)
# 切换窗口
dr.switch_to.window(dr.window_handles[-1])
time.sleep(1)
# 套餐
dr.find_element_by_xpath('//*[@data-value="套餐一"]').click()
time.sleep(1)
# 内存
dr.find_element_by_xpath('//*[@data-value="256G"]').click()
time.sleep(1)
# 颜色
dr.find_element_by_xpath('//*[@data-value="粉色"]').click()
time.sleep(1)
# 商品数量
dr.find_element_by_class_name('goods-number').send_keys(Keys.CONTROL+'a')
dr.find_element_by_class_name('goods-number').send_keys('2')
time.sleep(1)
# 加入购物车
dr.find_element_by_id('joinCarButton').click()
time.sleep(1)
# 去购物车结算
dr.find_element_by_class_name('shopCar_T_span3').click()
time.sleep(1)
# 结算
dr.find_element_by_class_name('shopCar_btn_03').click()
time.sleep(1)
# 添加新地址
dr.find_element_by_class_name('add-address').click()
time.sleep(1)
# 收货人姓名
dr.find_element_by_css_selector('[name="address[address_name]"]').send_keys('张小三')
time.sleep(1)
# 手机号
dr.find_element_by_css_selector('[name="address[mobile]"]').send_keys('13357796037')
time.sleep(1)
# 收货地址  省下拉框, 选择
se = Select(dr.find_element_by_css_selector('#add-new-area-select'))
se.select_by_visible_text('陕西省')
# 显示等待等待 市下拉框动态出现,  等待条件 市下拉框出现
locator = (By.CSS_SELECTOR,'.add-new-area>select:nth-child(3)')
ele = WebDriverWait(dr,10).until(EC.presence_of_element_located(locator))
se = Select(ele)
se.select_by_visible_text('西安市')
# 显示等待来对区元素进行定位
locator = (By.CSS_SELECTOR,'.add-new-area>select:nth-child(4)')
ele = WebDriverWait(dr,10).until(EC.presence_of_element_located(locator))
se = Select(ele)
se.select_by_visible_text('雁塔区')
time.sleep(1)
# 详细地址
dr.find_element_by_class_name('add-new-name-span-2').send_keys('科技路xxx大厦A座')
time.sleep(1)
# 邮政编码
dr.find_element_by_class_name('add-new-name-span-3').send_keys('000000')
time.sleep(1)
# 确定
dr.find_element_by_class_name('aui_state_highlight').click()
time.sleep(3)
# 配送方法
dr.find_element_by_css_selector('.pay-choose-1>label').click()
# 付款方式
locator=(By.CSS_SELECTOR,'[name="pay_type"]')
ele=WebDriverWait(dr,10).until(EC.presence_of_element_located(locator))
ele.click()
# 验证
assert 'iPhone 6' in dr.find_element_by_class_name('cart_01a_p1').text
price = dr.find_element_by_css_selector('.price').text
num = dr.find_element_by_class_name('cart_01e').text
assert float(dr.find_element_by_class_name('price-total').text)== float(price)*int(num)
# 提交订单
dr.find_element_by_class_name('agree-order-fr-btn').click()
time.sleep(3)

# 关闭
dr.quit()
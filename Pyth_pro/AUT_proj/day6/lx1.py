from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint,choice
from selenium.webdriver.support.select import Select

# 打开浏览器,进入网站
def open_browser(url):
    # 打开浏览器
    dr = webdriver.Chrome()
    # 最大化
    dr.maximize_window()
    # 进入url
    dr.get(url)
    dr.implicitly_wait(3)
    return dr
# 登录
def t_login(dr,usr,pwd):
    dr.find_element_by_xpath('//a[text()="登录"]').click()
    time.sleep(1)
    dr.switch_to.window(dr.window_handles[-1])
    time.sleep(1)
    dr.find_element_by_id('username').send_keys(f'{usr}')
    dr.find_element_by_id('password').send_keys(f'{pwd}')
    dr.find_element_by_xpath('//*[@value="登　录"]').click()
    time.sleep(2)
def back_login(dr,usr,pwd):
    dr.find_element_by_name('username').send_keys(f'{usr}')
    dr.find_element_by_name('userpass').send_keys(f'{pwd}')
    dr.find_element_by_name('userverify').send_keys('1234')
    dr.find_element_by_xpath('//*[@class="Btn"]').click()
    time.sleep(2)
# 退出浏览器
def q_bro(dr):
    dr.quit()
# 练习1: 作业2当出错时,做个截图
try:
    dr = open_browser('http://localhost:85/index.php')
    t_login(dr,'lgn1','123456')
    # 进入首页
    dr.find_element_by_xpath('//*[@class="logo fl"]//img').click()
    dr.find_element_by_css_selector('.module_pro_img>[src$="1432027851524213.jpg"]').click()
    dr.switch_to.window(dr.window_handles[-1])
    dr.find_element_by_xpath('//*[@data-value="粉色"]').click()
    dr.find_element_by_xpath('//*[@data-value = "512G"]').click()
    dr.find_element_by_xpath('//*[@data-value = "套餐一"]').click()
    num = dr.find_element_by_class_name('goods-number')
    act = ActionChains(dr)
    act.double_click(num).perform()
    num.send_keys(2)
    dr.find_element_by_id('joinCarButton').click()
    # 去购物车结算
    dr.find_element_by_class_name('shopCar_T_span3').click()
    dr.find_element_by_xpath('//a[text()="结算"]').click()
    dr.find_element_by_xpath('//div[text()="添加新地址"]').click()
    # 收货人
    dr.find_element_by_xpath('//*[@id="add-new-address"]/div[1]/input').send_keys('张三')
    # 手机号
    dr.find_element_by_xpath('//*[@id="add-new-address"]/div[2]/input').send_keys('15344335566')
    # 地区
    ele = dr.find_element_by_id('add-new-area-select')
    se = Select(ele)
    se.select_by_visible_text('北京市')
    ele = dr.find_element_by_xpath('//*[@class="add-new-area"]//select[2]')
    se = Select(ele)
    se.select_by_visible_text('北京市')
    ele = dr.find_element_by_xpath('//*[@class="add-new-area"]//select[3]')
    se = Select(ele)
    se.select_by_visible_text('朝阳区')
    # 详细地址
    dr.find_element_by_xpath('//*[@id="add-new-address"]/div[4]/input').send_keys('朝阳区派出所')
    # 邮编
    dr.find_element_by_xpath('//*[@id="add-new-address"]/div[5]/input').send_keys('110105')
    time.sleep(3)
    # 确认
    dr.find_element_by_xpath('//*[@class="aui_state_highlight"]').click()
    time.sleep(3)
except Exception as e:
    print(e)
    print('出现错误')
    time_str = time.strftime('%Y%m%d_%H%M%S')
    dr.get_screenshot_as_file(f'./screenshot/{time_str}.png')
finally:
    q_bro(dr)


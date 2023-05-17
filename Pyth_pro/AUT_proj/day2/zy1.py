from selenium import webdriver
import time
# 1.12306的火车票的查询做一下:
# 预置条件
dr = webdriver.Chrome()
dr.get('https://www.12306.cn/index/')
dr.maximize_window()
time.sleep(1)

#出发地
ele = dr.find_element_by_css_selector('#fromStationText')
ele.click()
ele.send_keys('西安北')
time.sleep(1)
ele = dr.find_element_by_css_selector('#citem_0').click()

#到达地
ele = dr.find_element_by_css_selector('#toStationText')
ele.click()
ele.send_keys('北京西')
time.sleep(1)
ele = dr.find_element_by_css_selector('#citem_0').click()

#时间
ele = dr.find_element_by_css_selector('#train_date')
ele.clear()
ele.send_keys('2022-10-16')
time.sleep(1)
#勾选 学生
ele=dr.find_element_by_css_selector('#isStudentDan').click()
#勾选 高铁
ele =dr.find_element_by_css_selector('#isHighDan').click()
time.sleep(2)
#注册
ele = dr.find_element_by_css_selector('#search_one')
ele.click()
time.sleep(2)
#关闭
dr.quit()
from selenium import webdriver
import time
# 2.打印https://item.jd.com/100027028257.html
url='https://item.jd.com/100027028257.html'
# 预置条件
dr=webdriver.Chrome()
dr.get(url)
dr.maximize_window()

# 商品介绍
dr.find_element_by_css_selector('#detail [clstag$="shangpinjieshao_1"]').click()
time.sleep(1)
print(dr.find_element_by_css_selector('#parameter-brand').text)
print(dr.find_element_by_css_selector('.parameter2.p-parameter-list').text)
# 规格与包装
dr.find_element_by_css_selector('#detail [clstag$="pcanshutab"]').click()
time.sleep(1)
print(dr.find_element_by_css_selector('.Ptable').text)
print(dr.find_element_by_css_selector('.package-list').text)
# 售后保障
dr.find_element_by_css_selector('#detail [clstag$="psaleservice"]').click()
time.sleep(1)
print(dr.find_element_by_css_selector('.serve-agree-bd').text)
print(dr.find_element_by_css_selector('#state').text)
# 商家评价
dr.find_element_by_css_selector('#detail [clstag$="shangpinpingjia_1"]').click()
time.sleep(1)
# 好评度
print(dr.find_element_by_css_selector('.comment-percent').text)
print(dr.find_element_by_css_selector('[clstag$="comment_icon"]').text)
print(dr.find_element_by_css_selector('.tab-main.small').text)
print(dr.find_element_by_css_selector('#comment-0').text)
# 关闭
dr.close()
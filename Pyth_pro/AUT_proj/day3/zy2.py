from selenium import webdriver
import time
# 3.爱奇艺首页获取最热门的关键词一个,并完成搜索和点击播放操作.
# 要求:尽量使用xpath来定位.
# https://www.iqiyi.com/
# 准备工作
dr=webdriver.Chrome()
dr.get("https://www.iqiyi.com/")
dr.maximize_window()
dr.find_element_by_xpath('//img[@class="header__promotion__close"]').click()
time.sleep(5)
# 执行
s=dr.find_elements_by_xpath('//*[@class="title-main"]')[0].text
dr.find_element_by_xpath("//*[@id='J-header-search-input']").send_keys(s)
dr.find_element_by_xpath("//*[@id='J-search-btn']").click()
dr.switch_to.window(dr.window_handles[-1])
dr.find_element_by_xpath("//*[@class='album-list']/li[1]").click()
time.sleep(5)
# 关闭
dr.quit()
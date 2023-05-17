# from selenium import webdriver
# import time
# # 1.12306搜索后,打印当天的车次信息,并提示用户哪些车次可以选择.
# url='https://www.12306.cn/index/'
# # 预置条件
# dr=webdriver.Chrome()
# dr.get(url)
# dr.maximize_window()
# # print(dr.current_window_handle)
# # 执行测试步骤
# # 出发地
# ele=dr.find_element_by_xpath('//*[@id="fromStationText"]')
# ele.click()
# dr.find_element_by_xpath('//*[@id="nav_list6"]').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@title="西安北"]').click()
# time.sleep(1)
# # 到达地
# ele=dr.find_element_by_xpath('//*[@id="toStationText"]')
# ele.click()
# dr.find_element_by_xpath('//*[@id="nav_list2"]').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@title="北京西"]').click()
# time.sleep(1)
# # 出发日期
# ele=dr.find_element_by_xpath('//*[@id="train_date"]')
# ele.clear()
# ele.send_keys('2022-10-16')
# time.sleep(3)
# # 学生  高铁/动车
# dr.find_element_by_xpath('//*[@id="isStudentDan"]').click()
# time.sleep(3)
# dr.find_element_by_xpath('//*[@id="isHighDan"]').click()
# time.sleep(3)
# # 查询
# dr.find_element_by_xpath('//*[@id="search_one"]').click()
# time.sleep(3)
# dr.switch_to.window(dr.window_handles[1])
# # print(dr.current_window_handle)
#
# dr.find_element_by_xpath('//*[@id="qd_closeDefaultWarningWindowDialog_id"]').click()
# time.sleep(1)
# i=1
# tbody = dr.find_element_by_css_selector('#queryLeftTable')
# tr_list = tbody.find_elements_by_tag_name('tr')
# while i<len(tr_list):
#     # 商务座订票信息
#     ele1=dr.find_element_by_xpath('//*[@id="queryLeftTable"]/tr[%d]/td[2]'%i)
#     # 一等座订票信息
#     ele2=dr.find_element_by_xpath('//*[@id="queryLeftTable"]/tr[%d]/td[3]'%i)
#     # 二等座订票信息
#     ele3=dr.find_element_by_xpath('//*[@id="queryLeftTable"]/tr[%d]/td[4]'%i)
#     if not(ele1.text=='无' and ele2.text=='无' and ele3.text=='无'):
#         print(dr.find_element_by_xpath('//*[@id="queryLeftTable"]/tr[%d]/td[1]//a'%i).text,'可以预订!')
#     i+=2
# # 关闭
# dr.quit()

from selenium import webdriver
import time
# 1.12306搜索后,打印当天的车次信息,并提示用户哪些车次可以选择.
# 准备工作
dr=webdriver.Chrome()
dr.get("https://www.12306.cn/index/")
dr.maximize_window()
# 执行
dr.find_element_by_xpath('//*[@class="icon icon-dancheng"]').click()
dr.find_element_by_xpath("//*[@id='fromStationText']").click()
dr.find_element_by_xpath("//*[@id='nav_list6']").click()
dr.find_element_by_xpath("//*[@title='西安北']").click()
dr.find_element_by_xpath('//*[@id="toStationText"]').click()
dr.find_element_by_xpath("//*[@id='nav_list2']").click()
dr.find_element_by_xpath("//*[@title='北京西']").click()
ele=dr.find_element_by_xpath("//*[@id='train_date']")
ele.clear()
ele.send_keys("2022-10-16")
dr.find_element_by_xpath('//*[@id="isStudentDan"]').click()
dr.find_element_by_xpath('//*[@id="isHighDan"]').click()
dr.find_element_by_xpath('//*[@id="search_one"]').click()
dr.switch_to.window(dr.window_handles[-1])
time.sleep(3)
dr.find_element_by_xpath('//*[@id="qd_closeDefaultWarningWindowDialog_id"]').click()
print(dr.find_element_by_xpath("//*[@id='t-list']").text)
li=dr.find_elements_by_xpath('//*[@class="no-br"]')
print(len(li))
j=1
for i in range(len(li)-1):
    try:
        dr.find_element_by_xpath(f'//*[@id="queryLeftTable"]/tr[{j}]/td/a')
    except:
        print(dr.find_element_by_xpath(f'//*[@id="queryLeftTable"]/tr[{j}]/td[1]//a').text,'不可选择')
    else:
        print(dr.find_element_by_xpath(f'//*[@id="queryLeftTable"]/tr[{j}]/td[1]//a').text,'可选择')

    finally:
        j+=2
# 关闭
dr.quit()
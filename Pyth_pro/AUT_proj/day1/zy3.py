from selenium import webdriver
import time
# 1.请填写本网站的注册信息,然后点击注册按钮.http://goootech.com/signup_personal.aspx
# 预置条件
try:
    dr = webdriver.Chrome()
    url='http://goootech.com/signup_personal.aspx'
    dr.get(url)
    dr.maximize_window()

    # 输入邮箱
    ele=dr.find_element_by_id('UEmail')
    ele.send_keys('123@456.com')
    time.sleep(1)

    # 输入姓名
    ele=dr.find_element_by_id('URealName')
    ele.clear()
    ele.send_keys('张三')
    time.sleep(1)

    # 输入昵称
    ele=dr.find_element_by_id('UNickName')
    ele.clear()
    ele.send_keys('时空')
    time.sleep(1)

    # 输入电话
    ele=dr.find_element_by_id('UTel')
    ele.send_keys('13925980021')
    time.sleep(1)

    # 输入密码
    ele=dr.find_element_by_id('UPwd1')
    ele.send_keys('123456')
    time.sleep(1)

    # 确认密码
    ele=dr.find_element_by_id('UPwd2')
    ele.send_keys('123456')
    time.sleep(1)

    # 工作单位
    ele=dr.find_element_by_id('UCompany')
    ele.send_keys('云星科技有限公司')
    time.sleep(20)

    #所属行业  环保检测
    ele_list = dr.find_elements_by_tag_name('label')
    ele = ele_list[2]
    ele.click()

    # 点击注册
    ele=dr.find_element_by_id('btnOk')
    ele.click()
    time.sleep(3)
except Exception as e:
    print(e)

finally:
    # 测试结束,关闭浏览器
    dr.close()
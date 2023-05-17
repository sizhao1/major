from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

# 1.海盗的后台, 添加一个新商品
# 打开网页
url = 'http://127.0.0.1:85/admin.php'
dr = webdriver.Chrome()
dr.get(url)
dr.maximize_window()
# 隐式等待
dr.implicitly_wait(10)

#输入用户名密码
ele = dr.find_element_by_css_selector('[placeholder$="用户名"]')
ele.send_keys('admin')
ele = dr.find_element_by_css_selector('[placeholder$="密码"]')
ele.send_keys('password')
ele = dr.find_element_by_css_selector('[placeholder="验证码"]')
ele.send_keys('1234')

#点击登录
dr.find_element_by_css_selector('.Btn').click()
time.sleep(1)

#点击商品管理
dr.find_element_by_link_text('商品管理').click()
time.sleep(1)
#点击添加商品
dr.find_element_by_css_selector('.n11.z_side').click()
time.sleep(1)

#切换到添加商品表单
dr.switch_to.frame('mainFrame')
time.sleep(1)

#选中商品名称输入框并输入信息
ele = dr.find_elements_by_css_selector('.text_input')[0]
ele.send_keys('华为P50')
time.sleep(1)

#选择商品分类标签
dr.find_element_by_id('1').click()
time.sleep(1)
dr.find_element_by_id('2').click()
time.sleep(1)
dr.find_element_by_id('6').click()
time.sleep(1)
ele = dr.find_element_by_id('7')
act = ActionChains(dr)
act.double_click(ele).perform()
time.sleep(1)

# 选择品牌
ele = dr.find_element_by_css_selector('[name="brand_id"]')
se = Select(ele)
se.select_by_visible_text('华为')
time.sleep(1)

# 是否上架销售
dr.find_element_by_xpath('//*[@name="status" and @value="0"]').click()
# 商品状态
dr.find_element_by_css_selector('[name="is_sales"]').click()
dr.find_element_by_css_selector('[name="is_hot"]').click()
dr.find_element_by_css_selector('[name="is_new"]').click()
# 商品关键字
dr.find_element_by_css_selector('[name="keyword"]').send_keys('华为 P50')
# 商品描述
dr.find_element_by_css_selector('[name="brief"]').send_keys('华为品牌 手机 型号 P50')
time.sleep(3)

#点击提交
dr.find_element_by_css_selector('.button_search').click()
time.sleep(3)
#结束进程
dr.quit()
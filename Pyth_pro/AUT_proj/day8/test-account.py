from selenium import webdriver
import unittest,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# (3).使用unittest框架完成会员账号的测试, 要求测试:
# 01.修改收货人姓名,断言收货人姓名是否修改
class TestAccount(unittest.TestCase):
    def login(self,usr,pwd):
        # 输入用户名
        ele_li = self.dr.find_elements_by_tag_name('input')
        ele_li[5].send_keys(usr)
        # 输入密码
        ele_li[6].send_keys(pwd)
        # 点击登录
        ele = self.dr.find_element_by_class_name('login_btn')
        ele.click()
        # 线程休眠3秒
        time.sleep(3)

    def click_text(self,text):
        self.dr.find_element_by_xpath(f'//*[text()="{text}"]').click()

    def setUp(self):
        url = 'http://127.0.0.1:85/index.php?m=user&c=user&a=manage'
        # 1.打开浏览器
        self.dr = webdriver.Chrome()
        # 2.输入对应的url地址
        self.dr.get(url)
        # 3.最大化窗口
        self.dr.maximize_window()
        # 4.设置隐式等待 10秒
        self.dr.implicitly_wait(10)
        # 5.登录
        self.login('lgn1',123456)

    def tearDown(self):
        self.dr.quit()

    # 测试修改收货人姓名
    def test_member_user(self):
        # 点击修改收货人姓名
        self.click_text('修改收货人姓名')
        # 点击编辑  .ditable>tbody>tr:nth-child(2)>td>a:nth-child(2)
        self.click_text('编辑')
        # 修改收货人姓名
        ele = self.dr.find_element_by_css_selector('#username')
        ele.clear()
        ele.send_keys('张三疯')
        time.sleep(1)
        # 点击编辑地址
        self.dr.find_element_by_css_selector('.btn3').click()
        time.sleep(1)
        # 处理弹窗
        WebDriverWait(self.dr,10).until(EC.alert_is_present())
        alert=self.dr.switch_to.alert
        print(alert.text)
        WebDriverWait(self.dr, 10).until(EC.alert_is_present())
        self.dr.switch_to.alert.accept()
        # 断言
        self.assertEqual('张三疯',self.dr.find_element_by_css_selector('.ditable>tbody>tr:nth-child(2)>td:first-child').text)


    # 02.修改默认收货地址,默认地址为第二条. 断言第二条收货地址是否为默认收货地址.
    def test_member_address(self):
        # 点击修改默认收货地址
        self.click_text('修改默认收货地址')
        # 把第二个地址设为默认地址
        ele = self.dr.find_element_by_css_selector('.ditable>tbody>tr:nth-child(3)>td:nth-child(5)')
        if "默认地址" not in ele.text:
            self.dr.find_element_by_css_selector('.ditable>tbody>tr:nth-child(3)>td:nth-child(5)>a:first-child').click()
            # 处理弹窗
            WebDriverWait(self.dr, 10).until(EC.alert_is_present())
            alert=self.dr.switch_to.alert
            print(alert.text)
            alert.accept()
            WebDriverWait(self.dr, 10).until(EC.alert_is_present())
            self.dr.switch_to.alert.accept()
            # 断言
            self.assertIn('默认地址',self.dr.find_element_by_css_selector('.ditable>tbody>tr:nth-child(3)>td:nth-child(5)').text)








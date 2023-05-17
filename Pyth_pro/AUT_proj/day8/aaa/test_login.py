from selenium import webdriver
import unittest,time,csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ddt import *


def get_data(filepath):
    lis = []
    with open(filepath, encoding='utf-8') as f:
        csv_r = csv.reader(f)
        for row in csv_r:
            lis.append(row)
    return lis

@ddt
class TestLogin(unittest.TestCase):
    # 设置预置条件
    def setUp(self):
        # 1.打开浏览器
        self.dr = webdriver.Chrome()
        # 2.输入对应的url地址
        url = 'http://127.0.0.1:85/index.php?m=user&c=public&a=login'
        self.dr.get(url)
        # 3.最大化窗口
        self.dr.maximize_window()
        # 4.设置隐式等待 10秒
        self.dr.implicitly_wait(10)

    # 设置结束条件
    def tearDown(self):
        self.dr.quit()

    @data(['lgn1',123456],['user01',123456],['abc123',123456])
    @unpack
    # 测试登录成功
    def test_login_success(self,usr,pwd):
        self.login(usr,pwd)
        # 做断言,检验登录是否成功
        self.assertIn('会员中心',self.dr.title)
        self.assertTrue(self.dr.find_element_by_xpath(f'//*[text()="{usr}"]'))

    @data(*get_data('../data/login_data.csv'))
    @unpack
    # 测试登录失败
    def test_login_failed(self,usr,pwd):
        self.login(usr,pwd)
        # 做断言,检查登录是不是失败了
        self.assertNotIn('会员中心', self.dr.title)
        self.assertTrue(self.dr.find_element_by_xpath('//*[text()="登录"]'))

    def test_reg(self):
        self.click_text('立即注册')
        # 断言
        WebDriverWait(self.dr,10).until(EC.title_contains('用户注册'))
        self.assertTrue(self.dr.find_element_by_xpath('//*[text()="道e坊商城用户注册"]'))

    def test_repwd(self):
        self.click_text('忘记密码')
        # 断言
        WebDriverWait(self.dr, 10).until(EC.url_contains('a=repwd'))
        self.assertTrue(self.dr.find_element_by_xpath('//*[text()="取回密码"]'))

    def click_text(self,text):
        self.dr.find_element_by_xpath(f'//*[text()="{text}"]').click()

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

if __name__ == '__main__':
    unittest.main()
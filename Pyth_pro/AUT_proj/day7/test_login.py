'''
unittest框架: python的单元测试框架, 用于做单元测试.
基于面向对象的框架.  python自带的,不需要安装, 不需要引入.
TestCase类:  用于编写测试用例.
TestSuit类:  用于组织测试用例.
TextTestRunner类:  用于运行测试用例,获取结果.

TestCase类:
1.导包  import unittest
2.自定义的测试类要继承unittest.TestCase类  -- 测试类一定是TestCase的子类
3.测试方法必须以test开头
4.重写setUp()和tearDown()方法, 利用setUp()来写预置条件, 利用tearDown()来写结束条件
setUp(): 在每个测试方法运行前,自动被调用一次.
tearDown(): 在每个测试方法运行后,自动被调用一次.
5.提供有丰富的断言
assertIn(member, str): 断言子串在字符串中
assertNotIn(member, str): 断言子串不在字符串中
assertTrue(expr): 断言表达式转bool后是True
assertFalse(expr): 断言表达式转bool后是True
assertNone(expr): 断言表达式或对象是不存在的,为空.

pytest框架: 既可以面向对象也可以面向过程. 需要安装.
'''
from selenium import webdriver
import unittest,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    # 测试登录成功
    def test_login_success(self):
        self.login('lgn1',123456)
        # 做断言,检验登录是否成功
        self.assertIn('会员中心',self.dr.title)
        self.assertTrue(self.dr.find_element_by_xpath('//*[text()="lgn1"]'))

    # 测试登录失败
    def test_login_failed(self):
        self.login('lgn1',12)
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


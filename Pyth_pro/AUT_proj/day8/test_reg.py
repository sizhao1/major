from selenium import webdriver
import unittest,time,random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# (1).使用unittest框架完成海盗电商注册,要求测试:
# 01.注册成功
# 02.注册失败
# 03.已有账号,立即登录链接
class TestReg(unittest.TestCase):
    # 设置预置条件
    def setUp(self):
        # 1.打开浏览器
        self.dr = webdriver.Chrome()
        # 2.输入对应的url地址
        url = 'http://127.0.0.1:85/index.php?m=user&c=public&a=reg'
        self.dr.get(url)
        # 3.最大化窗口
        self.dr.maximize_window()
        # 4.设置隐式等待 10秒
        self.dr.implicitly_wait(10)

    # 设置结束条件
    def tearDown(self):
        # 当测试结果出错的时候,保存截图,方便进行问题分析
        for method,error in self._outcome.errors:
            if error:
                time_str = time.strftime('%Y%m%d_%H%M%S')
                file_path = self._testMethodName+time_str
                self.dr.get_screenshot_as_file(f'./report/screenshot/{file_path}.png')
        # 结束测试, 彻底关闭浏览器进程
        self.dr.quit()

    # 01.注册成功
    def test_reg_success(self):
        # self.click_text('立即注册')
        usr = 'abc'+str(time.time())[:10]
        phone = random.randint(13000000000,13999999999)
        self.reg(usr,123456,123456,phone,usr+'@qq.com')
        # 断言
        WebDriverWait(self.dr,10).until(EC.title_contains('会员中心'))
        self.assertTrue(self.dr.find_element_by_xpath(f'//*[text()="{usr}"]'))
    time.sleep(3)

    # 02.注册失败
    def test_reg_failed(self):
        # self.click_text('立即注册')
        self.reg("user01",123456,123456,13677778888,'abcd123@qq.com')
        # 断言
        WebDriverWait(self.dr,10).until(EC.title_contains('用户注册'))
        self.assertTrue(self.dr.find_element_by_xpath('//*[text()="道e坊商城用户注册"]'))

    # 03.已有账号, 立即登录链接
    def test_login(self):
        self.click_text("登　录")
        ## 做断言,检验登录是否成功
        self.assertIn('用户登录',self.dr.title)
        self.assertTrue(self.dr.find_element_by_xpath('//*[text()="欢迎登录道e坊商城"]'))

    def click_text(self,text):
        self.dr.find_element_by_xpath(f'//*[text()="{text}"]').click()

    def reg(self,usr,pwd,pwd2,phone,email):
        # 输入用户名
        ele = self.dr.find_element_by_name('username')
        ele.send_keys(usr)
        time.sleep(1)

        # 输入密码
        ele = self.dr.find_element_by_name('password')
        ele.send_keys(pwd)
        time.sleep(1)

        # 确认密码  input_100 Validform_error
        ele = self.dr.find_element_by_name('userpassword2')
        ele.send_keys(pwd2)
        time.sleep(1)

        # 手机  mobile_phone
        ele = self.dr.find_element_by_name('mobile_phone')
        ele.send_keys(phone)
        time.sleep(1)

        # 邮箱  email
        ele = self.dr.find_element_by_name('email')
        ele.send_keys(email)
        time.sleep(1)

        # 点击注册 reg_btn
        ele = self.dr.find_element_by_class_name('reg_btn')
        ele.click()
        time.sleep(3)
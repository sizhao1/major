from selenium import webdriver
import unittest,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# (2).使用unittest框架完成会员中心的测试,要求测试:
# 01.交易信息
# 02.交易操作各个链接
# 03.正在进行中的交易
# 04.已买到的宝贝
# 05.已收藏的宝贝
# 06.我最近的浏览记录
class TestMember(unittest.TestCase):
    runornot = 'no'
    def setUp(self):
    # 1.打开浏览器
        self.dr = webdriver.Chrome()
        # 2.输入对应的url地址
        url = 'http://127.0.0.1:85/index.php?m=user&c=index&a=index'
        self.dr.get(url)
        # 3.最大化窗口
        self.dr.maximize_window()
        # 4.设置隐式等待 10秒
        self.dr.implicitly_wait(10)
        # 5.登录
        self.login('lgn1',123456)

    def tearDown(self):
        self.dr.quit()

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

    # 测试交易信息
    @unittest.skipIf(runornot=='no','不需要运行')
    def test_trade_info(self):
        # 交易信息
        print(self.dr.find_element_by_css_selector('.jiaoyi>h3').text)
        print(self.dr.find_element_by_css_selector('.jiaoyi>ul>li').text)
        print(self.dr.find_element_by_css_selector('.jiaoyi>ul>li:nth-child(2)').text)
        print(self.dr.find_element_by_css_selector('.jiaoyi>ul>li:nth-child(3)').text)

    # 测试交易操作
    @unittest.skipIf(runornot=='no', '不需要运行')
    def test_trade_oper(self):
        # 交易操作各个链接
        print(self.dr.find_element_by_css_selector('.chaozuo>h3').text)
        print(self.dr.find_element_by_css_selector('.chaozuo>ul>li>a').text)
        print(self.dr.find_element_by_css_selector('.chaozuo>ul>li:nth-child(2)').text)
        print(self.dr.find_element_by_css_selector('.chaozuo>ul>li:nth-child(3)').text)
        print(self.dr.find_element_by_css_selector('.chaozuo>ul>li:nth-child(4)').text)
        print(self.dr.find_element_by_css_selector('.chaozuo>ul>li:nth-child(5)').text)

    # 测试正在进行中的交易
    @unittest.skipIf(runornot=='no', '不需要运行')
    def test_trade_now(self):
        # 03.正在进行中的交易
        print(self.dr.find_element_by_css_selector('.dealing').text)
        # print(self.dr.find_element_by_css_selector('.clearfix').text)

    @unittest.skipIf(runornot=='no', '不需要运行')
    def test_buy(self):
        # 04.已买到的宝贝
        print(self.dr.find_element_by_css_selector('.mbaob.fl').text)

    @unittest.skipIf(runornot=='no', '不需要运行')
    def test_cang(self):
        # 05.已收藏的宝贝
        print(self.dr.find_element_by_css_selector('.sbaob.fr').text)


    def test_browse(self):
        # 06.我最近的浏览记录
        print(self.dr.find_element_by_css_selector('.liulan').text)
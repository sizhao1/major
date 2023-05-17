import unittest,time,ddt

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from day8.po.login.login_business import LoginBusiness
from day8.po.testutil import *

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.lo = LoginBusiness()
        self.lo.click_login_link()
        time.sleep(3)
        switch_window(self.lo.dr)


    def tearDown(self):
        self.lo.dr.quit()

    @ddt.data(['lgn1',123456],['user01',123456])
    @ddt.unpack
    # 测试登录的逻辑
    def test_login_success(self,usr,pwd):
        self.lo.login(usr,pwd)
        # 断言
        WebDriverWait(self.lo.dr,10).until(EC.title_contains('会员中心'))
        self.assertTrue(self.lo.dr.find_element_by_xpath(f'//*[text()="{usr}"]'))

if __name__ == '__main__':
    unittest.main()
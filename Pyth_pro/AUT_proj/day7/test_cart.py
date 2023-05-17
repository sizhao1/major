'''
TestCase类练习
'''
from selenium import webdriver
import unittest,time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 练习2:把购物车作为一个模块,写一个测试类来测试购物车这个模块.
# 要求:
# 1.把商品加入购物车
# 2.清空购物车
# 3.购物车去结算

class TestCart(unittest.TestCase):
    # 设置预置条件
    def setUp(self):
        # 1.打开浏览器
        self.dr = webdriver.Chrome()
        # 2.输入对应的url地址
        url = 'http://127.0.0.1:85/index.php?m=goods&c=index&a=detail&id=1'
        self.dr.get(url)
        # 3.最大化窗口
        self.dr.maximize_window()
        # 绕过登录
        dic1 = {'name':'PHPSESSID','value':'umlc89mm2h5qfh5dq9hqj973q4'}
        dic2 = {'name':'user_key','value':'d6155fJTP2LMaHcKIO2sf29HKayIR0DdEvZeCMel1w'}
        self.dr.add_cookie(dic1)
        self.dr.add_cookie(dic2)
        self.dr.refresh()
        # 4.设置隐式等待 10秒
        self.dr.implicitly_wait(10)

    # 设置结束条件
    def tearDown(self):
        self.dr.quit()

    def test_add_cart(self):
        # 添加商品到购物车
        self.choice_shop('粉色','128G','套餐一',3)
        self.dr.find_element_by_id('joinCarButton').click()
        # 断言
        WebDriverWait(self.dr,10).until(EC.url_contains('a=succeed'))
        self.assertEqual('商品已成功加入购物车',self.dr.find_element_by_css_selector('.shopCar_T_span1').text)

    # 测试 清空购物车
    def test_clear_cart(self):
        # 添加商品到购物车
        self.choice_shop('粉色','128G','套餐一',3)
        self.dr.find_element_by_id('joinCarButton').click()
        time.sleep(3)
        # 悬浮购物车
        dianji = self.dr.find_element_by_xpath('//dt[text()="去购物车结算"]')
        act = ActionChains(self.dr)
        act.move_to_element(dianji).perform()
        time.sleep(3)
        # 点击 清空购物车
        locator = (By.LINK_TEXT,"清空购物车")
        ele = self.find_element_by_webdriverwait(locator)
        ele.click()
        # 到空白处进行点击
        ActionChains(self.dr).move_by_offset(150,90).perform()
        time.sleep(2)
        # 断言
        locator = (By.CSS_SELECTOR, '.shop_number>em')
        self.assertEqual('0',self.find_element_by_webdriverwait(locator).text)

    def find_element_by_webdriverwait(self,locator):
        ele = WebDriverWait(self.dr, 10).until(EC.presence_of_element_located(locator))
        return ele


    def test_pay(self):
        # 添加商品到购物车
        self.choice_shop('粉色','128G','套餐一',3)
        self.dr.find_element_by_id('joinCarButton').click()
        time.sleep(3)
        # 悬浮到购物车,然后点击 去购物车结算
        dianji = self.dr.find_element_by_xpath('//dt[text()="去购物车结算"]')
        act = ActionChains(self.dr)
        act.move_to_element(dianji).perform()
        self.dr.find_element_by_xpath('//a[text()="去购物车结算"]').click()
        self.click('结算')
        # 断言
        WebDriverWait(self.dr,10).until(EC.title_contains('核对订单信息'))
        self.assertEqual('填写核对订单',self.dr.find_element_by_css_selector('.shopCar_Title-2').text)

    def choice_shop(self,color,storage,taocan,num):
        self.dr.find_element_by_xpath(f'//*[contains(text(),"{color}")]').click()
        self.dr.find_element_by_xpath(f'//*[contains(text(),"{storage}")]').click()
        self.dr.find_element_by_xpath(f'//*[contains(text(),"{taocan}")]').click()
        dianji = self.dr.find_element_by_xpath('//*[@class="goods-number"]')
        act=ActionChains(self.dr)
        act.double_click(dianji).perform()
        dianji.send_keys(num)


    def click(self, text):
        self.dr.find_element_by_xpath(f'//*[text()="{text}"]').click()

    def address(self,num):
        self.dr.find_element_by_xpath(f'//*[@id="address-box"]/div[{num}]').click()

    def kuaidi(self,kuaidi):
        self.dr.find_element_by_xpath(f'//*[text()="{kuaidi}"]').click()

    def pay_fangshi(self,pay):
        self.dr.find_element_by_xpath(f'//*[text()="{pay}"]').click()

if __name__ == '__main__':
    unittest.main()
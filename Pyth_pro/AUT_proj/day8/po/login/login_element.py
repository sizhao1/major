from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from day8.po.base import Base

# 这个类用来记录登录页面的所有标签
class LoginElement(Base):
    usr = '#username'
    pwd = '#password'
    btn = '.login_btn'
    login_link = '登录'

    # 显示等待定位出用户名标签
    def get_usr_ele(self):
        ele = self.get_ele(By.CSS_SELECTOR,LoginElement.usr)
        return ele

    # 显示等待定位出密码标签
    def get_pwd_ele(self):
        ele = self.get_ele(By.CSS_SELECTOR,LoginElement.pwd)
        return ele

    # 显示等待定位出登录按钮标签
    def get_btn_ele(self):
        ele = self.get_ele(By.CSS_SELECTOR,LoginElement.btn)
        return ele

    # 显示等待定位出登录超链接标签
    def get_hyperlink(self):
        ele = self.get_ele(By.LINK_TEXT, LoginElement.login_link)
        return ele

    def get_ele(self,by_method,value):
        locator = (by_method,value)
        ele = WebDriverWait(self.dr,10).until(EC.presence_of_element_located(locator))
        return ele

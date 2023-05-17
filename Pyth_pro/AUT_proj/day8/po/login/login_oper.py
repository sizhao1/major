from day8.po.login.login_element import LoginElement

class LoginOper(LoginElement):
    def ele_send_keys(self,ele,value):
        ele.send_keys(value)

    def ele_clear(self,ele):
        ele.clear()

    def ele_click(self,ele):
        ele.click()

    # 给用户号名输入数据
    def input_usr_value(self,usr):
        ele = self.get_usr_ele()
        self.ele_clear(ele)
        self.ele_send_keys(ele,usr)

    # 给密码输入数据
    def input_pwd_value(self,pwd):
        ele = self.get_pwd_ele()
        self.ele_clear(ele)
        self.ele_send_keys(ele,pwd)

    # 点击登录按钮
    def click_login_btn(self):
        ele = self.get_btn_ele()
        self.ele_click(ele)

    # 点击登录超链接
    def click_login_link(self):
        ele = self.get_hyperlink()
        self.ele_click(ele)
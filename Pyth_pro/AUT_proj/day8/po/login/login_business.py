from day8.po.login.login_oper import LoginOper

class LoginBusiness(LoginOper):

    # 实现登录的业务逻辑
    def login(self,usr,pwd):
        self.input_usr_value(usr)
        self.input_pwd_value(pwd)
        self.click_login_btn()
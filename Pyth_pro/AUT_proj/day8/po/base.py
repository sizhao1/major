from selenium import webdriver

class Base:
    def __init__(self):
        url = 'http://127.0.0.1:85/'
        self.dr = webdriver.Chrome()
        self.dr.get(url)
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)

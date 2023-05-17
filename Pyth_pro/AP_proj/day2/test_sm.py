'''
unittest框架:
python自带的单元测试框架.
不需要安装,需要导包:  import unittest.
框架: 半成品, 使用上要遵守使用上的规范.

主要使用的半成品:
TestCase类:        编写测试用例
TestSuite类:       组织测试用例
TextTestRunner类:  运行测试用例

TestCase类的使用方法:
1.导包   import unittest
2.测试类必须继承 unittest.TestCase类
3.所有的测试方法,方法名必须以test开头
4.测试方法前可以使用setUp()方法设置初始化条件, 测试方法执行完毕后可以使用tearDown()方法来结束测试,清理环境.
5.可以使用TestCase类中丰富的断言
self.assertTrue()
self.assertFalse()
self.assertEqual()
self.assertIn()
self.assertNotIn()
'''
# 1.导包
import unittest,requests
from day2.testutil import *

# 2.继承
class TestSM(unittest.TestCase):
    # 测试环境的初始化
    def setUp(self):
        self.session = requests.session()
        r = post_request(self.session,'http://127.0.0.1:8000/stu/loginsys/',data={'username':'hzdltest','password':'hzdltest'})
        print('setup开始了...')

    # 测试环境的结束工作
    def tearDown(self):
        self.session.close()
        print('tearDown开始了...')

    # 3.测试方法名
    def test_login(self):
        session = requests.session()
        r = post_request(session,'http://127.0.0.1:8000/stu/loginsys/',data={'username':'hzdltest','password':'hzdltest'})
        self.assertEqual(get_response_status(r),200)
        self.assertIn('login success!',get_response_text(r))
        session.close()


    def test_add_student(self):
        r = post_request(self.session, 'http://127.0.0.1:8000/stu/addstu/',data={'stu_name':'张龙','stu_class':'三年级一班',                          'stu_sex':'男','stu_phone':13981438114,'stu_email':'14381438114@qq.com'})
        assert get_response_status(r)==200
        assert 'success' in get_response_text(r)

    def test_get_student(self):
        r = get_request(self.session,'http://127.0.0.1:8000/stu/getstu?eid=1',params={'stu_id':1})
        assert get_response_status(r) == 200
        assert 'success' in get_response_text(r)

    def test_modify_student(self):
        print(444)

    def test_delete_student(self):
        print(444)
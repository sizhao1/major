'''
两个类方法:
setUpClass():每个类前调用一次,做每个类之前环境的准备工作.
tearDownClass():每个类后调用一次,做每个类之后的环境的扫尾工作.

类方法:
1.类前加注解(装饰器): @classmethod
2.类方法的第一个参数: cls
3.调用的时候, 在对象方法中, self也能调,cls也能调.

ddt:
数据驱动测试.
第三方库包, 需要安装,需要导包.   import ddt |  from ddt import *
使用:
1.类前加ddt装饰器
2.方法前加data装饰器, 组装数据,用列表来构成一组测试数据,所有列表作为元素加入到data()里作为参数.
3.方法前加unpack装饰器, 拆出一组数据,这组数据作为实参传入测试方法的形参中.

'''
import unittest,ddt,time
from day3.testutil import *
from day3.dbutil import *

@ddt.ddt
class Test_SM(unittest.TestCase):
    # def setUp(self):
    #     self.session = requests.session()
    #     self.session.post('http://127.0.0.1:8000/stu/loginsys/',data={'username':'hzdltest','password':'hzdltest'})
    #
    # def tearDown(self):
    #     self.session.close()

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        cls.session.post('http://127.0.0.1:8000/stu/loginsys/',data={'username':'hzdltest','password':'hzdltest'})

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        if cur is not None:
            close_cur()
        if con is not None:
            close_con()

    @ddt.data(['张一龙','T88期','男',13911001200,'13911001200@qq.com'],['张二龙','T88期','男',13911001201,'13911001201@qq.com'],['张三龙','T88期','男',13911001202,'13911001202@qq.com'])
    @ddt.unpack
    def test_add_student(self,name,bj,sex,phone,email):
        r = post_request(self.session, 'http://127.0.0.1:8000/stu/addstu/',data={'stu_name':name,'stu_class':bj,                          'stu_sex':sex,'stu_phone':phone,'stu_email':email})
        self.assertEqual(get_status_code(r),200)
        self.assertIn('success',get_text(r))
        self.assertEqual(get_jsondata(r)['stu_phone'],str(phone))
        res = execute_sql(f"select * from hello_student where stu_name='{name}';")
        time.sleep(0.5)
        if res:
            print('查到了!')

    @unittest.skip
    def test_get_student(self):
        r = get_request(self.session,'http://127.0.0.1:8000/stu/getstu?eid=1',params={'stu_id':1})
        self.assertEqual(get_status_code(r), 200)
        self.assertIn('success', get_text(r))
        self.assertEqual(get_jsondata(r)['data'][0]['stu_name'], 'aaa')
        res = execute_sql("select * from hello_student where stu_id=1;")
        if 'aaa' in res:
            print('查到了!')

if __name__ == '__main__':
    unittest.main()
import unittest,time
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 实例化TestSuite类, 把测试方法组织成测试套件
    # discover()是TestLoader类当中的一个方法, 从特定的开始目录,发现和返回所有的测试模块, 递归的查找测试模块和模块中的测试方法, 这些测试模块必须满足设定的正则表达式.
    suite = unittest.defaultTestLoader.discover('./day8/',pattern='test_*.py')

    # 实例化HTMLTestRunner类,调run方法运行测试套件中的测试方法
    file_path = time.strftime('%Y%m%d_%H')
    with open(f'./day8/report/{file_path}.html','wb') as f:
        runner = HTMLTestRunner(stream=f,title='海盗电商自动化测试',description='测试了登录注册,账号地址等模块')
        runner.run(suite)
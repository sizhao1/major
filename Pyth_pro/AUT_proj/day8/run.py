# import unittest
# from HTMLTestRunner import HTMLTestRunner
#
# if __name__ == '__main__':
#     # TestSuite组织测试用例
#     # 第一种方式: 繁琐,每个测试方法写一次添加,不用
#     # suite = unittest.TestSuite()
#     # suite.addTest(TestReg("test_reg_failed"))
#     # suite.addTest(TestAccount("test_member_address"))
#
#     # 第二种方式: 需要把测试的类进行添加,就可以自动搜索类下面的要测试的方法. 也不常用, 自动化每添加一个类,就必须添加一条代码,还是比较麻烦.
#     # suite = unittest.TestSuite()
#     # suite.addTest(unittest.makeSuite(TestReg))
#     # suite.addTest(unittest.makeSuite(TestAccount))
#
#     # 第三种方式: 自动探索发现要测试的模块(只要这个模块符合正则,就自动添加进来),通过模块去搜索模块下的类,再把要测试的类底下的测试方法添加进来
#     suite = unittest.defaultTestLoader.discover('./',pattern='test_*.py')
#
#     # # TextTestRunner类去运行
#     # with open('./report/1.txt','w') as f:
#     #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
#     #     runner.run(suite)
#
#     # 优化TestRunner部分, 第三方模块: HTMLTestRunner
#     with open('./report/1.html','wb') as f:
#         runner = HTMLTestRunner(stream=f,verbosity=2,title='自动化测试结果一览',description='测试海盗电商的模块: 登录/注册/会员中心/账号信息')
#         runner.run(suite)


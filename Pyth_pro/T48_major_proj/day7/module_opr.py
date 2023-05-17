'''
模块: 一个py文件就是一个模块.
内建模块:  不需要导入, 我们创建模块的时候,会自动导入内建模块.
其它模块或第三方模块(包):  需要导入,
第三方模块: 需要下载,安装, 在线下载和离线下载. pip工具
from ... import ... :从 包名.模块名 导入 函数或类或(变量)属性
import...  :导入包名.模块
from ... import * :从模块导入模块中所有的函数/类/变量
from ... import 类名 as 新类名: 给原来的类名起了个别名, 只能用别名.
导入自己写的模块: 使用相对路径的概念去导.
./ 表示当前路径, 可以省略不写
../ 返回上一级路径
'''
# import keyword
import random
# from random import *
# import math
# from selenium.webdriver.common.keys import Keys
from keyword import kwlist
# import selenium.webdriver.common.keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait as wdw
# from day6.lx import card_play
# import sys
# print(kwlist)
# print(randint())
# print(choice())
# print(sample())
# card_play()
# print(sys.path)

# 一个学校有三个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
# 要求: 每个办公室分配的老师不能超过3个.
# teachers = ['a','b','c','d','e','f','g','h']
# lis = [[],[],[]]
# for i in lis:
#     num = 3
#     if len(teachers)<3:
#         num = len(teachers)
#     li1 = sample(teachers,num)
#     i.extend(li1)
#     for j in li1:
#         teachers.remove(j)
# print(lis)

# li1=["办公室1","办公室2","办公室3"]
# li2=["老师1","老师2","老师3","老师4","老师5","老师6","老师7","老师8"]
# dic={"办公室1":[],"办公室2":[],"办公室3":[]}
# for i in li2:
#     for j in li1[:]:
#         if len(dic[j]) == 3:
#             li1.remove(j)
#     s = choice(li1)
#     dic[s].append(i)
# print(dic)


# dic = {'办公室1':[],'办公室2':[],'办公室3':[]}
# for k in dic.keys():
#     num = 3
#     if len(teachers)<3:
#         num = len(teachers)
#     li = sample(teachers,3)
#     dic[k].extend(li)
#     for i in li:
#         teachers.remove(i)
# print(dic)

# techer=[1,2,3,4,5,6,7,8]
# jieguo={'class1':[],'class2':[],'class3':[]}
# li=list(jieguo.keys())
# for i in range(1,9):
#         jieguo[random.choice(li)].append(i)
#         for k,v in jieguo.items():
#                 if len(v)==3:
#                         li.remove(k)
# print(jieguo)









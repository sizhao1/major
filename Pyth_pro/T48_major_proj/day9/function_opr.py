'''
函数:
定义:
语法格式:
帮助的写法:
\'''函数的帮助\'''
def 函数名(参数1,参数2,...):
    执行逻辑语句

光有定义,不调用的话,永远都不会执行

帮助文档:
help()函数来查看, 函数里的帮助文档.

调用:
ret = 函数名(参数1,参数2,...)
关心两个部分:  参数, 返回值
sum() : 传入itreable的数据结构(字符串,列表,元组,字典), 输出的返回值是元素的累加值.
调用过程:
1.解释器遇到函数的定义,不会执行
2.解释器遇到函数的调用, 会打断点, 从断点处出发去调用函数的定义
3.先进行按位置传参.
4.执行函数定义中的执行语句
5.执行完毕,返回到断点,如果定义中返回值,带返回值返回,如果没有返回值,返回None.
6.代码顺序往下执行

函数的参数:
参数都是写在()中.
在函数定义中叫形参.
在函数调用中叫实参.

参数传递:
从调用往定义传.
(1).按位置传参: 形参和实参的位置必须一一对应.
(2).按名字传参: 实参传参时,以名值对的方式来传, 名=值. 现在就按名字来传,和位置无关.
要求: 实参名必须和形参的名字一一对应, 必须要写对.
(3).默认值传参:  规定: 非默认值参数必须放在默认值参数的前面,最后是默认值参数.
形参给定默认值,形参就可以根据实际情况,需要重新赋值呢,实参就传值,不需要就不传了.

返回值:
return: 关键字, return后面跟的内容会在函数定义调用完毕的时候,返回给函数调用.
例:
return 1
return 1,2,3

定义的原则:
原子化原则: 函数一次只定义一个功能.不要一个函数定义多个用途.

函数的嵌套调用: 从哪里打断点调用函数定义的,返回到哪里.
print(sum([1,3,5])): 先执行的是内层函数: sum([1,3,5]), 再执行外层函数: print()
'aaa'.strip().upper(): 'aaa'字符串先执行strip()去空格, 再执行upper()进行大写.

局部变量: 定义在函数内部的变量, 生命周期会随着函数定义执行完毕而结束.
全局变量: 定义在函数外部的变量, 生命周期只有当整个软件运行结束,才结束.
tips: 当函数内部有和全局变量同名的局部变量时, 函数内部使用的是局部变量.
局部变量优先级>全局变量.
如果在函数内部想要修改全局变量的值, 必须用global关键字去申明.

在函数中修改全局变量值时:
1.全局变量的数据类型是可变还是不可变
2.根据类型来确定怎么修改
'''
from random import *

# # 定义两个数的加法
# def add(num1,num2):  #形参
#     '''这是一个两个数的加法运算,用户可以输入两个数值,这个函数负责进行运算,并将结果返回.'''
#     print('num1是:',num1)
#     print('num2是:', num2)
#     res = num1+num2
#     return res

# print(help(add))
# print(add(67,3))      #实参
# print(add(3,67))      #实参
# print(add(num1=22,num2=33))
# print(add('23','4'))  #实参

# res = sum([1,2,3,77,88,9])
# print(res)
# print(help(print))

# def save_user_info(name,age,sex='女'):
#     dic = {'name':name,'age':age,'sex':sex}
#     return dic
#
# d = save_user_info('王伟',20)
# print(d)

# 1.写一个函数打印一条横线
# def print_a_line(num):
#     print('-'*num)
#
# print_a_line(80)
# 2.打印自定义行数的横线
# def print_n_line(num,n):
#     for i in range(n):
#         print('-'*num)
# print_n_line(80,7)
# a = 13
# b = 26
# def aaa():
#     # 局部变量: 定义在函数内部的变量, 生命周期会随着函数定义执行完毕而结束.
#     # a = 3
#     # b = 9
#     global a,b
#     a = 23
#     b = 53
#     return b/a
#
# print(aaa())
# print(a)
# print(b)

# a = [1,2,3]
# b = [3,5,7]
# def bbb():
#     a.append(33)
#     b.extend([11,22,33])
#     return len(a),len(b)
#
# print(bbb())
# print(a)
# print(b)

# # 6.编写“学生管理系统”，要求如下：
# # 学生信息至少包含：姓名、年龄、性别, 学号等，除此以外可以适当添加
# # 必须完成的功能：添加、删除、修改、查询、退出
# # **********************************
# # 请选择你要做的操作:
# # 1.添加
# # 2.删除
# # 3.修改
# # 4.查询
# # 5.退出
# # **********************************
# stu_li = [{'name':'小花','age':'18','sex':'女','sid':'sid001'},
#           {'name':'小明','age':'19','sex':'男','sid':'sid002'},
#           {'name':'小田','age':'20','sex':'男','sid':'sid003'}]
#
# # 作用: 仅打印出前端功能页面
# def print_oper():
#     print('''**********************************
# 请选择你要做的操作:
# 1.添加
# 2.删除
# 3.修改
# 4.查询
# 5.退出
# **********************************''')
#     select = input('请输入你的选择:')
#     return select
# # 后端功能实现
# def add_a_student():
#     name = input('请输入学生姓名:')
#     age = input('请输入学生年龄:')
#     sex = input('请输入学生性别:')
#     sid = input('请输入学生学号:')
#     dic = {'name':name,'age':age,'sex':sex,'sid':sid}
#     stu_li.append(dic)
#
# def delete_a_student(sid):
#     for i in stu_li:  #{'name':'小花','age':'18','sex':'女','sid':'sid001'}
#         if i['sid'] == sid:
#             stu_li.remove(i)
#             break
#     else:
#         print('查无此人!')
#
# def modify_a_student(sid,k,v):
#     for i in stu_li:
#         if i['sid']==sid:
#             i[k] = v
#             break
#     else:
#         print('查无此人!')
#
# def find_a_student(sid):
#     for i in stu_li:
#             if i['sid']==sid:
#                 print(i)
#                 break
#     else:
#         print('查无此人!')
#
# def student_management_system():
#     while True:
#         sel = print_oper()
#         if sel == '1':
#             add_a_student()
#         elif sel=='2':
#             sid = input('请输入要删除的学生的学号:')
#             delete_a_student(sid)
#         elif sel=='3':
#             sid = input('请输入要修改的学生的学号:')
#             k = input('请输入要修改的项的名称:')
#             v = input('请输入要修改的项的值:')
#             modify_a_student(sid,k,v)
#         elif sel=='4':
#             sid = input('请输入要打印的学生的学号:')
#             find_a_student(sid)
#         elif sel=='5':
#             print('Bye!')
#             break
#
# # main函数是任何程序的入口函数
# if __name__ == '__main__':
#     student_management_system()

# 4 编程：日期计算：输入某年某月某日，判断这一天是这一年的第几天？
# 1).程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第 几天， 特殊情况，闰年且输入月份大于3时需考虑多加一天。
# 2).如果输入的月份大于12时提示错误，重新输入
# 3).如果月份为小月，天数大于30时提示错误，重新输入
# 4).如果月份为大月，天数大于31时提示错误，重新输入
# 5).如果年份为平年，2月天数大于28时提示错误，重新输入
# 6).如果年份为闰年，2月天数大于29时提示错误，重新输入
# li = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# year = int(input('请输入年(世纪年XXXX):'))
# month = int(input('请输入月(XX):'))
# day = int(input('请输入日(XX):'))
# # 判断月份的对错
# def is_month_right():
#     if 12>=month>0:
#         return True
# # 判断日期的正确性
# def is_day_right():
#     if li[month]>=day>0:  # 2月29  li[2]
#         return True
# # 计算年
# def calculate_year():
#     if (year%4==0 and year%100!=0) or (year%400==0):
#         return True
# # 修正月份的列表
# def modify_month(yeap):
#     if yeap:
#         li[2] = 29
# # 计算月
# def calculate_month():
#     total_day = 0
#     for i in range(month):  #3--0 1 2
#         total_day += li[i]
#     return total_day
#
# # 计算日
# def calculate_day(total_day):
#     total_day += day
#     print('这一天是这一年的第%d天'%total_day)
#
# if __name__ == '__main__':
#     is_leap_year = calculate_year()
#     modify_month(is_leap_year)
#     if is_month_right() and is_day_right():
#         t_day = calculate_month()
#         calculate_day(t_day)
#     else:
#         print('月份或日期错误,请检查!')

'''
16.一年一度的校园好声音进行到了激烈的决赛环节，8位评委对入围的6名选手依次给出最终的评分，
01.请写程序记录评委的打分.请根据评分表
02.将每位选手的得分去掉一个最高分和一个最低分后求平均分
03.按照平均分由高到低的顺序输出选手编号和最后得分。
'''
li = [[],[],[],[],[],[]]   #可变数据类型
# 保存评委的打分
def save_scores():
    for i in range(6):
        for j in range(8):
            score = randint(80,100)
            li[i].append(score)
# 处理选手的得分
def deal_with_scores():
    for i in range(len(li)):  #[97, 97, 82, 98, 97, 91, 92, 87]
        li[i].remove(max(li[i]))
        li[i].remove(min(li[i]))

# 求每个选手的平均分
def get_avg_score():
    dic = {1:None,2:None,3:None,4:None,5:None,6:None}
    for i in range(len(li)):  #[92, 84, 83, 88, 94, 100]
        total = sum(li[i])
        avg_score = total/len(li[i])
        dic[i+1] = round(avg_score,2)
    return dic
# 选手得分排序
def sort_score(dic):  #{1: 93.0, 2: 84.67, 3: 92.17, 4: 93.5, 5: 90.33, 6: 91.33}
    li = []
    for k,v in dic.items():
        li.append(v)
    li.sort(reverse=True)
    print(li)
    for i in range(len(li)):
        for k, v in dic.items():
            if li[i]==v:
                print('第%d名是:选手%d,得分是%.2f'%((i+1),k,v))

# if __name__ == '__main__':
#     save_scores()
#     print(li)
#     deal_with_scores()
#     print(li)
#     dic = get_avg_score()
#     print(dic)
#     sort_score(dic)

# 函数部分:
# 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#    print(a,b)
# c = test5(20,10)
# print(c)
#
# # 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
d=10
b=20
def test5(a,b):  #a,b = 20,10
   global d
   d=3
   b=5
   return b
c = test5(b,d) #b,d = 20,10
print(c)  #5
print(d)  #3
print(b)  #20

# a,b = 3,4
# def aaa():




'''
判断结构:
特殊结构, 判断不管写多长,都只是一条语句, 判断里只要有一种条件(if,elif,else)满足了,其它的就不会被执行.

单if结构:
if 条件语句:
    执行语句

条件语句: 一般由能直接运算出bool值结果的表达式或变量等构成.
if后跟的条件语句,结果为True, 执行语句会被执行,否则不执行. if判断整个只是一条语句.
单if解决的是,只需要判断/提示一种情况.

if...else...
如果...否则...
语法:
if 条件语句:
    执行语句1
else:
    执行语句2

if...elif...elif...else
如果 某一种情况,怎么样,另一种情况,怎么样,再一种情况,怎么样,再...,否则,怎么样.
语法:
if 条件语句:
    执行语句1
elif 条件语句:
    执行语句2
...
else:
    执行语句N

嵌套判断:
    一般外层做有效性判断, 内层做具体的实现的逻辑.
'''
from random import randint
# a = 12
# if 1==1 or 2>3:
#     print('if条件成立')
#     print(11)
#     print(222)
#     print(333)
#     print(a)

# 猜数字：设计一个程序，计算机随机出一个100以内的数值，让用户猜这个值是多少.
# num = randint(1,10)
# guess = int(input('请输入猜的数(1-10):'))
# if num==guess:
#     print('恭喜你,猜对了!')

# num = randint(1,10)
# guess = int(input('请输入猜的数(1-10):'))
# if num==guess:
#     print('恭喜你,猜对了!')
# else:
#     print('没猜对!')

# 1：a和b都是计算机随机产生,1-10的整数.
# 如果a<b，进行加法运算，否则进行减法运算
# num1 = randint(1,10)
# num2 = randint(1,10)
# if num1<num2:
#     print(num1,num2,num1+num2)
# else:
#     print(num1,num2,num1-num2)

'''
设计登录，如果用户名和密码正确，提示登录成功，否则提示登录失败
username = 'admin'
password = 'Pass1234'
'''
# username = 'admin'
# password = 'Pass1234'
# name = input('请输入你的用户名:')
# pwd = input('请输入你的密码:')
# if name == '' or pwd == '':
#     print('输入的用户名或密码为空,无效!')
# else:
#     if name == username and pwd == password:
#         print('亲爱的%s,恭喜你,登录成功!'%name)
#     else:
#         print('用户名或密码错误,登录失败!')

'''
3.要求用户输入学生的分数，输入的分数在0-100范围内：如果分数在90分或以上，打印优秀；如果分数在80分或以上且在90以下，打印中；如果分数在60分以上且在80以下，打印一般；如果分数低于60分，打印不及格
'''
# score = float(input('请输入你的分数(0-100):'))
# if score>=0 and score<=100:
#     if score>=90:
#         print('优秀')
#     elif score>=80:
#         print('中')
#     elif score>=60:
#         print('一般')
#     else:
#         print('不及格')
# else:
#     print('输入的分数无效!')

'''
5.输入上年CPI指数,CPI范围一般在0-50之间,若CPI>10,提示"物价过高,无法生活",若CPI在7-10之间,提示"物价很高,生活非常不易",若CPI在4-7之间,提示"物价高,生活不易",若CPI在2-4之间,提示"物价还行,可以接受",小于2,提示"物价便宜,生活舒适"
'''
# cpi = float(input('输入CPI(0-50)'))
# if cpi>=0 and cpi<=50:
#     if cpi>=10:
#         print('物价过高,无法生活')
#     elif cpi>=7:
#         print('物价很高,生活非常不易')
#     elif cpi>=4:
#         print('物价高,生活不易')
#     elif cpi>=2:
#         print('物价还行,可以接受')
#     else:
#         print('物价便宜,生活舒适')
# else:
#     print('无效数据!')

# 3.猜数字游戏, 计算机先定义好一个1-100的随机整数.然后让用户去猜,一共给予5次猜的机会,每次提示用户是猜大了还是猜小了,猜对结束,猜错5次,机会用完.
# num = randint(1,100)
# guess = int(input('请输入您猜的值:'))
# if guess>num:
#     print('大了!')
# elif guess<num:
#     print('小了!')
# else:
#     print('猜对了!')



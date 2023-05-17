'''
数值型数据:
int: 整数
float:小数

运算: + - * / // % **
复合运算:
运算符	描述	实例
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a

比较运算符:
==:  相等比较.   3==3-->True     3=='3'-->False
!=:  不等比较.   3!=3-->False
>:   大于比较.
<:   小于比较.
>=:  大于等于比较.
<=:  小于等于比较.
一般用作判断.

逻辑运算符:
and: 逻辑与   操作符前后的表达式必须都为True,结果才为True
or: 逻辑或   操作符前后的表达式有一个为True,结果就为True
not: 逻辑非   操作符后面只跟一个操作数或表达式, 对这个操作数或表达式的结果去反.

特殊数值:
数字0、空字符串、空值None、空集合都被认为是False,其他的值都认为是True.
'''

a,b,c = 10,20,5
# a+=b
# print(a)  #30

# a*=c
# print(a) #150

# b//=c  #b=b//c
# print(b) #4

# c**=b
# print(c) #625

# print(3==3)
# print(3=='3')

# print(1>2 and 2<3)  #False
# print(1<2 and 2<3)  #True

# print(1>2 or 2<3)  #True
# print(1<2 or 2<3)  #True
# print(1>2 or 2>3)  #False
#
# print(not 2>3) #True
# print(not 2<3) #False

print(not 0) #True
print(not '') #True
obj = None
print(not obj) #True
tup = []
print(not tup) #True
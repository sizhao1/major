'''
数据类型:
四种基础数据类型:
int: 数值型数据里的整数数据类型.     ------>处理除小数外的数据
float: 数值型数据里的小数数据类型.   ------>购物,金额,金钱等计算
str: 字符串.                      ------>人机交互
内容一定要包在'',"",''''''.
bool: 布尔类型.(只有两个值0--False和1--True)  ------>判断
程序当中, 最重要的是处理数据.

字符串:    -----人机交互
书写方式: 以单引,双引,三引来开始,以对应的单引,双引,三引来结束.
单引,双引表示单行,三引表示多行.
用来表示一句话, let's go!

print()函数两个参数:
sep=' ': 分割参数,用来指定输出函数的值和值之间的分割
end="\n": 结束参数,用来指定输出函数最后一个值和下一个print之间的结束符号.

\为转义字符,可以去掉符号的特殊含义:
\n: 换行输出, \\n:不具备特殊含义.
let': 在字符串中,可能会结束掉字符串, \': 去掉'结束字符串的特殊含义.
转义字符	描述
\	反斜杠符号,\可以做路径分割符,也可以和其它的字母结合具有特殊含义.
’	单引号
”	双引号
\n	换行
\t	横向制表符,横向产生四个空字符,与敲’Tab’键效果一样
\v	纵向制表符,纵向产生四个空字符
\r	回车,
\b(backspace)	退格(Backspace)
r:在字符串前使用字母r,表示原样输出.

字符串的格式化:
字符串里面有一部分内容是固定,另一部分是变化的. 可以用格式化来表示变化的这部分.
格式化的符号:
%d: 表示int型的数据.
%f: 表示float型的数据.
%s: 表示str型的数据.
替换: %后用真实的值或变量或算式去替换.
格式化符号:
%f: 添加一些修饰.  
%[(name)][flags][width].[precision]typecode: 最重要的是typecode,数据类型的编码, f代表的是float型,d代表的是int型,s代表的是str型.
.[precision]: 精度,表示的是小数点后保留几位.
[width]:宽度, 指的是数据总的长度.
[flags]:标识位, 
+: 正数做个正号标识,默认是右对齐,不足的宽度用空格填充.
-: 代表是左对齐.
0: 右对齐,不足的宽度用0填充.
[(name)]: 起名.
f:字符串前写f,表示的也是字符串的格式化. f'123{num}456'
'''
tips1 = '今天是星期一,困难的一天!'
tips2 = "今天是星期二,忙碌的一天!"
tips3 = '''
今天是星期三, 这周已经过一半了,很开心!
今天是星期三, 这周已经过一半了,很开心!
今天是星期三, 这周已经过一半了,很开心!
'''
# print(tips1,tips2,tips3)
word = "let's go"
# print(1,2,3,4,5,6,sep="@",end="################################")
# print(7,8)

'''
小练习：使用print()函数输出“Hello World！HZDL{3}”
1)word!后换行输出
2)不换行输出
3)把数字3和其它部分用|隔开
4）用两种方式将let’s go 打印输出
5）输出c:\note.txt
'''
# print ('''Hello World!
# HZDL{3}''')
# print("Hello World！HZDL{3}")
# print("Hello World!HZDL{",3,"}",sep = '|')
# print('''let’s go''')
# print("let","s go",sep='’')
# print('let\'s go')
# print('c:\\note.txt')

# 转义字符:
# print('1234------')
# print('1234\\n------')
# print('1234\n------')
# print("C:\\Users\CDLX\AppData\Local\Programs\Python\Python36")
# print(r"C:\Users\CDLX\AppData\Local\Programs\Python\Python36")

name = 'admin'
# print('亲爱的%s,你好!'%name)
score = 180000
# print('您本轮的总分是%d'%score)

# name='李潇潇'
# age=23
# sex='女'
print('学生名为:%(name)s,性别为:%(sex)s,年龄为:%(age)d岁'%{'sex':'男','name':'王毅','age':52})

num1 = 25
num2 = 1.7
# print('结果为:%10.2f'%(num1/num2))
# print('结果为:%010.2f'%(num1/num2))
# print('结果为:%+10.2f'%(num1/num2))
# print('结果为:%-10.2f'%(num1/num2))

# 购物车金额打印时:
# total = 1898.56
# discount = 0.9
# print("迎中秋的活动中,您本次消费了%+10.2f元"%total)
# print('折完,您应付%+23.2f元'%(total*discount))
# print("您的折扣是%f"%discount)

num = 190078
# print(f'123{num}456')

# i = 0
# while i<3:
#     xm = input('输入你的姓名：')
#     gs = input('输入你的公司：')
#     zw = input('输入你的职位：')
#     dh = int(input('输入你的电话：'))
#     yx = input('输入你的邮箱：')
#     gz = float(input('输入你的工资：'))
#     print(f'公司名称 :{gs}',f'姓名(职位):{xm}',f'电话：{dh}',f'邮箱：{yx}',f'工资:{gz}')
#     i=i+1


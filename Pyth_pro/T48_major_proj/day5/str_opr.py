'''
字符串:
表示方法: 单引,双引,三引成对表示.

序列:  字符串,列表,元组都属于序列.
索引(下标): 字符串都具有
切片: 字符串都具有

输入函数: input()函数
输出函数: print()函数

不可变数据类型.
查询:
in: 判断某个字符或子串是存在于这个字符串中
not in: 判断某个字符或子串不存在于这个字符串中

遍历:
for一:
for i in 字符串:
    #i 表示的是 字符串里顺序取到的每个字符
    执行语句

for二:
for i in range(len(字符串)):
    #i 表示的是 字符串中的索引下标
    #字符串[i] 表示的是 字符串中的取到的字符值
    执行语句

特有函数：
<1>len() (***)
len(object)
返回元素在列表，元祖，字符串中的元素个数。

<2>find（）  (**)
检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则（找不到）返回-1
mystr.find(str, start=0, end=len(mystr))
index（）：不友好，如果找不到，程序就崩溃退出。

<4>capitalize（）
把字符串的第一个字符大写, 首字母大写。
mystr.capitalize()
title（）： 字符串中的每个单词都大写。

<5>startswith()
检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
mystr.startswith(obj)

<6>endswith()
检查字符串是否以obj结束，如果是返回True,否则返回 False.
mystr.endswith(obj)

<7>lower()
转换 mystr 中所有大写字符为小写
mystr.lower()

<8>upper()
转换 mystr 中的小写字母为大写
mystr.upper()

--------------------------------------------------------------------
<9>strip
删除mystr字符串两端的空白字符
mystr.strip()

<10>isalpha
如果 mystr 所有字符都是字母 则返回 True,否则返回 False
mystr.isalpha()

<11>isdigit
如果 mystr 只包含数字则返回 True 否则返回 False.
mystr.isdigit()

<12>isalnum
如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
mystr.isalnum()

-------------------------------------------------------------------
<3>split（***）
以 sep 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
mystr.split(sep, maxsplit)

<13>join(***)
mystr 中每个字符后面插入str,构造出一个新的字符串
mystr.join(str)

<14>replace()
可以对字符串中的部分子串进行替换,替换后在内存中保存了新的字符串.

<15>format()
格式化函数,把指定的{}格式化成设定的内容.
'''

s1 = 'abcdefghrtyuio'
# print(s1[8]) #'r'
# print(s1[-8:-3]) #'ghrty'
# print(s1[:])  #'abcdefghrtyuio'
# print(s1[::-1]) #倒序

s2 = 'abc'
# print(s2 in s1) # 'abc' in 'abcdefghrtyuio'--->True
# print(s1 in s2) # 'abcdefghrtyuio' in 'abc'--->False

# 取出其中的星期几的描述?把首个单词取出来？判断今天是不是星期五？
s1 = 'Today is Monday!'
# print(s1[-7:-1])
# print(s1[:5])
# print('Friday' in s1)

# s = 'abcdefghijklmnopqrstuvwxyz',挨个打印字符串中的字符，遇到m结束打印？跳过m，继续打印？遇到m，改成#？
s = 'abcdefghijklmnopqrstuvwxyz'
# for i in s:
#     if i=='m':
#         # break
#         continue
#     print(i)

# 由于字符串是不可变数据类型，所以报错：
# TypeError: 'str' object does not support item assignment
# for i in range(len(s)):
#     if s[i]=='m':
#         s[i] = '#'
#     print(s[i])

# print(s.find('n')) #13
# print(s.index('n')) #13
# print(s.find('abn')) #-1
# print(s.index('abn')) #没找到，崩溃退出

# s1 = 'abc@der@abn@aaa@efr'
# inx = s1.find('ab')
# print(s1.find('ab',inx+1,len(s1)-1))

# phgraph = 'mom said:"lily is a nice and beatiful girl!"'
# print(phgraph.capitalize())
# city_str = 'beijing xian nanjing shanghai'
# print(city_str.title())

s1 = 'today is monday!'
s2 = 'today is hot'
s3 = 'lily is a girl!'
# 1.要求三个句子必须语法正确,保留语法正确的句子。
# li = [s1,s2,s3]
# for i in li[:]:
#     li.append(i.capitalize())
#     li.remove(i)
# print(li)

# 2.判断每个字符串是否以today开头，是否以！结尾
# for i in li:
#     if i.lower().startswith('today') and i.endswith('!'):
#         print(i)

li = ['sElect * from sc where id=1','Select * from sc where id=2','update sc set a=1 where id=3','delete from sc','SELECT * from sc where id=4']
# 挑出其中的查询语句，并打印出来
# for i in li:
#     if i.upper().startswith('SELECT'):
#         print(i)

# 7.想办法将字符串'aldous Huxley was born in 1894.'的第一个字符大写,从而使语法正确
# s = 'aldous Huxley was born in 1894.'
# s = s.capitalize()
# print(s)
# 8.找到字符串"Hemingway"中字符"m"所在的第一个索引
# s = "Hemingway-MadMin-mOff-mIff"
# cont = s.count('m')
# for i in range(cont):
#     if i==0:
#         idx = s.find('m')
#     else:
#         idx = s.find('m',idx+1,len(s))
#     print(idx)
#
# a = "Hemingway-MadMin-mOff-mIff"
# lis = []
# for i in range(len(a)):
#     if a[i].lower()=='m':
#         lis.append(i)
# print(lis)

# count = 0
# for i in s:
#     if i.isupper():
#         count+=1
# print(count)

# usr = ' admin  '
# pwd = ' 123456'
# if usr.strip()=='admin' and pwd.strip() == '123456':
#     print('登录成功!')
# else:
#     print('登录失败!')

# s = 'adm1223'
# print(s.center(15))
# print(s.ljust(15))
# print(s.rjust(15))

def is_other_word(pwd3):
    for i in pwd3:
        if 0<=ord(i)<=127:
            if not(i.isdigit() or i.isupper() or i.islower()):
                print(i,'这个是符号')
                return True
#密码如果全为字母,或数字,密码强度为弱,如果密码既有数字,又有字母,强度为中,如果既有数字,又有字母,还有符号,强度为强.
# pwd1 = 'atomy'
# pwd2 = 'P123456'
# pwd3 = 'as1234_1'
# if pwd3.isalpha() or pwd3.isdigit():
#     print('密码强度弱!')
# elif pwd3.isalnum():
#     print('密码强度为中!')
# elif is_other_word(pwd3):
#     print('密码强度为强!')

s = 'today is monday!'
#切割函数, 会把一个字符串切成几个部分. 默认切割的分割符为空格.
li = s.split()
# print(li)
li[2] = 'friday!'
# print(li)

# 列表转回字符串, join()
s = ' '.join(li)
# print(s)

# 随机输入三个同学的姓名,语文成绩,数学成绩,英语成绩,用字符串保存结果,
# 计算该同学的总分,平均分,并保存在原字符串中
# 保存三个同学的成绩:
# li = []
# for i in range(3):
#     s = input('请输入学生姓名,语文成绩,数学成绩,英语成绩,用空格分开:')
#     li.append(s)
#
# li2 = []
# for i in li[:]:
#     li1 = i.split() #'张三 80 90 55'-->['张三','80','90','55']
#     total = float(li1[1])+float(li1[2])+float(li1[3]) #225
#     avg = total/3
#     li1.append(str(total))
#     li1.append(str(avg)) #['张三','80','90','70','240','80.00']
#     s = ' '.join(li1) #'张三 80 90 70 240 80.00'
#     li.append(s)
# print(li)

# 6.编写程序,从用户处获取两个字符串,将其插入字符串'Yesterday I wrote a [用户输入1]. I sent it to [用户输入2]!'中,并打印新字符串
# s = 'Yesterday I wrote a {}. I sent it to {}!'
# s1 = input('请输入一个单词:')
# s2 = input('请输入第二个单词:')
# print(s.format(s1,s2))
# print(f'i sent it to {s2}')

# 9.将字符串"A screaming comes across the sky."中所有的"s"字符替换为美元符号.
# s = "A screaming comes across the sky."
# s1 = s.replace('s','$')
# print(s1)

'''
2.根据完整路径从路径中分离文件路径，文件名及文件扩展名
注意python中一个反斜杠有特殊含义，所以要用二个反斜杠
str2 = "D:\\软件\python\\python39\\Tools\scripts\\abitype.py"
'''
# str2 = "D:\\软件\python\\python39\\Tools\scripts\\abitype.py"
# li1 = str2.split('.')
# print('文件扩展名为:',li1[1])
# li2 = str2.split('\\')
# print('文件名为:',li2[-1].replace('.py',''))
# print('文件路径为:',str2.replace('\\'+li2[-1],''))

# 1.str = "today is a good day",去掉字符串所有的空格,并使用@进行连接,使其变成这个字符串'today@is@a@good@day'
s1 = "today is a good day"
# li = s1.split()  #['today','is','a','good','day']
# s = '@'.join(li)  #
# print(s)
# s = s1.replace(' ','@')
# print(s)

# 3.把字符串数组中每个字符串的good替换为nice.
# ls=["today is a good day","my english is good","i love you"]
# for i in range(len(ls)):
#     if 'good' in ls[i]:
#         s = ls[i].replace('good','nice')
#         ls[i] = s
# print(ls)





















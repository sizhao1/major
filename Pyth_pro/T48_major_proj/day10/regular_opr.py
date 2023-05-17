'''
正则表达式:
其它模块,需要导包
import re
使用findall()函数来查找.
findall(): 两个参数, 1-->规则, 2-->字符串.

元字符
1.以子串为规则来找
2.以^+子串为规则来找(如果找到,表明字符串以子串开头的)
3.以子串+$为规则来找(如果找到,表明字符串以子串结尾的)
4.以字母+?为规则来找(?只能匹配它前面的一个字母0-1次)
5.以字母+加号为规则来找(+只能匹配它前面的一个字母1-多次)
6.以字母+*为规则来找(*只能匹配它前面的一个字母0-多次)
7.[...]可以规定一个字符的变化,可以是全大写,全小写,全数字,或者混合(|).
8.{最小,最大}可以规定它前面一个字符出现的次数,只要在最小和最大之间,就符合规则.

例9：预定义字符集（可以写在字符集[...]中）
字符 意思                              表达式  结果
\d   表示数字：[0-9]                    a\dc    a1c
\D   表示非数字：[^\d]                  a\Dc    abc
\s   表示空白字符：[<空格>\t\r\n\f\v]   a\sc    a c
\S   表示非空白字符：[^\s]              a\Sc    abc
\w   单词字符：[A-Za-z0-9_]              a\wc    abc
\W   非单词字符：[^\w]                  a\Wc    a c
'''
import re

# 例1：检索字符串中所有的hzdl子串并以列表的形式返回，这个会经常用到计算同一字符出现的次数
str1 = "hello hzdl, this is xa's hzdl, welcome to xahzdl!"
# lis = re.findall('hzdl',str1)
# print(lis)

# 例2：使用符号^表示匹配以hell开头的的字符串返回,也可以判断字符串是否以hell开始的
# li = re.findall('^helo',str1)
# print(li)

# 例3：使用符号$符号表示以hzdl！结尾的字符串返回,也可以判断字符串是否以hzdl！结束
# li = re.findall('hzdl!!$',str1)
# print(li)

# 例4：使用符号？表示它前面一个字母可匹配0-1次的结果
str2 = "ben been b beeeeeeeeen beeeen block bark bn"
li = re.findall('be?n',str2)
print(li)

# 例5：使用符号+表示它前面一个字母可匹配1-多次的结果
# li = re.findall('be+n',str2)
# print(li)

# 例6：使用符号*表示它前面一个字母可匹配0-多次的结果
# li = re.findall('be*n',str2)
# print(li)

# 例7：[...]的意思匹配括号内的值则返回列表
str3 = "hzdl, hZdl, h2dl, h中dl, hadl, hddl, hRdl, h8dl"
# li = re.findall('h[a-z|A-Z|0-9]dl',str3)
# print(li)

# 例8：{最小，最大}的意思匹配{}前的字符的次数只能在最大和最小之间
str4 = "ho heo helo hello helllo hellllllllllllo heao hebo herrro hebbbbbbbbbbbbbbo"
# li = re.findall('he[a-z]{0,20}o',str4)
# li = re.findall('he[a-z]{3}o',str4)
# print(li)

'''
例9：预定义字符集（可以写在字符集[...]中）
字符 意思                                       表达式  结果
\d   表示数字：[0-9]                            a[\d]c    a1c
\D   表示非数字：[^\d]   ^在[]中是取反的含义     a\Dc    abc
\s   表示空白字符：[<空格>\t\r\n\f\v]           a\sc    a c
\S   表示非空白字符：[^\s]                      a\Sc    abc
\w   单词字符：[A-Za-z0-9_]                     a\wc    abc
\W   非单词字符：[^\w]                          a\Wc    a c
'''
# li = re.findall('h\ddl',str3)
# print(li)
# li = re.findall('h\Ddl',str3)
# print(li)

# str5 = '我有一个中国梦, 梦里有个小愿望!\t'
# # li = re.findall('\s',str5)
# # print(li)
# li = re.findall('\S',str5)
# print(li)

# usrname = 'admin1122中_-!AAA:)'
# li = re.findall('\w',usrname)
# print(li)
# li = re.findall('\W',usrname)
# print(li)

# phone = input('请输入你的手机号:')
# # if len(phone) == 11:
# #     if phone.isdigit():
# #         if phone.startswith('1'):
# #             if phone[1] not in '012':
# #                 print('这是一个手机号!')
#
# if re.findall('^1[3-9][\d]{9}$',phone):
#     print(phone,'是一个手机号!')
# else:
#     print('不是一个手机号!')

# 练习3: My_str =“123 I like 456 chinese J ^&* ”,把数字和字母和其它字符分开,所有字母组成一个新的字符串
# My_str ="123 I like 456 chinese J ^&*"
# li1 = re.findall('[\d]',My_str)
# li2 = re.findall('[a-z|A-Z]{1,10}',My_str)
# li3 = re.findall('\W',My_str)
# print(li1,li2,li3)
# print(' '.join(li2))

# 密码: 6-16位, 可以包含大写字母,小写字母,数字,中文,_,其它的不可以包含,至少是三者混合,不能以数字开头,不能以_开头,不能以中文开头.
# pwd = input('请输入密码:')
# if 16>=len(pwd)>=6:
#     if re.findall('[a-z|A-Z]+[\d]+[\w]+',pwd):
#         print('密码合法!')
#     else:
#         print('密码不合法!')
# else:
#     print('密码不合法')


# re.split()
# li = re.split('be?n',str2)  :根据规则查找子串,根据找到的子串进行切割,得出切割后的列表.
# print(li)
# re.match()   :在字符串中根据正则规则查找,返回第一个命中的子串对象.
# li = re.match('be?n',str2)
# print(li)
# re.search()  :在字符串中根据正则规则查找,返回第一个命中的子串对象.
# li = re.search('be?n',str2)
# print(li)
# re.compile()  :编译函数, 从正则表达式生成一个正则对象
# re.I  #忽略大小写



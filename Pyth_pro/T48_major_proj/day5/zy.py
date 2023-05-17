# 4.获取字符串中汉字的个数
# a = "我的 English 学的不好"
# '\u4e00' <= 单个中文字符的unicode码 <= '\u9fef'
# a = "我的 English 学的不好"
# cont=0
# for i in a:
#     if i>=u'\u4e00' and i <= u'\u9fa5':
#         cont+=1
# print(cont)

# 5.将字母全部转换为大写或小写
# str3 = "toDay is a Good day"
# print(str3.upper())
# print(str3.lower())
# print(str3)

# 6.书店中对书价格进行调整, 现有列表如下:
# ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
# 每本书价格均上涨3.5元,输出新的记录列表.
# li=['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
# new_li = []
# for i in range(len(li)):
#     li1 = li[i].split() #['简爱','35.0元']
#     new_price = str(float(li1[1][:-1])+3.5)+'元'
#     li1[1] = new_price #['简爱','38.5元']
#     new_li.append(' '.join(li1))
# print(new_li)

# 7.让用户输入一个日期格式如“2008/08/08”，将 输入的日期格式转换为“2008年-8月-8日”。
# d=input('请输入一个日期格式（XXXX/XX/XX）：')
# 做法一:
# li=d.split('/')  #['2008','08','08']
# print('%s年-%s月-%s日'%(li[0],li[1],li[2]))
# 做法二:
# d = d.replace('/','-')
# d = d[:4]+'年'+d[4:7]+'月'+d[7:]+'日'
# print(d)

# 8.接收用户输入的字符串，将其中的字符进行排序(升序)，并以逆序的顺序输出，“cabed"“abcde”,"edcba”。
# s=input('请输入一个字符串：')
# li = list(s)
# li.sort(reverse=True)
# s1=''.join(li)
# print(s1)

# 9.接收用户输入的一句英文，将其中的单词以反序输出，“hello c sharp","sharp c hello”。
# s=input('请输入一句英文：')
# li=s.split()  #['hello','c','sharp']
# print(li[::-1]) #['sharp','c','hello']
# s2=' '.join(li[::-1])
# print(s2)

# 10.从请求地址中提取出用户名和域名http://www.163.com?userName=admin&pwd=123456
s='http://www.163.com?userName=admin&pwd=123456'
# li1=s.split('//')
# li2=li1[1].split('?')
# print('域名为：',li2[0])
# li3=li2[1].split('&')
# li4=li3[0].split('=')
# print('用户名为：',li4[1])
# s1 = s.split('&')[0]
# s2 = s1.split('//')[1] #'www.163.com?userName=admin'
# s3 = s2.split('?')
# print('域名为:',s3[0])
# print('用户名为:',s3[1][-5:])





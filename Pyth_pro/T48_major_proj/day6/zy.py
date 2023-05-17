from random import *
# 0920作业:
# 1.给定n个整数的列表，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出,输出为字典。
li = [3,4,1,2,5,6,7,1,2,3,7,2,6,8,9,0,1,4,7,9,2,3,7,9,1]
# li1 = []
# dic1={}
# dic2={}
# 如果不用集合, 先把列表进行排序, 排完序后手动去重
# lis = sorted(li)
# print(lis)
# new_li = []
# while True:
#     if len(lis) == 0:
#         break
#     else:
#         for i in lis:
#             if lis.count(i)>1:
#                 new_li.append(i)
#                 for j in range(lis.count(i)):
#                     lis.remove(i)
#             else:
#                 new_li.append(i)
#                 lis.remove(i)
# print(new_li)
# 集合, 自动排序和去重
# print(set(li))
# 用字典保存了每个整数以及整数出现的次数,列表保存的是次数
# for i in set(li):
#     dic1[i] = li.count(i)  # {0:1}
#     li1.append(li.count(i))
# print(li1)
# print(dic1)
# # 利用列表来逐步跳出列表中次数最大的,每挑出一个,删一个.
# for i in range(len(li1)):
#     for k,v in dic1.items():
#         if v == max(li1):
#             dic2[k]=v
#     li1.remove(max(li1))
# print(dic2)

# 2.一年一度的校园好声音进行到了激烈的决赛环节，8位评委对入围的6名选手依次给出最终的评分，01.请写程序记录评委的打分.请根据评分表
# 02.将每位选手的得分去掉一个最高分和一个最低分后求平均分
# 03.按照平均分由高到低的顺序输出选手编号和最后得分。
# pj_zcj={}
# for p in range(2):
#     num = 0
#     li = []
#     for i in range(3):
#         pw = float(input('第%d位选手第%d位评委打分:'%((p+1),(i+1))))
#         li.append(pw)
#     li.remove(max(li))
#     li.remove(min(li))
#     for j in li:
#         num += j
#     pj = round(num/len(li),2)
#     pj_zcj[p+1] = pj
# print(pj_zcj)

# 3.列表操作
# 【问题描述】编写程序将列表s=[6,17,81,3,29,12,51,16]中能被3整除的数减2，其他数保持不变,输出变换后的列表。
# 【输出形式】[4，17，79,1,29，10，49,16]
# 用字典统计变化的数,和不变的数.
# li=[6,17,81,3,29,12,51,16]
# # 统计能被3整除的数,顺手减2
# li1 = []
# for i in li:
#     if i%3==0:
#         li1.append(i-2)
#     else:
#         li1.append(i)
# print(li1)
# # 统计变化的数和不变的数:
# dic = {'变化的数':[],'不变的数':[]}
# for i in range(len(li)):
#     if li[i] == li1[i]:
#         dic['不变的数'].append(li[i])
#     else:
#         dic['变化的数'].append(li[i])
# print(dic)

# 4.斗地主, 一共54张牌, 保存在列表中,随机给两个用户各发13张牌. 第一个用户随机出了一张单牌后,判断第二个用户可以出哪些单牌,不能出哪些单牌,保存在字典中,给予用户提示.
# 生成54张牌
# li = ['小王','大王']
# for i in range(1,14):
#     for j in range(4):
#         li.append(str(i))
# print(li)
# # 做下修饰
# for i in range(len(li)):
#     if li[i]=='1':
#         li[i] = 'A'
#     elif li[i]=='11':
#         li[i] = 'J'
#     elif li[i]=='12':
#         li[i] = 'Q'
#     elif li[i]=='13':
#         li[i] = 'K'
# print(li)
# # 随机给两个人发牌,发13张牌
# li_pai = []
# for i in range(2):
#     li1 = sample(li,13)
#     for j in li1:
#         li.remove(j)
#     li_pai.append(li1)
# print(li_pai)
#
# # 单独出两个列表来表示a和b两个人分别的牌:
# a = li_pai[0][:]
# b = li_pai[1][:]
#
# # 第二个人理牌
# dic = {200:[],100:[],50:[],20:[],13:[],12:[],11:[],10:[],9:[],8:[],7:[],6:[],5:[],4:[],3:[]}
# while True:
#     if len(b)==0:
#         break
#     else:
#         if '大王' in b:
#             dic[200].append('大王')
#             b.remove('大王')
#         elif '小王' in b:
#             dic[100].append('小王')
#             b.remove('小王')
#         elif '2' in b:
#             dic[50].append('2')
#             b.remove('2')
#         elif 'A' in b:
#             dic[20].append('A')
#             b.remove('A')
#         elif 'K' in b:
#             dic[13].append('K')
#             b.remove('K')
#         elif 'Q' in b:
#             dic[12].append('Q')
#             b.remove('Q')
#         elif 'J' in b:
#             dic[11].append('J')
#             b.remove('J')
#         else:
#             for i in range(3,11):
#                 if str(i) in b:
#                     dic[i].append(str(i))
#                     b.remove(str(i))
# print(dic)
# # 比较:
# chu_p = choice(a)
# print(chu_p)
# kc_b = []
# if chu_p=="大王":
#     key = 200
# elif chu_p=="小王":
#     key = 100
# elif chu_p=="2":
#     key = 50
# elif chu_p=='A':
#     key = 20
# elif chu_p=='K':
#     key = 13
# elif chu_p=='Q':
#     key = 12
# elif chu_p=='J':
#     key = 11
# else:
#     key = int(chu_p)
# # 比较两个人牌的权重
# for k,v in dic.items():
#     if k>key and len(v)!=0:
#         kc_b.extend(v)
# print(kc_b)

# 5.书店中对书价格进行调整, 现有列表如下:
# ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
# 首先将书和价格分别整理成合理的数据结构,然后给每本书先上涨4元,再打八折,输出最后的在售价格.
# li = ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
# li1 =[]
# dic ={}
# for i in range(len(li)):
#     a = li[i].split()
#     s = a[1][:-1]
#     new_price=round((float(s)+3.5)*0.8,2)
#     a[1] = str(new_price) + '元'
#     str1 = ' '.join(a)
#     li1.append(str1)
# print(li1)
# for i in range(len(li1)):
#     li2 = li1[i].split(' ')
#     dic[li2[0]]=li2[1]
# print(dic)

# 6.编写“学生管理系统”，要求如下：
# 学生信息至少包含：姓名、年龄、性别, 学号等，除此以外可以适当添加
# 必须完成的功能：添加、删除、修改、查询、退出
# **********************************
# 请选择你要做的操作:
# 1.添加
# 2.删除
# 3.修改
# 4.查询
# 5.退出
# **********************************
# stu_li = [{'name':'小花','age':18,'sex':'女','sid':'sid001'},{'name':'小明','age':19,'sex':'男','sid':'sid002'},{'name':'小田','age':20,'sex':'男','sid':'sid003'}]
# li={}
# print('''         1.添加
#          2.删除
#          3.修改
#          4.查询
#          5.退出''')
# cz = input('请选择你要进行的操作:')
# if cz =='1':
#     usr = input('请输入你的姓名:')
#     age = input('请输入你的年龄:')
#     sex = input('请输入你的性别:')
#     sid = input('请输入你的学号:')
#     li['name']=usr
#     li['age']=age
#     li['sex']=sex
#     li['sid']=sid
#     stu_li.append(li)
# print(stu_li)
# if cz =='2':
#     ifo = input('请输入你要删除的信息(1.姓名2.年龄3.性别4.学号任选其一):')
#     for i in stu_li:
#         for k,v in i.items():
#             if v == ifo:
#                 stu_li.remove(i)
#                 print(stu_li)
# if cz =='3':
#     old = input('请输入你要修改的信息(1.姓名2.年龄3.性别4.学号任选其一):')
#     for i in stu_li:
#         for k,v in i.items():
#             if v == old:
#                 new = input('请输入你要更新的信息:')
#                 i[k]=new
#                 print(i)
# if cz=='4':
#     ifo = input('请输入你要查询的信息(1.姓名2.年龄3.性别4.学号任选其一):')
#     for i in stu_li:
#         for k,v in i.items():
#             if v == ifo:
#                 print(i)
# if cz=='5':
#     exit()

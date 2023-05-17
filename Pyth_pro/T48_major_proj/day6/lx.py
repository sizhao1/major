# 1.斗地主, 一共54张牌, 保存在列表中,随机给三个用户发牌.
# 保存54张牌
from random import *
def card_play():
    li = ['小王','大王']
    for i in range(1,14):
        for j in range(4):
            li.append(str(i))
    print(li)
    # 做下修饰
    for i in range(len(li)):
        if li[i]=='1':
            li[i] = 'A'
        elif li[i]=='11':
            li[i] = 'J'
        elif li[i]=='12':
            li[i] = 'Q'
        elif li[i]=='13':
            li[i] = 'K'
    print(li)
    # 随机给三个人发牌
    li_pai = []
    for i in range(3):
        li1 = sample(li,17)
        for j in li1:
            li.remove(j)
        li_pai.append(li1)
    print(li_pai)

# 2.抽奖: 给全公司35个员工, 生成35个随机抽奖号码, 号码由字母1位和数字3位组成.再随机抽出3个三等奖,2个二等奖,1个一等奖
# s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# li_word = list(s)
# # 生成35位抽奖号码
# li_hm = []
# for i in range(35):
#     start = choice(li_word)
#     s = start + str(randint(10000000,99999999))
#     li_hm.append(s)
# print(li_hm)
# # 抽奖 抽三等奖
# li_dj = sample(li_hm,3)
# for i in range(len(li_dj)):
#     li_hm.remove(li_dj[i])
# print('三等奖为:',li_dj)
# # 抽奖 抽二等奖
# li_dj = sample(li_hm,2)
# for i in range(len(li_dj)):
#     li_hm.remove(li_dj[i])
# print('二等奖为:',li_dj)
# # 抽奖 抽一等奖
# li_dj = sample(li_hm,1)
# for i in range(len(li_dj)):
#     li_hm.remove(li_dj[i])
# print('一等奖为:',li_dj)

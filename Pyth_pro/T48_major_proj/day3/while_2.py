'''
while循环:
死循环:
while True:
    执行语句
    判断条件
        break

continue: 关键字, 结束本次循环,直接开始下次循环.
break: 关键字, 结束整个循环.
'''
# 计算1到100所有的和
# 思考  不计算50
# i = 0
# sum = 0
# while i<100:
#     i += 1
#     if i==50:
#         continue
#     sum += i
# #打印的是累加最终的结果
# print(sum)

# i=1
# sum = 0
# while i<=100:
#     if i==50:
#         i+=1
#     sum+=i
#     i+=1
# print(sum)

# 练习2：打印1-100之间所有的偶数的累加
# 写法一:
# i=0
# sum = 0
# while i<100:
#     i+=1
#     if i%2==1:
#         continue
#     sum+=i
# print(sum)
# 写法二:
# i=0
# sum=0
# while i <100:
#     i+=2
#     sum+=i
# print(sum)

# 03，公交卡余额为43.8元，每天花1.5元坐公交车，问多少天以后就不能乘坐公交车？
# money = 43.8
# day_cost = 1.5
# day = 1
# while True:
#     money -= day_cost
#     if money<1.5:
#         print('第%d天后不够乘坐公交车了!'%day)
#         break
#     day +=1

# 练习3：小明家有一只乌龟,每天吃一根火腿肠,冰箱中火腿肠数由用户输入,
# 吃光所有的火腿肠需要几周?
# 打印一周后冰箱中还剩多少根火腿肠,二周后?三周后?四周后?...直到最后一周?
# week=0
# i = int(input('请输入火腿肠数：'))
# while 1:
#     week+=1
#     i-=7
#     if i<7:
#         print('第%d周后剩%d根火腿肠'%(week,i))
#         break

# ht_num=int(input('输入火腿数量：'))
# week=0
# while ht_num>7:
#     week+=1
#     ht_num -= 7
#     print(f'这是第{week}周,还剩{ht_num}根火腿')
# print(f'这些火腿可以吃{week}周！')

# 用户可以给商品写评价, 用户可以不限制输入评价的次数,直到用户输入'q'来退出. 写一个程序,保存用户的评价,并且将用户的评价记录在一个字符串中,等用户评价 完,打印输出用户的全部评价.
pingjie = ''
while 1:
    usr = input('请输入您的评价,结束请输入q:')
    if usr == 'q':
        break
    pingjie = pingjie+'\n'+usr
print(pingjie)







import random
# 1、循环录入5个数字，用一个列表保存, 然后将该列表的从小到大排序部分和不排列但原列表的逆序部分分别保存在两个列表中.
# li=[]
# for i in range(5):
#     num=int(input('请输入一个数字：'))
#     li.append(num)
# print(li)
# # 逆序保存的部分
# li1 = li[::-1]
# print(li1)
# # 排序升序排列,保存的部分
# li2 = sorted(li)
# print(li2)

# 2、 ['12','13','33','34','1399','2315','1111']，移除这个数组中包含1的字符串
# li= ['12','13','33','34','1399','2315','1111']
# for i in li[:]:
#     num=int(i)
#     if '1' in i:
#         li2=li.remove(i)
# print(li)

'''
3、移除一个列表中，数字小于33的元素 
列表：[11,22,33,1,6,4,88,44] 
'''
# li=[11,22,33,1,6,4,88,44]
# for i in li[:]:
#     if i<33:
#         li.remove(i)
# print(li)

# 4.将列表 [11,22,33,1,6,4,88,44]中元素分成大于33的部分,和小于33的部分, 分别用两个列表来保存.
# li= [11,22,33,1,6,4,88,44]
# li2=[]
# li3=[]
# for i in li:
#     if i>33:
#         li2.append(i)
#     elif i<33:
#         li3.append(i)
# print(li2)
# print(li3)

# 7, 从外部输入5个数值，保存起来，找出其中的最大值和最小值
# li=[]
# for i in range(5):
#     num=int(input('请输入一个数：'))
#     li.append(num)
# print(li)
# print('最大的值为：%d'%max(li))
# print('最小的值为：%d'%min(li))

# 8. 随机产生20个100-200之间的正整数存放到数组中，并求数组中的所有元素最大值、最小值、平均值，然后将各元素与平均值的差组成一个新数组。
# 生成 20个100-200之间的正整数
# li=[]
# for i in range(20):
#     num=random.randint(100,200)
#     li.append(num)
# print(li)
# # sum=0
# # for j in li:
# #     sum+=j
# # 求平均值
# sum1 =  sum(li)
# avg=sum1/len(li)
# print('该数组中所有元素的最大值为%d，最小值为%d，平均值为%.2f'%(max(li),min(li),avg))
# # 求各个值和平均值的差值
# li2=[]
# for k in li:
#     ret=k-avg
#     li2.append(round(ret,2))
# print(li2)

'''
9、用户输入某年某月某日，利用列表判断这一天是这一年的第几天？ 
   思路: 以2021年3月5日为例,需要考虑
   1).2021年是否为闰年,如果为闰年,那么2月是29天,比平年多1天
   2).3月,那么需要把3月前的满月天数加上,1月天数+2月天数
   3).5日,那么需要在日期基础上加上5
   4).用列表来记录每月的天数,比较好遍历
'''
# 接收用户输入的年月日数据
n=int(input('请输入年：'))
y=int(input('请输入月：'))
r=int(input('请输入日：'))
mouth=[0,31,28,31,30,31,30,31,31,30,31,30,31]
sum=0
# 处理年的影响
if (n%4==0 and n%100!=0) or (n%400==0):
    mouth[2]=29
# 处理月的影响
for i in range(y):  # 3 ----0,1,2
    sum += mouth[i]
# 处理日的影响
print('%d年%d月%d日是这一年的第%d天'%(n,y,r,sum+r))



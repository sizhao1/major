# 9.15作业:
# 1.输入一个数，判定该数是否为质数
# num = int(input('请输入一个数:'))   #9
# if num==1:
#     print('%d既不是质数也不是合数'%num)
# else:
#     for i in range(2,num):  #2,3,4,5,6,7,8
#         if num%i==0:
#             print('%d是合数' %num)
#             break
#     else:
#         print('%d是质数'%num)
# 2.输入班级学生语文成绩，求总成绩和平均成绩 。班级人数从键盘输入
# num = int(input('请输入班级的人数:'))
# sum = 0
# for i in range(num):
#     ywcj = float(input('请输入第%d个人的语文成绩:'%(i+1)))
#     sum += ywcj
# print('总成绩是:%.2f'%sum,'平均成绩是%.2f'%(sum/num))
# 3.循环输入7天温度，求平均温度
# total_wd=0
# for i in range(7):
#     wd=float(input("请输入%d天的温度："%(i+1)))
#     total_wd+=wd
# avg_wd=total_wd/7
# print("这七天的平均温度为：%.2f"%avg_wd)

# 4.求 100-200以内同时能被7、8整除的数
# for i in range (100,201):
#     if i%7==0 and i%8==0:
#         print("同时能被7、8整除的数为：%d"%i)
# 4.1设计一个程序求出所有能够被7整除的3位整数
# for i in range (100,1000):
#     if i%7==0:
#         print(i)
# 5.整除
# 5.1：求 100-200以内同时能被2、3、5整除的第一个数
# 5.2 #把100~200之间的不能被3整除的数输出
# for i in range(100,201):
#     if i%2==0 and i%3==0 and i%5==0:
#         print("100-200以内同时能被2、3、5整除的第一个数为：%d" % i)
#         break

# for i in range(100,201):
#     if i%3!=0:
#         print("100~200之间的不能被3整除的数为：%d"%i)
# 6.求 1-100以内所有含6的数
# for i in range(1,101):
#     shi=i//10
#     ge=i%10
#     if shi==6 or ge==6:
#         print(i,end=' ')
# 7.Chuckie Lucky赢了100W美元，
# # 他把它存入一个每年盈利8%的账户。
# # 在每年的最后一天，Chuckie取出10W美元。
# # 设置一个列表，来记录每年他的剩余金额,直至0为止, 打印多少年后Chuckie会清空他的账户。
total_money=100
i=0
while True:
    total_money=total_money+total_money*0.08
    total_money-=10
    i+=1
    if total_money<10:
        i+=1
        print("%d年后Chuckie会清空他的账户,此时他要取出%fW美元!"%(i,total_money))
        break

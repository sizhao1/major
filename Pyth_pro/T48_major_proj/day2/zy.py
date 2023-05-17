'''
1.企业发放的奖金根据利润提成,利润低于或等于10万元时,奖金可提成10%,利润高于10万元时,
 低于20万元时,低于10万元部分按10%提成,高于10万元部分按7.5%提成,20-40万时,高于20万部分,
 可提成5%,40-60万时,高于40万部分,可提成3%,60-100万时,高于60万部分,可提成1.5%,高于100万的部分,
 可提成1%,从键盘输入当月利润,求应发放的奖金总数?
'''
# profit=float(input('请输入利润(单位为万)：'))
# if profit>0:
#     if profit<=10:
#         commission=profit*0.1
#     elif profit<20:
#         commission=10*0.1+(profit-10)*0.075
#     elif profit<=40:
#         commission=10*0.1+10*0.075+(profit-20)*0.05
#     elif profit<=60:
#         commission=10*0.1+10*0.075+20*0.05+(profit-40)*0.03
#     elif profit<=100:
#         commission=10*0.1+10*0.075+20*0.05+20*0.03+(profit-60)*0.015
#     else:
#         commission=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(profit-100)*0.01
#     print('您的提成为：%.2f万' % commission)
# else:
#     print('输入不正确!')

#2.登录的那个题,给三次机会.

# i=1
# while i<=3:
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     if username == 'admin' and password == 'Pass1234':
#         print('登录成功！')
#         break
#     else:
#         print('登录失败，用户名或密码错误！')
#     i+=1


'''3. 编写程序，完成以下要求：
提示用户输入数据
获取用户的数据（需要获取2个,且两个都为两位数）
如果用户输入的数为99,则提示其输入了最大的两位数
如果用户输入的数为10,则提示其输入了最小的两位数
最后计算两数的和,打印出来和
'''
# num1=int(input('请输入第一个值：'))
# num2=int(input('请输入第二个值：'))
# if (num1>=10 and num1<=99) and (num2>=10 and num2<=99):
#     if num1==99 or num2==99:
#         print('您输入了最大的两位数')
#     if num1==10 or num2==10:
#         print('您输入了最小的两位数')
#     print(num1 + num2)
# else:
#     print('输入无效!')

'''
4、请根据男女,输入你的各项参数,计算你的体脂率:
成年女性的体脂率计算公式：
参数a=腰围（cm）×0.74
参数b=体重（kg）×0.082+34.89
体脂肪重量（kg）=a－b
体脂率=（身体脂肪总重量÷体重）×100%
成年男性的体脂率计算公式：
参数a=腰围（cm）×0.74
参数b=体重（kg）×0.082+44.74
体脂肪重量（kg）=a－b
体脂率=（身体脂肪总重量÷体重）×100%。
成年人的体脂率正常范围分别是女性20%～25%，男性15%～18%，若体脂率过高，就有肥胖的风险。
请提示用户是否可能属于肥胖。
'''
# sex=input('请输入您的性别：')
# yw=int(input('请输入您的腰围（cm）：'))
# tz=int(input('请输入您的体重（kg）：'))
# a = 0.74 * yw
# if sex=='女':
#     b=tz*0.082+34.89
#     zf=a-b
#     tzl=zf/tz
#     print('您的体脂率为：%.2f%%'%(tzl*100))
#     if tzl>=0.2:
#         if tzl<=0.25:
#             print('您的体脂率正常')
#         else:
#             print('您的体脂率过高，有肥胖的风险！')
#     else:
#         print('您的体脂率不在正常范围!')
#
# elif sex=='男':
#     b=tz*0.082+44.74
#     zf=a-b
#     tzl=zf/tz
#     print('您的体脂率为：%.2f%%' %(tzl*100))
#     if tzl>=0.15:
#         if tzl<=0.18:
#             print('您的体脂率正常')
#         else:
#             print('您的体脂率过高，有肥胖的风险！')
#     else:
#         print('您的体脂率过低')

'''
5、计算机和人进行猜数字游戏,计算机随机在1-100之间产生一个整数,由人猜测,
把人输入的数字和计算机产生的比较,提示猜大了,小了,还是猜对了.
计算机随机产生整数的代码为:
import random
computer = random.randint(1,100)
'''
# import random
# computer = random.randint(1,100)
# i = 1
# while i<=5:
#     guess=int(input('请输入一个整数：'))
#     if guess>computer:
#         print('猜大了！')
#     elif guess<computer:
#         print('猜小了！')
#     else:
#         print('猜对了！')
#         break
#     i += 1


'''
6. 用户输入他的公交卡余额,如果余额在0-500则认为是普通卡,若果超过500,则认为是vip卡
普通卡如果余额小于2元,则提示用户"您的公交卡需要充值了".
普通卡如果余额为0元,则提示用户"您不可以乘坐公交车".
'''
ye=int(input('请输入您的公交车余额：'))
if ye>=0 and ye<=500:
    print('您的公交卡是普通卡！')
    if ye<=2 and ye!=0:
        print('您的公交卡需要充值了')
    if ye==0:
        print("您不可以乘坐公交车")
elif ye>500:
    print('您的公交卡是vip卡！')
else:
    print('输入不正确!')


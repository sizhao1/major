import re
# 0926函数完成:
# 1.某售票系统在用户买票时，需要输入身份证号码，设计一个程序完成身份证号码的校验。
# 校验规则：身份证必须是18位，全部由数字组成（只有最后一位可以是字母X），且身份证开头3位数字必须与当前省份编码（510）一致
def check_id(id_card):
    if re.findall('^510[\d]{14}[\d|X]$',id_card):
        return True

# if __name__ == '__main__':
#     id_card=input('请输入身份证号：')
#     if check_id(id_card):
#         print(id_card,'输入的身份证号正确！')
#     else:
#         print(id_card,'输入的身份证号有误！')

# 2.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
def calculate_age(num,age1):
    age=[age1]
    for i in range(num-1):  #0 1 2 3
        age_i=age[i]+2
        age.append(age_i)
    return age
# if __name__ == '__main__':
#     ret=calculate_age(5,10)
#     print('第5个人的年龄为',ret[4],'岁')

# 3.16海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
# 第五只猴子也拿走了一份，问海滩上原来最少有多少个桃子？
def match_sum(total):
    peach=[]
    for i in range(5):
        total=(total-1)/5
        peach.append(total)
    return peach
# if __name__ == '__main__':
#     p1=25
#     while 1:
#         peach=match_sum(p1)
#         if peach[4].is_integer() and peach[4] > 0:
#             break
#         p1+=1
#     p_sum=peach[0]*5+1
#     print(peach)
#     print('海滩上原来最少有%d个桃子'%p_sum)

#定义一个函数传入参数几只猴参加分桃，最后一只猴拿到桃子的最大值
def jisuan(num1,num2):
# 外层循环规定最后一只猴拿到的桃数
    for i in range(num2):
        num=i
# 内层循环计算上一个猴拿到的桃数
        for j in range(num1-1):
            num=num*num1+1
            num=num/(num1-1)
        if int(num*num1+1)==num*num1+1:
            break
    # 打印最后一个猴拿到的桃数
    # 打印总的桃数
    print(i)
    print(num*num1+1)
# if __name__ == '__main__':
#     jisuan(5,10000)

def fen_tao():
    x = 1
    while 1:
        fen = (x+4)/5  #第一只猴分到的
        for i in range(1,5):  #1,2,3,4 第二只候,到第五只猴分到的桃子
            fen = (x+4)*(4**i)/5**(i+1)
        if fen%1==0:
            break
        else:
            x += 1
    print(x)

fen_tao()

# 4.用户输入一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
def num_judge(num):
    try:
        if len(num)==5 and int(num):
            return True
        else:
            return False
    except Exception:
        print('输入的不是整数!')

def num_hwnum(num):
    if num == num[::-1]:
        return True
    else:
        return False
# if __name__ == '__main__':
#     num=input('请输入一个五位数：')
#     if num_judge(num):
#         if num_hwnum(num):
#             print('您输入的数为回文数！')
#         else:
#             print('您输入的数不是回文数！')
#     else:
#         print('输入有误！')

# 5.你在月球上的体重
# 如果你现在正站在月球上,你的体重将只相当于在地球上的16.5%.你可以通过把你在地球上的体重乘以0.165来计算.
# 如果在接下来的15年里,你每年增长一公斤,那么在直到15年后的你每年里访问月球时的体重都是多少?
# 用for循环来写一个程序,来打印你每年在月球上的体重.
def calculate_weight(rig_weight):
        moon_weight=rig_weight*0.165
        return moon_weight

# if __name__ == '__main__':
#     rig_weight=float(input('请输入初始体重（公斤）：'))
#     for i in range(15):
#         m_weight = calculate_weight(rig_weight)
#         print('第%d年在月球上的体重为：%.2f'%(i+1,m_weight))
#         rig_weight +=1



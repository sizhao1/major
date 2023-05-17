'''
循环结构:
特殊结构.循环也只被当做一条语句. 循环里的执行语句,执行结束后,会回到循环开始的地方,继续做判断,只要while后面的条件语句为True,循环就会继续执行.

while的定次循环语法:
i=1  #计数器
while i<=5(条件语句):
    执行语句
    i+=1

break: 关键字, 结束循环.
'''
from random import randint
# i=1  #计数器
# while i<=5:
#     print(i)
#     i+=1

# 3.猜数字游戏, 计算机先定义好一个1-100的随机整数.然后让用户去猜,一共给予5次猜的机会,每次提示用户是猜大了还是猜小了,猜对结束,猜错5次,机会用完.
i = 1
num = randint(1,100)
while i<=5:
    guess = int(input('请输入您猜的值:'))
    if guess>num:
        print('大了!')
    elif guess<num:
        print('小了!')
    else:
        print('猜对了!')
        break
    i+=1
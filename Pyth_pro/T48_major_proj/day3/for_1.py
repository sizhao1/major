'''
for循环:
格式二:
for i in range(start,end,step):
    执行语句

介绍range()函数:
range():一共有三个参数.
start: 开始值,默认从0开始,如果是0,可以省略.
end: 结束值, 不可以省. 取值只能取到 end-1 .
step: 步长,默认是1,可以省.
返回值: 返回一个连续数值的序列,范围从start到end-1,间隔按step间隔.

for...else写法: for里面一定要有一个判断退出循环的条件(一定要有个break),当for是因为执行到break语句退出,那么else不会被执行. 如果for是因为正常的循环结束而退出的话,那么else就会被执行.
tips:如果for中,忘了写break,那么else一定会被命中.

双层循环:
一般用作两个逻辑的嵌套,或者打印图形.
'''
from random import randint

# a = list(range(1,10,2))
# print(a)

# 从1到10进行打印
# for i in range(1,11):
#     print(i)

# 计算1到100的乘积
# 只乘以偶数
# res = 1
# for i in range(2,101,2):
#     res *= i
# print(res)

# 0代表剪刀,1代表石头,2代表布,计算机和用户进行猜拳游戏
# 给5次机会,统计用户赢的次数
# 逻辑: 计算机  0   1   2
#        用户  1   2   0   ----赢
# count = 0
# for i in range(5):
#     computer = randint(0, 2)
#     user = int(input('请输入你的结果(0代表剪刀,1代表石头,2代表布):'))
#     if user>=0 and user<=2:
#         if (computer==0 and user==1) or (computer==1 and user==2) or (computer==2 and user==0):
#             print('用户赢!')
#             count += 1
#         elif computer==user:
#             print('平了!')
#         else:
#             print('输了!')
#     else:
#         print('输入无效!')
# print('用户一共赢了%d次'%count)

# 3、求100-999之间的所有水仙花数。
#    水仙花数是这个数的每一位上数字的立方和等于这个数本身，比如153=1^3+5^3+3^3=1+125+27=153
# for i in range(100,1000):
#     bai = i//100
#     shi = i%100//10
#     ge = i%10
#     if i == bai**3+shi**3+ge**3:
#         print('%d是水仙花数'%i)

# 小练习：使用for循环输出下列结果
# 五行一列*
# *
# *
# *
# *
# # *
# for i in range(5):
#     print('*')
# # 一行五列*
# # *****
# for i in range(5):
#     print('*',end='')
'''
*****
*****
*****
*****
*****
'''
# for i in range(5):
#     for j in range(5):
#         print('*',end='')
#     print()

'''
*              第1行   有1列
**             第2行   有2列
***            第3行   有3列
****           第4行   有4列
*****          第5行   有5列
'''
# for i in range(5):        # 0,1,2,3,4  i+1
#     for j in range(i+1):  #0|0,1|0,1,2|0,1,2,3|0,1,2,3,4
#         print('*',end='')
#     print()

# 打印九九乘法表
for i in range(9):        # 0,1,2,3,4  i+1
    for j in range(i+1):  #0|0,1|0,1,2|0,1,2,3|0,1,2,3,4
        print('%d*%d=%d'%((j+1),(i+1),(i+1)*(j+1)),end='\t')
    print()

'''
需要打印的总共的*和空格数: 2*8-1
    *         i=1    s=8  *=1   需要打印的*数:2i-1 需要打印的空格:9-(2i-1)=(10-2i)/2 = 5-i
   ***        i=2    s=6  *=3   
  *****       i=3    s=4  *=5
 *******      i=4    s=2  *=7
*********     i=5    s=0  *=9             
'''
for h in range(1,6):
    for k in range(1,6-h):
        print(' ',end='')
    for x in range(1,2*h):
        print('*',end='')
    print()






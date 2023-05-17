from random import *
import os

# 0923:
# 1.在当前路径下,新键一个"report"路径, 通过代码的方式创建一个文本文件"1209re.txt"生成在report目录下,在这个txt文件中写入如下内容:
# #1  zhangsan  89
# #2  lisi  59
# #3  wangwu  19
# #4   asan  9
def create_dir(dir_name):
    if os.path.exists(dir_name):
        print('该文件夹已经存在!')
        return True
    else:
        os.mkdir(dir_name)
        return True
# li = ['1  zhangsan  89\n','2  lisi  59\n','3  wangwu  19\n','4   asan  9\n']
def create_file(filepath,s):
    with open(filepath,'w')as f:
        f.write(s)

# if __name__ == '__main__':
#     dirname = 'rwpwwwwwiii'
#     filepath = '.\\'+dirname+'\\'+'1209re.txt'
#     s = '1 zhangsan 89\n2  lisi  59\n3  wangwu  19\n4   asan  9\n5   xiaohua   77'
#     if create_dir(dirname):
#         create_file(filepath,s)
#     else:
#         print('创建文件夹不成功!')


# 2 编写一个函数接收输入一个字符，判断这个字符是数字，还是大写字母，还是小写字母，还是符号(ASCII码,ord()函数)
def save_a_char():
    s = input('请输入一个字符：')
    if len(s)!=1:
        print('输入不是一个字符!')
    else:
        return s

def type_of_which(chr1):
    if 0<=ord(chr1)<=127:
        if chr1.isdigit():
            print(chr1,'这是个数字')
        elif chr1.isalpha():
            if chr1.isupper():
                print(chr1,'这是个大写字母')
            elif chr1.islower():
                print(chr1,'这是个小写字母')
        else:
            print(chr1,'这是个符号')
    else:
        print('输入的不是ascii码,无法判断!')

# if __name__ == '__main__':
#     # chr1 = save_a_char()
#     # if chr1:
#     #     type_of_which(chr1)
#
#     s = input('请输入一个字符串:')
#     for i in s:
#         type_of_which(i)

# 3 计算程序，要求用户输入两个整数和一个运算符，程序能够计算出两个数的运算结果（只考虑加减乘除）。（涉及到精确度的，一律保留两位小数)
# 利用此计算程序,给用户连续出10道题, 计算用户答对的次数.
def count_res(num1,num2,operate):
        if operate == '+':
            return num1 + num2
        elif operate == '-':
            return num1-num2
        elif operate == '*':
            return num1 * num2
        elif operate == '/':
            if num2 == 0:
                print('除数不能为0,此题做废!')
                return '过'
            else:
                return round(num1/num2,2)

def check_valid(num1,num2,operate):
    if num1.isdigit() and num2.isdigit() and operate in ('+','-','*','/'):
        return True
    else:
        print('输入错误,重新输入!')

# if __name__ == '__main__':
#     count = 0
#     for i in range(5):
#         print('这是第%d道题'%(i+1))
#         num1 = input('请输入一个整数:')
#         num2 = input('请输入另一个整数:')
#         operate = input('请输入计算符(+-*/):')
#         if check_valid(num1,num2,operate):
#             res = count_res(int(num1),int(num2),operate)
#             if res!="过":
#                 answer = round(float(input('请输入您的答案:')),2)
#                 if res == answer:
#                     print('恭喜你,答对了!')
#                     count += 1
#                 else:
#                     print("答错了,正确答案是:",res)
#
#     print('一共答对了%d道题'%count)

# 4.有10个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，设计一个程序计算最后留下的是原来第几号的那位
# lis=['1','2','3','4','5','6','7','8','9','10']
# while 1:
#     print(lis)
#     # 如果只剩下一个数,那么结果就出来了
#     if len(lis)==1:
#         break
#     # 如果大于3,继续循环,删报3的数
#     elif len(lis)>=3:
#         # 计算删除报3的数后,需要往下一轮列表移动的数
#         num = len(lis)%3
#         # 计算需要删除的元素,这些元素用' '表示
#         for j in range(len(lis)):
#             if (j+1)%3==0:
#                 lis[j] = ' '
#         # 当列表中有' ',删除
#         for k in lis:
#             if k==' ':
#                 lis.remove(k)
#         # 计算需要移动的数,做处理
#         for l in range(num):  # 0  #0和1
#             lis.insert(l,lis.pop(-(num-l)))
#     # 如果只剩两个数,那么删第一个
#     else:
#         lis.pop(0)
# print(lis)

# li=[1,2,3,4,5,6,7,8,9,10]
# coun=0
# while True:
#     if len(li)==1:
#         break
#     else:
#         num=coun%3
#         lix=li[:]
#         for i in lix:
#             if (lix.index(i)+num+1)%3==0:
#                 li.remove(i)
#             coun+=1
# print(f"最后留下的是第{li}位")


# 5 有一个10米深的井，井底有只青蛙，青蛙每次向上爬5米后就会下滑3米，设计一个程序计算青蛙需要几次能爬到井外
# def frog_climbing():
#     i = 0
#     left = 10
#     while 1:
#         i += 1
#         left = left - 5
#         if left<=0:
#             break
#         else:
#             left += 3
#     print(i)
#
# frog_climbing()


# 6.某个公司传输数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后再用除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换，设计解密程序，能够根据接收的数据判断出原始数据

# （每位数字+5 ）%10 ---> 2.乘以10后，每位数字-5
# 第一位和第四位交换，第二位和第三位交换--->
# 1.先把位置换回来,--->倒序
# 2.每位数字都加上,5除以10的余数代替该数字--->  大于5: -5 小于5: +5
3.

def switch_num(num):
    num = num[::-1]
    print(num)
    return num

def cal_num(num):
    li = list(num)
    for i in range(len(li)):
        li[i] = int(li[i])
        if li[i] >= 5:
            li[i] = str(li[i] -5)
        elif li[i] < 5:
            li[i] = str(li[i] +5)
    num = int(''.join(li))
    return num

# if __name__ == '__main__':
#     num = input('输入传输数据四位的整数:')  # 7920
#     n = switch_num(num)
#     num = cal_num(n)
#     print(num)

# 7.某系统做限时促销活动，要求设计一个程序生成200个邀请码，邀请码由6位字符组成，要求是一个随机字母开头,其它五位为随机数字
def invite_code(num):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ'
    d = '1234567890'
    lis = []
    for i in range(num):
        start = choice(s)
        digit = sample(d,5)
        res = str(start) + ''.join(digit)
        lis.append(res)
    print(lis)

# invite_code(20)
# 8.现在银行推出一款理财产品，要求连续5年每年存入1万元钱，每年年终按8%计息，利息滚入下一年本金中，存满15年后全部取出，要求设计一个程序计算出最终能得到多少钱
def manage_money(money,a,b):
    # money是本金，a是连续存入的年数，b是总得存款年限
    for i in range(a):
        money += money * 0.08
        money += 1
    # print(money)
    for j in range(b-a):
        money += money * 0.08
    print(round(money,2))
manage_money(1,5,15)
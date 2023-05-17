'''
列表:
数据结构, 可以有多个数据,多种数据类型. 可变数据类型. 建议:尽量将同种数据类型的数据存在一个列表中.
表示:
[],中括号里面保存列表的元素, 可以是多个,元素和元素之间有逗号分隔开.
例空列表: []
例非空列表: [1,3,5,7,9,11]

序列:
定义:字符串、列表和元组都是序列. 序列在内存中,它的元素是顺序存储.
索引(下标): 可以通过列表的索引下标来获取到列表中的元素. 例: li[3]
切片: 对列表的部分或全部元素的复制. 写法: li[start:end:step]
start: 开始值, 可以取到,默认为0,为0时可以省.
end: 结束值, 取不到, 默认是最后一个元素的索引+1, 可以省.
step: 步长值, 默认为1,可以不写.
li[:]: 全盘复制.
li[::-1]: 逆序输出全盘复制的结果.

+: 序列中把两个序列拼接到一起
tips:列表和列表拼接, 字符串和字符串拼接,元祖和元祖拼接
*: 把序列复制多少遍.
tips: *后一定跟的是int,不能是其它数据类型.

可变数据类型.
列表中的元素是可以增删改查,且很方便.
增:
append(): 往列表的末尾追加元素. 排队式的追加.
列表主调这个函数, 把要追加的元素作为参数传入函数中, 没有返回值.
insert(): 插入元素,插队式的加入, 两个参数, 插入的索引,元素值.
extend(): 类似于 + 操作. 其它的数据结构要先转换成列表. 参数里的列表的元素往主调的列表元素中追加.
删:
pop(): 不需要传参, 从列表的末尾进行删除. 对应append(). 返回删除的元素.
pop(i): 需要传参, 传入要删除的元素的索引值. 返回删除的元素. 对应的需求是: 知道索引下标去删元素.
remove(item): 需要传参,传入要删除的元素值. 无返回值. 对应的需求是: 知道要删除的元素去删除.
del 关键字: 可以删除整个列表, 可以删除单个元素.
改:
li[index] = 新值
查:
知道索引查值:  li[index]
知道值查索引:
index():  传参,传入要查找的值, 返回对应的索引. 缺陷: 第一个找到了,就不会往后找.
传入要查找的值,传入查找的位置(起始位置和终止位置).
count(): 传参,传入要查找的值, 返回找到的次数.
判断:
in:      判断某个元素在这个列表中     ---True
not in:  判断某个元素不在这个列表中    ---True

列表中元素的遍历:
for循环的第一种格式:
for i in list:
    只能知道值:
    i
    执行语句

for i in range(len(li)):
    第一:知道索引
    i
    第二:知道值
    li[i]

特有的函数:
len(): 计算序列中的元素个数.
sort(): 数值型的数据, 从小到大的顺序排.  列表会被改变.
reverse=True 参数: 可以改变排列的顺序. 将默认的升序变成降序.
其它类型的数据,按ascii排列.
sorted(): 数值型的数据, 从小到大的顺序排.  列表不会被改变. 产生一个排序的结果.
reverse(): 直接进行逆序操作.
max(): 从列表中取最大值. 不改变列表
min(): 从列表中取最小值. 不改变列表

列表推导式:
1.
lis = [表达式 for i in range(数值)]
例: list5 = [x*0.9 for x in range(10)]
2.
lis = [表达式 for i in list1]
例:list5 = [1,2,3,4,5,6]
list6 = [x**2 for x in list5]
3.
lis = [表达式 for i in list1 if 条件表达式]
例:list5 = [1,2,3,4,5,6]
list6 = [x**2 for x in list5 if x<5]
'''
li = [1,3,5,7,9,10,11]
li2 = ['a','b','c']
# print(li[2])
# print(li[::])  #[1, 3, 5, 7, 9, 10, 11]
# print(li[::2]) #[1, 5, 9, 11]
# print(li[:])
# print(li[:-2])
# print(li[-6:-1]) #[3,5,7,9,10]
# print(li[::-1])
# print(li+li2)
# print(li+'11223344')  #不支持, 列表和列表拼接, 字符串和字符串拼接,元祖和元祖拼接
# print(li*3)

# str1 = 'abcderftyyu'
# print(str1[6])
# print(str1[::-1])
# print(str1[-8:-2])

tup = (1,2,5,8,0,11,44,55)
tup2 = ('22','33')
# print(tup[6])
# print(tup[::-1])
# print(tup[-3:-1])
# print(tup+tup2)
# print(tup2*4)


# 增删改查
li1 = [11,22,33,44,11,12,13,15]
# li1.append('44')
# print(li1)
# li1.insert(3,'11001')
# print(li1)
# li1.extend(['11223344'])
# s = '11223344'
# print(list(s))
# print(li1)
# ret = li1.pop()
# print(li1)
# print(ret)
# ret = li1.pop(2)
# print(li1)
# print(ret)
# ret = li1.remove(11)
# print(ret)
# print(li1)
# del li1
# print(li1)
# del li1[6]
# print(li1)
# li1[6] = 'abcdg'
# print(li1)
# ret = li1.count(11)
# print(ret)
# start = li1.index(11)
# print(start)
# ret = li1.index(11,start+1,len(li1))
# print(ret)
# print(len(li1))
# print(11 in li1)
# print(11 not in li1)

'''
li = ['taibai','alexC','AbC','egon','Ritian','Wusir','aqc']
1)计算列表长度并输出
2）向列表中追加一个元素并输出最终列表
3）在指定位置1插入元素ttt
4）修改指定元素‘AbC’为‘ooo’
5）删除最后一个元素
6）将列表所有元素翻转
'''
li = ['taibai','alexC','AbC','egon','Ritian','Wusir','aqc']
# print(len(li))
# li.append('abc')
# print(li)
# li.insert(1,'ttt')
# print(li)
# inx = li.index('AbC')
# li[inx] = 'ooo'
# print(li)
# li.pop()
# print(li)
# print(li[::-1])

'''
练习3:用列表记录自己到过的8个城市:
1)增加一个城市"北京"
2)判断是否有城市"南京",如果有,删除
3)判断索引为3的城市是否为'东京',如不是把索引为3的城市修改为"东京"
4)对此列表先进行排序,再进行逆序
'''
# li = ['西安','南京','宝鸡','安康','延安','上海','南京','南京']
# for city in li[:]:
#     print(li)
#     if city=='南京':
#         li.remove('南京')
# print(li)

# li.append('北京')
# print(li)
# if '南京' in li:
#     li.remove('南京')
# else:
#     print('没有南京!')
# if li[3]!='东京':
#     li[3] = '东京'
# print(li)
# li.sort()
# print(li)
# li.reverse()
# print(li)

'''
输入并记录班级学生的语文成绩,输入'q'结束，打印出记录的成绩,计算总成绩和平均成绩.
'''
# li = []
# while True:
#     score = input('请输入你的语文成绩:')
#     if score=='q':
#         break
#     else:
#         score = float(score)
#         li.append(score)
# print(li)
#
# total = 0
# for i in range(len(li)):
#     total+=li[i]
#
# print('总成绩为:',total)
# print('平均成绩为:%.2f'%(total/len(li)))

li = [3,9,7,4,6,8,1,6,7,9,0]
# li.sort(reverse=True)
# print(li)
# a = sorted(li)
# print(a)
# print(li)
# li.reverse()
# print(li)

# li = ['a','A','b','z','e','Z','1','中','人']
# li.sort()
# print(li)

'''
练习4:解决千年虫问题,以前的电脑为了节省存储空间,通常年份都是用的两位数字,这样跨过2000年后,2000年和1900都会表示为00,造成计算机系统故障,编写程序将一下序列中年份转换为4位,并升序输出.
当前序列:[89,98,00,75,68,37,58,90]
输出序列:[1937,1958,1968,1975,1989,1990,1998,2000]
'''
# li1 = [89,98,00,75,68,37,58,90]
# li2 = []
# for i in li1:
#     if i==0:
#         li2.append(2000)
#     else:
#         i = i+1900
#         li2.append(i)
# print(li2)
# li2.sort()
# print(li2)

'''
练习5:将列表[45,23,2,5,3,2,6,45,43,21,66,2,3,2]进行从小到大排序,不能用sorted()函数或list.sort()方法.
'''
# li = [45,23,2,5,3,2,6,45,43,21,66,2,3,2]
# li2=[]
# for i in li[:]:
#     li2.append(min(li))
#     li.remove(min(li))
# print(li2)

# 练习6:求100-200以内同时能被7,8整除的数,保存在列表中.
# li = []
# for i in range(100,201):
#     if i%7==0 and i%8==0:
#         li.append(i)
# print(li)
# 练习7:找出一个列表中,只出现了一次的数字,并保持原来的次序,例如[1,2,1,3,2,5]结果为[3,5]
# li =[1,2,1,3,2,5]
# li1 = []
# for i in li:
#     if li.count(i)==1:
#         li1.append(i)
# print(li1)

# 练习8: 求0 -1 +2 -3 +4 -5 +6 -7...+100的结果
# res = 0
# for i in range(1,101):
#     if i%2==0:
#         res+=i
#     else:
#         res-=i
# print(res)

# lis = [2,3,'k',['qwe',20,['k',['tt',3,'1']],89],'ab','adv']
# 1)将列表lis中的’tt’变成大写:
# 2)将列表中的数字3变成字符串’100’ :
lis = [2,3,'k',['qwe',20,['k',['tt',3,'1']],89],'ab','adv']
# print(lis[3])
# print(lis[3][2])
# print(lis[3][2][1])
# lis[3][2][1][0] = 'TT'
# print(lis)
# lis[1] = '100'
# lis[3][2][1][1] = '100'
# print(lis)
print(isinstance(lis,list))
print(isinstance(lis[3],list))
print(isinstance(lis[3][2],list))
print(isinstance(lis[3][2][1],list))
print(isinstance(lis[3][2][1][0],list))
print(isinstance('a',str))



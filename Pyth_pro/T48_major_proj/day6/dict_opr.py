'''
字典:
数据结构, 可以存储多个数据,多种数据类型. 可变数据类型.
建议:尽量将同种逻辑的数据存在一个字典中.
表示:
{},元素和元素之间也是用逗号分割, 元素怎么表示: 键值对的方式来表示, k:v 表示.
例: 空字典{}
有元素的字典{'姓名':'张三','性别':'男','学号':'sid001'}

存储方式:
并不是像列表一样, 按照索引的顺序, 在内存中顺序存储.
按照键来有规律的存储, 不属于序列, 属于可迭代的结构(itreable).

字典的特点: 按照键来获取值
可变数据类型:
增:
字典名[新键] = 新值, 就是一个增加元素到字典.
改:
字典名[老键] = 新值, 就是一个对原有元素的修改.
删:
popitem(): 直接删除最后一个元素, 类似于列表中的pop().
pop(k): 按照键来删除值,在原字典中这个键值对就删除了.
del: del 字典名-->整个删除字典. del 字典名[键] -->删除单个元素,基本等同pop(k)
clear(): 清空字典.
查:
知道键,查值 ---> 字典名[键]:没有这个键,崩溃退出  get(键):当没有这个键,返回None
in: 可以做判断,判断的是键.  判断有这个键
not in: 判断没这个键

字典中元素的遍历:
a.遍历键
字典名.keys()
b.遍历值
字典名.values()
c.遍历键值对
字典名.items()
for k in dic.keys():
    print(k)
for v in dic.values():
    print(v)
for k,v in dic.items():  # k,v = 1,2
    print(k,v)

特有的函数:
len(): 计算字典中元素的个数.
max(): 对键进行比较,取最大.
min(): 对键进行比较,取最小.

tips:
字典中键有要求的,键只能是不可变数据类型,不能够是可变数据类型.

字典的深拷贝和浅拷贝:
浅拷贝:   dic.copy()         拷贝的是原字典中元素的应用(内存地址值)
深拷贝:   copy.deepcopy(dic) 拷贝的是原字典中的元素
'''
# 生成每个组的学生信息: 姓名,年龄, 性别, 身高,体重,学号
group3={1:{'name':'袁荣兵','sex':'男','higth':'180','weigh':'65','age':'23'},
        2:{'name':'徐赟','sex':'男','higth':'180','weigh':'60','age':'23'},
        3:{'name':'伊文静','sex':'女','higth':'155','weigh':'38','age':'25'},
        4:{'name':'李亮亮','sex':'男','higth':'188','weigh':'75','age':'25'},
        5:{'name':'李荣','sex':'女','higth':'165','weigh':'45','age':'25'}}
# print(max(group3))
# print(min(group3))
dic = group3.copy()
print(dic)

# lis=[{'name':'袁荣兵','sex':'男','higth':'180','weigh':'65','age':'23'},{'name':'徐赟','sex':'男','higth':'180','weigh':'60','age':'23'},{'name':'伊文静','sex':'女','higth':'155','weigh':'38','age':'25'},{'name':'李亮亮','sex':'男','higth':'188','weigh':'75','age':'25'},{'name':'李荣','sex':'女','higth':'165','weigh':'45','age':'25'}]

# lis =  [1,3,5,7,9]
# print(id(lis[0]),id(lis[1]),id(lis[2]),id(lis[3]),id(lis[4]))
dic1 = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4','k5':'v5'}
# print(dic[1])  # 报错:字典中括号中的值当成键来处理了,不会被当做索引.
# print(id(dic['k1']),id(dic['k2']),id(dic['k3']),id(dic['k4']),id(dic['k5']))
# print(dic[:])  # 报错:不支持切片.
# dic2 = {1:'a1',2:'a2'}
# dic1['k6'] = 'v6'
# print(dic1)
# dic1['k2'] = 'abc'
# print(dic1)
# v = dic1.pop('k1')
# print(v)
# print(dic1)
# del dic1['k1']
# print(dic1)
# print(dic1['k11'])  #键不存在,会报错.
# print(dic1.get('k11')) #不报错,返回None. 友好
# print('v1' in dic1)

'''
10. 用一个字典来记录某个学生的一系列信息,包括: 姓名,性别,年龄,身高,体重信息
1)、请循环遍历出所有的key 
2)、请循环遍历出所有的value
3).请循环遍历出所有的key和value
4)、请在字典中增加一个键值对,"sid":"stu001"，输出添加后的字典
5)、请删除字典中键为age的元素,并输出删除后的结果
6)、请获取字典中"name"对应的值
'''
# dic = {'name':'张三','sex':'女','age':21,'height':1.66,'weight':55}
# for k in dic.keys():
#     print(k)
# for v in dic.values():
#     print(v)
# for k,v in dic.items():
#     print('键是%s'%k,'值是%s'%v)
# dic['sid'] = 'stu001'
# print(dic)
# dic.pop('age')
# print(dic)
# print('name对应的值是:%s'%dic['name'])
# dic['sex']='男'
# print(dic)

# 1、循环录入5个数字，用一个列表保存, 然后将该列表的从小到大排序部分和不排列但原列表的逆序部分分别保存在两个列表中.
# 字典题: 分别将结果保存在字典中.
# 保存录入的数字
# li = []
# for i in range(5):
#     num = int(input('请输入一个数字:'))
#     li.append(num)
# print(li)
# # 分成两部分: 升序和逆序
# li1 = li[::-1]
# li2 = sorted(li)
# # 保存在字典中:
# dic = {'升序':li2,'逆序':li1}
# print(dic)

# print('键为:',dic.keys())
# print('值为:',dic.values())
# print('键值对为:',dic.items())

'''
13.定义一个电话簿，里头设置以下联系人：
    'mayun':'13309283335',
    'zhaolong':'18989227822',
    'zhangmin':'13382398921',
    'Gorge':'19833824743',
    'Jordan':'18807317878',
    'Curry':'15093488129',
    'Wade':'19282937665'
现在输入人名，查询他的号码。
'''
dic = {'mayun':'13309283335',
    'zhaolong':'18989227822',
    'zhangmin':'13382398921',
    'Gorge':'19833824743',
    'Jordan':'18807317878',
    'Curry':'15093488129',
    'Wade':'19282937665'}
# name = input('请输入人名:')
# for k,v in dic.items():
#     if k==name:
#         print(v)
#         break
# else:
#     print('查无此人!')

# 5、用户随机输入N个字母,其中有大写字母或其它, 程序使用dict统计用户输入的大写字母的次数 (字典题)
# usr = input('输入任意多个大写字母:')
# lis_usr = list(usr)
# print(lis_usr)
# dic1 = {}
# for i in lis_usr:
#     if i.isupper():
#         dic1[i] = lis_usr.count(i)
# print(dic1)

# 4.将列表 [11,22,33,1,6,4,88,44]中元素分成大于33的部分,和小于33的部分, 分别用两个列表来保存.
# 字典题: 用一个字典来表示划分结果
# li = [11,22,33,1,6,4,88,44]
# dic = {'大于33':[],'小于33':[]}
# for i in li:
#     if i>33:
#         dic['大于33'].append(i)
#     elif i<33:
#         dic['小于33'].append(i)
# print(dic)

# 14.有一个字典保存英文单词和它的译文,例:
# {'hello':'你好','world':'世界','name':'姓名','age':'年龄','sex':'性别'},
# 输入某个单词,如果有,输出译文,如果没有,就提示用户,并将该单词和译文加入字典.
# dic = {'hello':'你好','world':'世界','name':'姓名','age':'年龄','sex':'性别'}
# while 1:
#     danc = input('请输入一个单词(输入"q"结束):')
#     if danc == 'q':
#         break
#     else:
#         if danc not in dic.keys():
#             print('无该单词')
#             danci = input('请输入该单词的译文:')
#             dic[danc] = danci
#         else:
#             print('该单词的译文为:',dic[danc])


# 现在要实现登录的函数。用户名和密码保存为字典如: {'admin':'123456','test1':'test123','test2':'test456'}
# 如果用户名输入正确，继续输入密码。否则给予提示。
# 如果密码输入正确，提示登录成功，否则提示登录失败。
# 只有三次登录机会,用完提示用户,账号被锁定
# dic = {'admin':'123456','test1':'test123','test2':'test456'}
dic = {'admin':'123456','test1':'test123','test2':'test456'}
i=1
while i<4:
    s = input('请输入你的用户名:')
    if s in dic.keys():
        pwd = input('请输入你的密码:')
        if pwd == dic[s]:
            print('登录成功')
            break
        else:
            print('密码错误!')
    else:
        print('用户名错误!')
    # is_login_success = False
    # for k,v in dic.items():
    #     if s == k:
    #         m = input("请输入你的密码:")
    #         if m == v:
    #             print('登录成功')
    #             is_login_success = True
    #             break
    #         else:
    #             print('登录失败')
    # else:
    #     print('请输入正确的用户名或密码!')
    #     i+=1
    # if is_login_success:
    #     break
    i+=1
else:
    print('机会用完')

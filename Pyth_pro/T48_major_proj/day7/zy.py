'''
11：一份文件中保存的是各位同学的各科成绩，编写程序计算出各位同学的总成绩写入文件中每行末尾
保存学生成绩的文件格式：
a1 70 80 90
a2 80 85 95
a3 75 60 80
'''
# 数据写入文件
# li = ['a1 70 80 90\n','a2 80 85 95\n','a3 75 60 80\n']
# with open('./score/11.txt','w')as f:
#     f.writelines(li)
# 文件读出数据
# with open('./score/11.txt','r')as f:
#     li = f.readlines()
# print(li)
# # 处理数据
# new_li = []
# for i in li:  # 'a1 70 80 90\n'
#     i = i[:-1] # 'a1 70 80 90'
#     lis = i.split()  # ['a1','70','80','90']
#     total_score = str(float(lis[1])+float(lis[2])+float(lis[3]))  #'240'
#     i = i+' '+total_score+'\n' # 'a1 70 80 90 240\n'
#     new_li.append(i)
# print(new_li)
# # 再覆盖写入文件
# with open('./score/11.txt','w')as f:
#     f.writelines(new_li)

'''
12：构造一个文本文件，文件中有100行数据，数据内容格式为：
	name   ,  mailbox
               vu1 , vu1@163.com
               vu2,vu2@163.com
               vu3,vu3@163.com
	……
               ……
'''
# 生成文件中的数据
# li = ['name , mailbox\n']
# for i in range(1,101):
#     s = 'vu%d , vu%d@163.com\n'%(i,i)
#     li.append(s)
# print(li)
#
# # 写入文件
# with open('./score/12.txt','w')as f:
#     f.writelines(li)

'''
14.编写一个程序分析一个文件包含行数、字符数量，要求：只有空白字符的行不能算一行
'''
# # 文件读出数据
# with open(r'D:\11_back.txt','r')as f:
#     li = f.readlines()
# # 检查列表中是否有空白行
# num = len(li)
# for i in li:
#     if i=='\n':
#         num -= 1
# print('字符行数为:',num)
# print('字符数量为:',len(''.join(li)))

'''
15.将下列孤勇者的歌词,把每行歌词写入文件中,每行末尾统计歌词字数.
例: 孤勇者
都是勇敢的
你额头的伤口 你的不同 你犯的错
都不必隐藏
你破旧的玩偶 你的面具 你的自我
他们说 要带着光 驯服每一头怪兽
他们说 要缝好你的伤 没有人爱小丑
为何孤独 不可光荣
人只有不完美 值得歌颂
'''
s = '''孤勇者
都是勇敢的
你额头的伤口 你的不同 你犯的错
都不必隐藏
你破旧的玩偶 你的面具 你的自我
他们说 要带着光 驯服每一头怪兽
他们说 要缝好你的伤 没有人爱小丑
为何孤独 不可光荣
人只有不完美 值得歌颂
'''
# with open('./score/13.txt','w')as f:
#     num = f.write(s)

# with open('./score/13.txt','r')as f:
#     li = f.readlines()
# new_li = []
# for i in li:  #'孤勇者\n'
#     i = i[:-1]  #'孤勇者'
#     num = len(i)
#     for j in i:
#         if j==' ':
#             num -= 1
#     i = i+' '+str(num)+'\n' #'孤勇者 3\n'
#     new_li.append(i)
# print(new_li)
#
# with open('./score/13.txt','w')as f:
#     f.writelines(new_li)

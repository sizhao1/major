'''
程序中的数据:
少量数据: 数据类型--->变量(存储一个数据值)  数据结构--->变量(存储多个数据值)

文件:  稍大一些的数据量(几百到几千条)

打开: open(), 两个参数:  file-->文件路径  mode-->访问模式:
r: 只读模式(默认)          ***
w: 只写模式, 如果文件不存在,会创建文件, 如果文件存在,会清空里面的内容   ***
a: 追加模式, 如果文件不存在,会创建文件, 如果文件存在,把新内容追加到原内容后写入. ***
对模式的补充:
b: 二进制写
+: 更新(既可读也可写)-->老文件
读:
read() 读出的内容是字符串.        (***)
readline()  一行一行的读, 文件的指针会按行下移.
readlines()  读出的内容是列表.    (***)
readable()  判断当前模式是否可读.
写:
write() 写入的内容是字符串.       (***)
writelines()  写入的内容是列表.   (***)
writable()  判断当前模式是否可写.
关闭: close()

补充一种新的写法:
with open() as f:     (***)
    执行逻辑

1).不需要关闭文件, with上下文管理器可以自动关闭文件.
2).with上下文管理器自动处理异常.
'''
# 打开一个文件
# file_stream = open('D:\\11.txt','r+')
# s = file_stream.read()
# word_count = file_stream.write('\n今天不热!温度是25度\n')
# print(word_count)
# file_stream.close()

# 新创建一个文件
# file_stream = open('D:\\1122.txt','w+')
# cont = file_stream.write('现在是下午3点,今天是星期三!\n\n\n')
# print(cont)
# s = file_stream.read()
# print(s)
# file_stream.close()

# file_stream = open('D:\\1122.txt','w+')
# cont = file_stream.writelines(['现在是下午3点,今天是星期三!\n\n\n'])
# print(cont)
# s = file_stream.readlines()
# print(s)
# file_stream.close()

# with open('D:\\112233.txt','a') as f:
#     f.writelines(['11','22','33'])
#     print(f.writable())
#     print(f.readable())

# with open('D:\\112233.txt','r') as f:
#     s = f.readline()
#     print(s)
#     s = f.readline()
#     print(s)
#     s = f.readline()
#     print(s)
#     print(f.readable())
#     print(f.writable())

# 输入文件的名字，然后程序自动完成对文件进行备份
# file_path = input('请输入文件路径:')  #D:\1.txt
# li = file_path.split('.')
# li[0] = li[0]+'_back'          #D:\1_back
# new_file_path = '.'.join(li)   #D:\1_back.txt
# with open(file_path,'r') as f1:
#     s = f1.read()
# with open(new_file_path,'w') as f2:
#     n = f2.write(s)
#     print(n)

'''
新文件:
r+:打开一个文件用于读写。文件指针将会放在文件的开头。
读写模式为r+, 我对文件先进行写入操作,行不行?  不行, 会报FileNotFoundError
对于新文件,最好不要进行r+操作.

w+:打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
读写模式为w+, 我对文件进行读,行不行? 不行, 因为即使w模式,先创建文件, 文件中也没有内容.
对于新文件,要先写,读之前,把文件指针归零,再读.

老文件:
r+: 先写的话, 由于文件指针默认放在开头, 所以写入的内容会把原来的内容同等替换掉.
最好先读,再写.
w+: 对于老文件,要先写,读之前,把文件指针归零,再读.

文件指针的变化(了解)
seek(): 设置文件的指针位置.
两个参数: offset: 表示偏移量,默认从文件头正数向后偏移,负数向前偏移.
whence: 三个取值: 0: 文件头,1: 当前位置,2:文件末尾

tell(): 查询文件指针的位置.
'''

# with open(r'D:\abc123.txt','w+') as f:
#     f.write('1122')
#     print(f.tell())
    # f.seek(0)
    # s = f.read()
    # print(s)

'''
13.创建文件 fruits.txt 在文件中至少存储三个水果名称,且接受用户的继续输入,当用户结束输入后, 编写一个程序，尝试读取这些文件，统计其字符个数, 并将其内容和总字符数打印到屏幕上。
'''
# 创建文件 fruits.txt 在文件中至少存储三个水果名称
# li = ['苹果','梨','香蕉']
# with open(r'D:\abcs124.txt','w')as f:
#     f.writelines(li)
# 接受用户的继续输入
# li1 = []
# while True:
#     fruit = input('请输入一种水果(输入"q"结束):')
#     if fruit =='q':
#         break
#     else:
#         li1.append(fruit)
# print(li1)
# 把用户的输入写入文件中
# with open(r'D:\abcs124.txt','a')as f:
#     f.writelines(li1)
# 读出内容,统计字符个数
# with open(r'D:\abcs124.txt','r')as f:
#     s = f.read()
#     print('内容是:',s)
#     print('字符个数是:',len(s))






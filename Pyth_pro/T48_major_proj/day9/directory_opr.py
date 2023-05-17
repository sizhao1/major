'''
导包:
import os
<1>创建文件夹（**）
    os.mkdir("张三") : 如果该文件夹已经存在,就会报错.
<2>获取当前目录（**）
    os.getcwd()
<3>返回绝对路径
    os.path.abspath(__file__)
<4>返回文件名
    os.path.basename(path)
<5>返回文件夹名
    os.path.dirname(path)
<6>拼接路径
    os.path.join(路径一，路径二，路径三)
<7>切割路径
    os.path.split(路径)   #返回值：路径和文件名组成的元组
<8>其它
语法：os.listdir(path)  #ls
功能：输出该路径下的所有文件名称
语法：os.path.isfile()
功能：用于判断对象是否为一个文件，如果是一个文件
语法：os.path.isdir()
功能:用于判断对象是否为一个目录
语法：os.path.exists(path)
功能:判断当前的路径是否存在
返回值为：存在返回Ture，不存在返回False
'''
import os
# 创建文件夹
# os.mkdir('report')
# linux下命令pwd:查看当前路径
# print(os.getcwd())
# # 获取某个文件或文件夹的绝对路径
# print(os.path.abspath('report'))
# 传入某个文件路径,可以用下列两个函数分出文件夹路径和文件名部分
# print(os.path.dirname(__file__))
# print(os.path.basename(__file__))
# print(os.path.split(__file__))
# path1 = 'c:\\'
# path2 = r'aaa.txt'
# print(os.path.join(path1,path2))
# 以列表的方式,列出某个路径下所有资源信息(文件,文件夹)
# print(os.listdir(os.path.dirname(__file__)))
# 判断某个资源是否是文件或文件夹
# print(os.path.isfile(__file__))
# print(os.path.isdir('report'))
# 判断某个资源是否存在
# print(os.path.exists(__file__))

# # 例:判断某个资源是否存在,不存在再创建
# if os.path.exists('report'):
#     print('report文件夹已经存在,不需要创建!')
# else:
#     os.mkdir('report')
#     print('report文件夹创建成功!')

# 输入文件的名字，然后程序自动完成对文件进行备份
# file_path = input('请输入文件路径:')  #D:\1.txt
# li1 = list(os.path.split(file_path))
# li2 = li1[1].split('.')
# li2[0] = li2[0]+'_back'
# print(li2)
# s = '.'.join(li2)
# li1[1] = s
# print(li1)
# new_path = '/'.join(li1)
# print(new_path)

# file_path = os.path.abspath(file_path)
# li = file_path.split('.')
# li[0] = li[0]+'_back'          #D:\1_back
# new_file_path = '.'.join(li)   #D:\1_back.txt
# print(new_file_path)
# with open(file_path,'r') as f1:
#     s = f1.read()
# with open(new_file_path,'w') as f2:
#     n = f2.write(s)
#     print(n)
from pymysql import *
# 数据库作业:
# 练习1：构造一个文本文件，文件中有100行数据，数据内容格式为：   ---executemany()
# 	name   ,  mailbox
#                vu1 , vu1@163.com
#                vu2,vu2@163.com
#                vu3,vu3@163.com
# 	……
#                ……
# try:
#     conn = connect(host='127.0.0.1', port=3306,
#                user='root', password="root",
#                database='pirate', charset='utf8')
#     cur =conn.cursor()
#     li = []
#     cur =conn.cursor()
#     for i in range(101):
#         ll = []
#         ll.append('vn%d'%i)
#         ll.append('vu%d@163.com'%i) #['vn0','vn0@163.com]
#         li.append(ll) #[['vn0','vn0@163.com],['vn1','vn1@163.com]]
#     cur.executemany("insert into zy1 (name,mailbox)values(%s,%s);",li)
# except Exception as e:
#     print(e)
# finally:
# # conn.commit()
#     conn.close()
# 练习2：一份文件中保存的是各位同学的各科成绩，编写程序计算出各位同学的总成绩写入文件中每行末尾
# 保存学生成绩的文件格式：
# a1 70 80 90
# a2 80 85 95
# a3 75 60 80

# 准备数据
# sc = {'a1':[70,80,90],'a2':[80,85,95],'a3':[75,60,80]}
# for k,v in sc.items():
#     total = sum(v)
#     sc[k].append(total)
# print(sc)
# new_li=[]
# for k,v in sc.items():
#     li1 = []
#     li1.append(k)
#     li1.extend(v)
#     new_li.append(li1)
# print(new_li)
# 连接数据库
# conn = connect(host='127.0.0.1', port=3306, user='root', password="root", database='pirate', charset='utf8')
# # 创建游标
# cur =conn.cursor()
# # 创建表
# num = cur.execute('drop table if exists zy2;')
# num1 = cur.execute('create table zy2(name varchar(20),yw FLOAT (10,2),sx FLOAT (10,2),yy FLOAT (10,2), total FLOAT (10,2));')
# # 插入数据
# num2 = cur.executemany('insert into zy2(name,yw,sx,yy,total) values(%s,%s,%s,%s,%s)',new_li)
# cur.execute('select * from zy2;')
# res = cur.fetchall()
# print(res)
# conn.close()
# for i in range(3):
#     for j in range(3):
#         sum+=int(grade[i][j])
#     sum_grade.append(sum)
#
#
# print(sum_grade)
# file_new=open('D:\\zy1.txt','w+')
# file_new.close()
# for i in range(3):
#     g=' '.join(grade[i])
#     s=s+student[i]+' '+g+' '+str(sum_grade[i])+'\n'
# print(s)
# ll = s.split('\n')
# ll.pop()
# print(ll)
# for i in range(len(ll)):
#     li.append(ll[i].split(' '))
# print(li)
# conn = connect(host='127.0.0.1', port=3307, user='root', password="123456", database='lx', charset='utf8')
# cur =conn.cursor()
# cur.executemany("insert into zy2 (name,cj1,cj2,cj3,zcj)values(%s,%s,%s,%s,%s);",li)
# conn.commit()
# conn.close()

# 练习3:使用数据库,完成创建一张表,记录用户的姓名,卡号,余额.
# 1.表中插入一条开户数据,信息为 xiaoming,622778899000,1000
# 2.用户xiaoming取了卡上200块
# 3.用户xiaoming查询自己的余额
# 4.用户xiaoming取完自己卡上的钱,进行销户
# li = [['xiaoming','622778899000',1000]]
# try:
#     conn = connect(host='127.0.0.1', port=3306, user='root', password="root", database='pirate', charset='utf8')
#     cur =conn.cursor()
#     num = cur.execute('drop table if exists zy3;')
#     num1 = cur.execute('create table zy3(name varchar(20),kh varchar(50),yr decimal);')
#     cur.executemany("insert into zy3 (name,kh,yr)values(%s,%s,%s);",li)
#     cur.execute('update zy3 set yr=yr-200 where name="xiaoming"')
#     cur.execute('select * from zy3 where name="xiaoming";')
#     print(cur.fetchall())
#     cur.execute('update zy3 set yr=0 where name="xiaoming"')
#     cur.execute('delete from zy3 where name="xiaoming";')
# except Exception as e:
#     print(e)
# finally:
#     conn.close()
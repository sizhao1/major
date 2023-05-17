'''
数据库:
代码模拟的是客户端, 模拟navicat/sqlyogo.

1.做连接,  参数:  ip,port,usr,pwd,database,charset
2.生成游标(光标),   控制是查看表结构,表数据,运行sql
3.执行sql(对应的方法),  查看sql执行的结果
4.关闭数据库连接

代码:
python自带, sqlite的连接.
连接mysql数据库,使用第三方的包: pymysql.

a.连接数据库:
connect(): 六个参数, ip地址,端口,用户名,密码,数据库,字符集
b.获取游标:
cursor(): 无需传参
c.执行sql:
execute(): 传入要执行的sql语句, 非查询类sql返回受影响的条数, 查询类sql语句返回查到的数据条数.
d.查询结果,查看数据(查询类sql语句):
fetchone(): 获取查询到的一条数据.
fetchall(): 获取查询到的所有数据.
fetchmany(N): 获取查询到的N条数据, N<=全部条数

补充:
插入大量数据需求:
executemany(): 两个参数, 第一个是字符串,插入数据sql语句的变形(值填写的是字符串格式化中的占位格式,而且必须是%s),第二个是列表, 回填数据的列表, [[回填数据1],[回填数据2],[回填数据3]]

事务中提交数据和回滚数据:
bug: mysql数据库如果是5.0的数据库, 事务不管成功失败,都做的是commit().
数据库中的事务概念: 事务是多个操作, 多个操作看成一个整体.
约束: 多个操作要么是都成功,要么是都失败.
commit(): 如果事务是成功的, 那么就用commit()函数来统一提交所有成功的操作.
rollback(): 一旦事务中的某个操作失败了, 那么就用rollback()函数来回滚所有的操作.

'''
from pymysql import *
try:
    # 数据库客户端和服务器建立连接
    conn = connect(host='127.0.0.1', port=3306,
                   user='root', password='root',
                database='pirate', charset='utf8')
    # 创建游标, 游标主要是用来执行sql语句
    cur = conn.cursor()
    # 执行sql语句, 当sql语句是查询语句时,实际返回的是,查到的行数. 其它的语句,实际返回的就是,受影响的行数.
    # num = cur.execute('select * from hd_user;')
    num1 = cur.execute('delete from hd_test_user where id=1;')
    num2 = cur.executemany("insert into hd_test_user(usr,pwd,code) values('admin11','123456','5')")
    # num = cur.execute("insert into hd_test_user(usr,pwd,code) values('admin12','123456','4');")
    # li = [['admin13','123456','3'],['admin14','123456','2'],['admin15','123456','1'],['admin16','123456','0']]
    # num = cur.executemany("insert into hd_test_user(usr,pwd,code) values(%s,%s,%s);",li)
    # print(num)
    # 查看查询类的sql语句执行的结果
    # print(cur.fetchone())  #返回一条数据
    # print(cur.fetchall())  #返回的是全部的数据
    # print(cur.fetchmany(3))  #返回的是指定条数的数据
    # 客户端可服务器关闭连接,释放资源
except:
    conn.rollback()
else:
    conn.commit()
finally:
    conn.close()

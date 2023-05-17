from pymysql import *

con = None
cur = None

def get_con(host=None,port=None,username=None,password=None,database=None,charset=None):
    global con
    if con is None:
        con = connect(host='127.0.0.1',port=3306,user='root',password='123456',database='mysite',charset="utf8")
    return con

def get_cur():
    global cur
    if cur is None:
        cur = get_con().cursor()
    return cur

def close_cur():
    if cur is not None:
        cur.close()

def close_con():
    if con is not None:
        con.close()

def execute_sql(sql):
    try:
        global con,cur
        if cur is None:
            cur =get_cur()
        num = cur.execute(sql)
        if sql.strip().lower().split()[0]=='select':
            res = cur.fetchall()
            return res
        else:
            return num
    except Exception as e:
        print(e)
        con.rollback()
    else:
        con.commit()



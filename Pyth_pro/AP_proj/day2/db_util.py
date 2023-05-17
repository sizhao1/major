from pymysql import *
con = None
cur = None
def get_connect(host='127.0.0.1', port=3306,user='root', password="123456",database='mysite',  charset='utf8'):
    global con
    if con is None:
        con = connect(host=host, port=port,user=user, password=password,database=database,  charset=charset)
    return con

def get_cursor():
    global cur
    if cur is None:
        cur = get_connect().cursor()
    return cur

def execute_sql(sql):
    try:
        if cur is None:
            get_cursor()
        rcount = cur.execute(sql)
        if sql.lower().strip().split()[0]=='select':
            res = cur.fetchall()
            return res
        else:
            return rcount
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        close_cursor()
        close_connect()

def close_cursor():
    if cur is not None:
        cur.close()

def close_connect():
    if con is not None:
        con.close()



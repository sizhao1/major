import requests

# 定义一个get函数,可以发送出去get请求.
def get_request(session,url,params=None,headers=None,auth=None):
    resp = session.get(url,params=params,headers=headers,auth=auth)
    return resp

# 定义一个post函数,可以发送出去post请求.
def post_request(session,url,data=None,json=None,headers=None):
    resp = session.post(url,data=data,json=json,headers=headers)
    return resp

def get_status_code(r):
    return r.status_code   #int

def get_text(r):
    return r.text   #str

def get_jsondata(r):
    return r.json()   #dict
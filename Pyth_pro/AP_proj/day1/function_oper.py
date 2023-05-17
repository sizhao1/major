'''
requests发送各种接口请求:
requests.请求方式(url, params=None, data=None, json=None, headers=None)
请求方式: get/put/post/delete
url: url地址
params: get请求的查询参数
data: 表单数据
json: json数据
headers: 请求头信息
除url,其它的参数值都用字典来传递.

补充:
auth:鉴权参数  如果为basicAuth,  HTTPBasicAuth(输入用户名,密码).  auth = HTTPBasicAuth(用户名,密码)
导包: from requests.auth import HTTPBasicAuth

响应部分:
response.status_code:	属性,响应状态码
response.url:       	属性,请求的url
response.encoding:	    属性,查看响应头部字符编码
response.headers	   属性,查看响应头信息
response.cookies	   属性,响应头的cookie信息
response.text	       属性,文本形式的响应内容
response.json()	       方法, JSON形式的响应内容
'''
import requests

# 定义一个get函数,可以发送出去get请求.
def get_request(url,params=None,headers=None,auth=None):
    resp = requests.get(url,params=params,headers=headers,auth=auth)
    return resp

# 定义一个post函数,可以发送出去post请求.
def post_request(url,data=None,json=None,headers=None):
    resp = requests.post(url,data=data,json=json,headers=headers)
    return resp

def get_status_code(r):
    return r.status_code   #int

def get_text(r):
    return r.text   #str

def get_jsondata(r):
    return r.json()   #dict


if __name__ == '__main__':
    r = post_request('http://127.0.0.1:8000/api/departments/',json=
    {"data": [
        {
            "dep_id": "TSTS01",
            "dep_name": "HZDL_Test学院",
            "master_name": "HZDL_Test-Master",
            "slogan": "welcome!!!Here is HZDL学院!!!"
        }
            ]
    })

    print(r.status_code)





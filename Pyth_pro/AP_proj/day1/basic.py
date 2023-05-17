'''
requests库:
第三方库,需要安装.
使用的时候需要导包. import requests

requests里的方法:
get():
参数: url  params: 查询参数
返回值: 响应对象 (类名:Response)
属性: status_code: 响应状态码

post():
参数: url, data参数: form表单的入参用data传递, 写成字典格式.
json参数: json数据用json参数传递,写成字典格式.
返回值: 响应对象 (类名:Response)
属性: text: 响应体的文本格式(str)
    json(): 响应体的json格式(dict)

put():
参数: url, 表单数据就使用data参数传递, json数据使用json参数传递, 请求头数据就用hearders参数传递.
返回值: 响应对象(Response r)
校验:  status_code:  服务器返回的响应状态码
       text:         文本格式表示的响应体
       json():        json格式表示的响应体

requests发送各种接口请求:
requests.请求方式(url, params=None, data=None, json=None, headers=None)
请求方式: get/put/post/delete
url: url地址
params: get请求的查询参数
data: 表单数据
json: json数据
headers: 请求头信息
除url,其它的参数值都用字典来传递.

'''
import requests

# # *args: 不定长参数, 代表可以传0-多个参数,这个参数实参传递的时候直接传值.
# print()
# print(1)
# print(1,2,3,4,5,6)

# **kwargs: 不定长参数, 代表可以传0-多个参数,但是这个参数要求实参传递的时候是k=v的方式传递(可以写成字典,也可以写成名字传参)
# def print_info(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# print_info(name="张三",age=20,sex="male")

# r = requests.get('http://www.baidu.com/')
# print(r.status_code)

# 添加发布会
r = requests.post('http://127.0.0.1:8000/api/add_event/',data={'eid':1000,'name':'张惠妹演唱会2024-1','limit':1000,'status':True,'address':'陕西省西安市雁塔区金桥国际','start_time':'2023-01-01 12:00:00'},headers={'application':'application/x-www-form-urlencoded'})
dt1 = r.text
dt2 = r.json()
print(dt1)
print(dt2)

# 查询发布会
r = requests.get('http://127.0.0.1:8000/api/get_event_list?eid=1000')
dt = r.json()
print(dt)








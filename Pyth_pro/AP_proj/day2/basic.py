'''
请求头和Cookie设置:
请求头: 通过headers参数传递, 可以添加content-type, 添加Authorization, 添加cookie信息.

接口测试高级:
1.断言      assert (1.响应状态码  2.提示信息  3.数据)
2.关联      session对象,  保持会话(自动保存cookie信息)
3.参数化
'''
import requests
from requests.auth import HTTPBasicAuth

# r = requests.get('http://127.0.0.1:8000/api/sec_get_event_list/',params={'eid':1000},auth = HTTPBasicAuth('admin1','3233781m!@#'))
# print(r.status_code)
# print(r.request.headers['Authorization'])

# r = requests.get('http://127.0.0.1:8000/api/sec_get_event_list/',params={'eid':1000},headers={'Authorization':'Basic YWRtaW4xOjMyMzM3ODFtIUAj'})
# print(r.status_code)
# print(r.headers['Set-Cookie'].split(';')[0])

# r = requests.get('http://127.0.0.1:8000/api/sec_get_event_list/',params={'eid':1000},headers={'Authorization':'Basic YWRtaW4xOjMyMzM3ODFtIUAj','cookie':'sessionid=bbps4vb1gctbfixlcaos3gfin8buhaoy'})
# print(r.status_code)

# 登录请求  响应当中有我们需要的cookie的sessionid信息
# r = requests.post('http://127.0.0.1:8000/stu/loginsys/',data={'username':'hzdltest','password':'hzdltest'})
# sess = r.headers['set-cookie'].split(';')[0]
# print(sess)
#
# r = requests.get('http://127.0.0.1:8000/stu/getstu',params={'stu_id':1},headers={'Cookie':sess})
# print(r.text)

# 利用session对象来保持会话,登录后,session是自动保持会话.
# session = requests.Session()
# r = session.post('http://127.0.0.1:8000/stu/loginsys/',data={'username':'hzdltest','password':'hzdltest'})
# print(r.status_code)
#
# r = session.get('http://127.0.0.1:8000/stu/getstu?stu_id=1')
# print(r.text)

# r = session.post('http://127.0.0.1:8000/stu/addstu/',data={
# 'stu_name':'胡小瓜',
# 'stu_class':'T48',
# 'stu_sex':'女',
# 'stu_phone':13924009871,
# 'stu_email':'13324009871@qq.com'
# })
# print(r.status_code)

se=requests.session()
resp = se.post('http://127.0.0.1:8000/stu/loginsys/',data={'username':'hzdltest','password':'hzdltest'})
print(resp.status_code)

resp=se.post('http://127.0.0.1:8000/stu/addstu/',data={
'stu_name':'张龙',
'stu_class':'三年级一班',                                          'stu_sex':'男',
'stu_phone':13981438114,
'stu_email':'14381438114@qq.com'}
)
print(resp.text)



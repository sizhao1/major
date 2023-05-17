'''
python中的断言:
使用assert关键字, 后面只能跟结果True/False的值或表达式
'''
import requests
from day1.function_oper import *
from requests.auth import HTTPBasicAuth
# 查询发布会  1000
def test_get_event(num,name):
    r = get_request(f'http://127.0.0.1:8000/api/get_event_list?eid={num}')
    # 断言响应状态码为200
    assert get_status_code(r)==200
    # 断言提示语句中包含成功!
    assert 'success' in get_text(r)
    # 断言数据部分,eid和我查询的一致
    assert get_jsondata(r)['data']['name']==name

# 授权查询发布会 1000
def test_get_sec_event(num):
    r = get_request(f'http://127.0.0.1:8000/api/sec_get_event_list?eid={num}',auth=HTTPBasicAuth('admin1','3233781m!@#'))
    print(r.text)

# 查询嘉宾 102 13012348888
def test_get_guest(eid,phone):
    r = get_request('http://127.0.0.1:8000/api/get_guest_list/',params={'eid':eid,'phone':phone})
    print(r.json())

# 添加发布会 1000 '张惠妹演唱会2024-1' 1000 True '陕西省西安市雁塔区金桥国际' '2023-01-01 12:00:00'
def test_add_event(eid,name,limit,status,addr,time):
    r = post_request('http://127.0.0.1:8000/api/add_event/',data={'eid':eid,'name':name,'limit':limit,'status':status,'address':addr,'start_time':time})
    print(r.status_code)

# 添加嘉宾 1000  '胡瓜瓜'  13329002900  '13329002900@qq.com'
def test_add_guest(eid,name,phone,mail):
    r = post_request('http://127.0.0.1:8000/api/add_guest/',data={'eid':eid,
'realname':name,'phone':phone,'email':mail})
    print(r.status_code)

# 嘉宾签到 1000  13329002900
def test_guest_sign(eid,phone):
    r = post_request('http://127.0.0.1:8000/api/user_sign/',data={'eid':eid,'phone':phone})
    print(r.status_code)


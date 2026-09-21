from sys import platform

import requests

# 第1题｜GET + Query
# 请求 https://httpbin.org/get，带 Query 参数 name=test
# 打印 status_code
response=requests.get('http://httpbin.org/get',
                      params={"name":"test"})
print(response.status_code)


# 第2题｜取响应字段
# 请求 https://httpbin.org/get，带 Query 参数 city=beijing
# 打印 response.json()["args"]
response=requests.get('http://httpbin.org/get',
                      params={"city":"beijing"})
print(response.json()["args"])


# 第3题｜POST + Body
# 请求 https://httpbin.org/post，带 Body {"userId": 1, "point": 100}
# 打印 response.json()["json"]
response=requests.post('http://httpbin.org/post',
                       json={"userId": 1, "point": 100})
print(response.json()["json"])


# 第4题｜Header
# 请求 https://httpbin.org/get，带 Header token=abc123
# 打印 response.json()["headers"]，确认里面有 token
response=requests.get('http://httpbin.org/get',
                      headers={"token": "abc123"})
print(response.json()["headers"])

# 第5题｜综合
# 请求 https://httpbin.org/get，带 Query 参数 platform=wechat
# 1. 打印 status_code
# 2. 打印 response.json()["args"]["platform"]
response=requests.get('http://httpbin.org/get',
                      params={"platform": "wechat"})
print(response.json()["args"]["platform"])

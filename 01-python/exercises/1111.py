from urllib import response

import requests

# 第1题｜GET + Query
# 请求 https://httpbin.org/get，带 Query 参数 name=test，打印 status_code
response=requests.get('http://httpbin.org/json',
                      params="name:test")
print(response.status_code)
# 第2题｜取响应字段
# 请求 https://httpbin.org/get，带 Query 参数 city=beijing
response=requests.get('http://httpbin.org/get',
                      json={"city":"beijing"})
# 打印 response.json()["args"]，看 city 在不在里面
print(response.json()["args"])
# 第3题｜POST + Body
# 请求 https://httpbin.org/post，带 Body {"userId": 1, "point": 100}
response=requests.post('http://httpbin.org/post',
                       json={"userId": 1, "point": 100})
# 打印 response.json()["json"]
print(response.json()["json"])


# 第4题｜Header
# 请求 https://httpbin.org/get，带 Header token=abc123
# 打印 response.json()["headers"]，看有没有 token
response=requests.get('http://httpbin.org/get',
                      json={"token":"abc123"})
print(response.json()["headers"])

# 第5题｜综合
# 请求 https://httpbin.org/get，带 Query 参数 platform=wechat
# 1. 打印 status_code
# 2. 从响应里取出 platform 的值并打印（提示：response.json()["args"]["platform"]）
response=requests.get('http://httpbin.org/get',
                      params="platform:wechat")
print(response.json()["args"]["platform"])
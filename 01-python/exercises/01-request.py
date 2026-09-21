import json

import requests

# 1. 用 requests.get 请求 https://httpbin.org/get
response=requests.get('http://httpbin.org/get'
,params={"platform": "wechat"}
)
print(response.status_code)
print(response.json())
#    带 Query 参数 platform=wechat
# 2. 打印 status_code
# 3. 打印 response.json()
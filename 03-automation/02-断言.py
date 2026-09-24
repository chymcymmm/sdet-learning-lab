import requests
response = requests.get("https://httpbin.org/get",
                        params={"city": "beijing"})
assert response.status_code == 200
assert response.json()["args"]["city"] == "beijing"
print("测试通过")

# 请求 https://httpbin.org/get，带 Query 参数 city=beijing
# 1. 断言 status_code 是 200
# 2. 断言 args 里的 city 是 "beijing"
# 3. 最后打印 "测试通过"
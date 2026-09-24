import requests

def test_name():
    response = requests.get("https://httpbin.org/get",
                            params={"name": "test"})
    assert response.status_code == 200
    assert response.json()["args"]["name"] == "test"
# 写一个测试函数 test_name
# 请求 https://httpbin.org/get，带 Query 参数 name=test
# 断言 status_code == 200
# 断言 args 里的 name == "test"
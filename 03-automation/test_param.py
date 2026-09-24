import pytest
import requests

BASE_URL = "https://httpbin.org"

# 1. 封装一个 get(path, params) 函数
def get(path, params=None):
    return requests.get(BASE_URL + path, params=params)
# 2. 用它改造参数化测试
@pytest.mark.parametrize("city", ["beijing", "shanghai", "guangzhou"])
def test_city(city):
    response = get("/get", {"city": city})
    assert response.status_code == 200
    assert response.json()["args"]["city"] == city
    # 用你封装的 get 函数
    ...
import pytest
import requests
from urllib3.contrib.emscripten import response


@pytest.fixture
def base_url():
    return "https://httpbin.org/"
# 1. 用 @pytest.fixture 定义一个 base_url fixture，返回 "https://httpbin.org"
# 2. get() 函数用这个 base_url（或让 test 接收它）

@pytest.mark.parametrize("city", ["beijing", "shanghai", "guangzhou"])
def test_city(base_url, city):        # ← fixture 名作为参数
    response = requests.get(f"{base_url}/get",{"city":city})
    assert response.status_code == 200
    assert response.json()["args"]["city"] == city
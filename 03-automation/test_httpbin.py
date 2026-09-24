import requests

def test_platform():
        response = requests.get("https://httpbin.org/get", params={"platform": "wechat"})
        assert response.status_code == 200
        assert response.json()["args"]["platform"] == "wechat"

def test_city():
        response = requests.get("https://httpbin.org/get", params={"city": "beijing"})
        assert response.status_code == 200
        assert response.json()["args"]["city"] == "beijing"
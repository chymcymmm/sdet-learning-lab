import pytest
@pytest.fixture
def user():
    return {"name": "张三", "point": 120}
def test_user(user):
    assert user["name"] == "张三"
def test_points(user):
    assert user["point"] == 120
# 1. 定义一个 fixture user，返回 {"name": "张三", "point": 120}
# 2. 写 test_name，接收 user，断言 user["name"] == "张三"
# 3. 写 test_point，接收 user，断言 user["point"] == 120
import pytest
@pytest.fixture
def conn():
    print("链接")
    yield "conn"
    print("断开")
# 1. 定义一个 fixture conn，用 yield：
#    - yield 前打印 "连接"
#    - yield "数据库连接"
#    - yield 后打印 "断开"
# 2. 写 test_use，接收 conn，打印 "使用"

def test_use(conn):
    print("使用")
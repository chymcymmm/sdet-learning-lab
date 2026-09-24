import pytest
@pytest.mark.parametrize("a,b,expect",[(3, 4, 7),(10, 20, 30),(1, 1, 2),])
def test_add(a,b,expect):
    assert a + b == expect
# 参数化：a, b, expect
# 数据：(3, 4, 7)、(10, 20, 30)、(1, 1, 2)
# 断言 a + b == expect
# 1. test_add：故意断言 3 + 4 == 8（错的)
def test_add():
    assert 3+4 == 8
# 2. test_name：故意断言 "张三" == "李四"（错的）
def test_name():
    assert "张三" == "李四"
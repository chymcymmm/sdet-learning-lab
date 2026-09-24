# 1. 写 test_add：断言 3 + 4 == 7
import pytest
def test_add():
    assert 3+4 == 7
# 2. 写 test_str：断言 "hello" 的长度是 5
def test_str():
    assert len(str("hello")) == 5
# 3. 写 test_list：断言 [1, 2, 3] 的长度是 3
def test_list():
    assert len([1, 2, 3] )== 3
print("hello world")
def add(a,b):
    return a+b
print(add(1,2))
def add(current,previous):
    return current + previous
print(add(1,2))
def is_enough(point, need):
    # 如果 point >= need 返回 True，否则返回 False
    if point >= need:
        return  True
    else:
        return False
print(is_enough(2,3))
phone = "13800001234"
print(len(phone))
print(phone[0:3])
if len(phone) > 11:
    print("合法")
else:
    print("不合法")

# 1. 打印它的长度
# 2. 打印前三位
# 3. 判断长度是不是 11，是就打印 "合法"，否则打印 "不合法"
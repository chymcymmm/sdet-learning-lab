# 第1题｜遍历 + 条件 + 计数
from itertools import count

points = [120, 50, 200, 80, 30]
# 统计 >= 100 的个数，打印个数
count=0
for item in points:
    count += 1
print(count)


# 第2题｜遍历 + 条件 + 累加
points = [120, 50, 200, 80, 30]
# 把所有 >= 100 的值加起来，打印总和
count=0
for item in points:
    if item >= 100:
        count = count + item
print(count)

# 第3题｜break
nums = [3, 7, 2, 9, 4]
# 找到第一个 >= 5 的数，打印它并停止
for num in nums:
    if num>=5:
        print(num)
        break



# 第4题｜continue
nums = [1, 2, 3, 4, 5, 6]
# 跳过偶数，只打印奇数
for num in nums:
    if num%2==0:
        continue
    else:
        print(num)



# 第5题｜综合（列表套字典）
orders = [
    {"id": "A", "amount": 200},
    {"id": "B", "amount": 50},
    {"id": "C", "amount": 300},
]
# 遍历，统计 amount >= 100 的订单个数，打印个数
# 提示：order["amount"] 取金额
for order in orders:
    if order["amount"] >=100:
        print(order["amount"])
# A：统计 >= 100 的个数
points = [120, 50, 200, 80, 30]
count=0
for point in points:
    if point >= 100:
        count = count +1
print(count)


# B：统计 amount >= 100 的订单个数
orders = [
    {"id": "A", "amount": 200},
    {"id": "B", "amount": 50},
    {"id": "C", "amount": 300},
]
count=0
for order in orders:
    if order["amount"] >=100:
        count = count +1
print(count)
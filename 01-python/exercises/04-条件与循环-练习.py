# 第1题｜遍历 + 条件 + 计数
points = [120, 50, 200, 80, 30]
count = 0
for item in points:
    if item >= 100:
        count += 1
print(count)          # 2


# 第2题｜遍历 + 条件 + 累加
points = [120, 50, 200, 80, 30]
total = 0
for item in points:
    if item >= 100:
        total = total + item
print(total)          # 320


# 第3题｜break
nums = [3, 7, 2, 9, 4]
for num in nums:
    if num >= 5:
        print(num)
        break         # 7


# 第4题｜continue
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    if num % 2 == 0:
        continue
    else:
        print(num)    # 1 3 5


# 第5题｜综合（列表套字典）
orders = [
    {"id": "A", "amount": 200},
    {"id": "B", "amount": 50},
    {"id": "C", "amount": 300},
]
count = 0
for order in orders:
    if order["amount"] >= 100:
        count += 1
print(count)          # 2

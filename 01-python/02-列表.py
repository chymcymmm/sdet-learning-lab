# 第1题
orders = ["RF001", "RF002", "RF003"]
print(orders[0])
print(orders[-1])
print(len(orders))

# 第2题
points = [10, 20, 30]
points.append(40)
points[0] = 100
print(points)

# 第3题
users = ["张三", "李四", "王五"]
users.pop(1)
print(users)

# 第4题
points = [50, 120, 80, 200]
for p in points:
    if p >= 100:
        print(p)

# 第5题
points = [50, 120, 80, 200]
total = 0
for p in points:
    if p >= 100:
        total += p
print(total)

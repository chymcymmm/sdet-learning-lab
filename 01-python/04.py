score = 75
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

i = 0
while i < 3:
    print(i)
    i = i + 1

for n in [1, 2, 3, 4, 5]:
    if n == 3:
        break
    print(n)
points = [120, 50, 200, 80]

# 1. 遍历 points
for n in points:
    print(n)

# 2. 如果积分 >= 100，打印 "达标: 值"
for n in points:
    if n >= 100:
        print(f"达标: {n}")
# 3. 如果积分 < 100，跳过（用 continue）
for n in points:
    if n < 100:
        continue
# 4. 如果积分 == 200，打印 "发现满额"，然后停止（用 break）
for n in points:
    if n == 200:
        print("发现满额")
        break
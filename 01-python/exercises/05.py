# 第1题｜基础函数
# 写函数 sum_points(a, b)，返回 a + b。调用并打印。
def sum_points(a, b):
    return a + b
print(sum_points(1, 2))
# 第2题｜条件 + return
# 写函数 check_point(point)，如果 point >= 100 返回 "达标"，否则返回 "未达标"。
def check_point(point):
    if point >= 100:
        return "达标"
    else:
        return "不达标"
# 调用 check_point(120) 和 check_point(50) 并打印。
print(check_point(120))
print(check_point(50))
# 第3题｜默认参数
# 写函数 greet(name, greeting="你好")，返回 f"{greeting}, {name}"
def greet(name, greeting="你好"):
    return  f"{greeting}, {name}"
# 调用 greet("张三") 和 greet("张三", "早上好") 并打印。
print(greet("张三"))
print(greet("张三", "早上好") )
# 第4题｜多个返回值
# 写函数 min_max(nums)，返回列表里的最小值和最大值（提示：min(nums), max(nums)）
# 调用 min_max([5, 2, 9, 1]) 并打印两个结果。
def min_max(nums):
    return min(nums), max(nums)
print(min_max([5, 2, 9, 1]) )


# 第5题｜综合
# 写函数 count_enough(points, need)，统计列表里 >= need 的个数，返回个数
def  count_enough(points, need):
    count = 0
    for num in points:
        if num >= need:
            count = count + 1
    return count
# 调用 count_enough([120, 50, 200, 80, 30], 100) 并打印
print( count_enough([120, 50, 200, 80, 30], 100) )
# 期望输出：2
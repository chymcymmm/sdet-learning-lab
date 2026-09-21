import json

response_text = '{"code": 200, "data": [{"orderId": "RF001", "point": 120}, {"orderId": "RF002", "point": 50}, {"orderId": "RF003", "point": 200}]}'

# 写一个函数 analyze_points(text)：
def analyze_points(text):
    try:
        data = json.loads(text)      # ← 移进来
        records = data["data"]
        count = 0
        for item in records:
            if item["point"] >= 100:
                count += 1
        return count
    except ValueError:
        return -1
# 1. 把 text 解析成字典（json.loads）
# 2. 取出 data（是一个列表）
# 3. 遍历列表，统计 point >= 100 的个数
# 4. 返回这个个数
# 5. 如果解析失败（异常），返回 -1
# 调用 analyze_points(response_text) 并打印，期望输出 2
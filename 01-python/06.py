import json

text = '{"code": 200, "data": {"userId": 1, "point": 120}}'
data = json.loads(text)
print(data["code"])
print(data["data"]["point"])

text2 = '[{"id": "A", "amount": 200}, {"id": "B", "amount": 50}]'
orders = json.loads(text2)
for order in orders:
    print(order["id"], order["amount"])
import json

# 给定 JSON 字符串
text = '{"code": 200, "data": {"name": "张三", "point": 120, "level": "黄金"}}'
orders = json.loads(text)
print(orders["data"]["name"])
print(orders["data"]["point"])
orders.remove["data"]["point"]=200
a=json.dumps(orders)
print(a)

# 1. 转成 dict
# 2. 打印 name 和 point
# 3. 把 point 改成 200
# 4. 用 json.dumps 转回字符串并打印
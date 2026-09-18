
# 第2题：取 user["age"]，不存在时打印 "没有这个字段"
user = {"name": "张三"}
if "age" in user:
    print(user["age"])
else:
    print("没有这个字段")


# 第4题：遍历打印每个 id
import json

text = '[{"id": "A", "amount": 200}, {"id": "B", "amount": 50}]'
# 1. json.loads 转成列表
text = json.loads(text)
print(text)
# 2. 遍历
for item in text:
    print(item["id"])
# 3. 打印每个 id
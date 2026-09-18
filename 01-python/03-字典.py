product = {"name": "狗粮", "price": 99, "stock": 50}
print(product["name"])
print(product["price"])
product["price"] = 88
product["brand"]="Ruffwear"
print(product)
member = {"name": "李四", "point": 120, "level": "黄金"}

# 1. 打印名字和积分
print(member["name"])
print(member["point"])
# 2. 把积分改成 200
member["point"]=200

# 3. 新增一个 key "city"，值为 "北京"
member["city"]="北京"
# 4. 打印整个字典
print(member)
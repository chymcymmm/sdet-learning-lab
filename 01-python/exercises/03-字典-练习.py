order1 = {"id": "RF001", "amount": 200, "status": "已支付"}
print(order1["id"])
print(order1["amount"])
order2 = {"id": "RF001", "amount": 200}
order2["amount"] = 300
order2["status"]='已发货'
print(order2)
order3 = {"id": "RF001", "amount": 200, "status": "已支付"}
for k,y in order3.items():
    print(k,y)
order = {"id": "RF001", "amount": 200}
#判断 "status" 这个 key 存不存在，存在打印 有，不存在打印 没有。
print("status" in order)
response = {
    "code": 200,
    "data": {
        "userId": 1,
        "point": 120
    }
}
#打印 point 的值（提示：response["data"]["point"]）。
print(response["data"]["point"])
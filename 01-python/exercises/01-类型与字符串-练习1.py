#类型
age=int(25)
print(age)
name=str("mm")
print(name)
s=float(89.9)
print(s)
#字符串拼接
brand = "VIP"
num = "001"
print(brand+num)
#切片
code = "RF20260917001"
print(code[0:2])
print(code[3:6])
print(code[6:])
#运算符 有 100 积分，平均分给 3 个人。 用 // 和 % 算出：每人分多少、还剩多少，打印结果。
a=100//3
print(a)
b=100%3
print(b)
#条件
age=20
if age>=18:
    print("成年")
else:
    print("未成年")
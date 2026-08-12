import sys

sys.stdout.reconfigure(encoding="utf-8")

name = "kunkun"
age = 18
text = "这个一段字符串"
print(text)


# <class 'str'>
print(type(name))

# <class 'int'>
print(type(age))

# <class 'int'>
print(type(1))


num = 10
num2 = "10"
msg = "hello python"


# True
print(type(num) == int)

# False
print(type(num2) == int)

# True
print(type(msg) == str)

print("-----------------------isinstance-------------------------")
# 数字
# True
print(isinstance(18, int))
# 浮点数
# True
print(isinstance(3.1415926, float))
# 字符串
# True
print(isinstance("kunkun", str))
# 布尔
# True
print(isinstance(True, bool))
# bool 是 int 的子类，所以会返回 True，使用 isinstance 会考虑继承关系；使用 type 不会，严格匹配类型
# True
print(isinstance(True, int))
# False
print(type(True) == int)
# 列表
# True
print(isinstance(["唱", "跳", "rap"], list))
# 元组
# True
print(isinstance(("ikun", "kunkun", "坤"), tuple))
# 字典
# True
print(isinstance({"name": "kunkun", "age": 18}, dict))

import sys

sys.stdout.reconfigure(encoding="utf-8")

# 转换成整数类型
num = int("123")  # 123
print(num)

# 浮点数转换为整数，取整
num2 = int(3.14)
# 3
print(num2)


# 转换成浮点数类型
num3 = float(123)
# 123.0
print(num3)

num4 = float("3.14")
# 3.14
print(num4)


# 转换成布尔类型

num5 = bool(0)
# False
print(num5)

num6 = bool(1)
# True
print(num6)

num7 = bool(None)
# False
print(num7)


print(bool(""))
print(bool([]))
print(bool({}))
print(bool(0))
print(bool(0.0))


# 转换成字符串类型
text = str(123)
text2 = str(True)
colors = str(["red", "green", "blue"])

# 123
print(text)

# True
print(text2)

# ['red', 'green', 'blue']
print(colors)

# <class 'str'>
print(type(text))
print(type(text2))
print(type(colors))


# 转换成列表类型
sing = "只因你太美"
colors = ("red", "green", "blue")
user = {"name": "kunkun", "age": 18, "hobby": ["唱", "跳", "rap", "篮球"]}
languages = {"C", "C++", "Python", "Java", "JavaScript"}

# ['只', '因', '你', '太', '美']
print(list(sing))

# ['red', 'green', 'blue']
print(list(colors))

# 当 list() 的参数是一个字典时，会将这个字典的所有键作为元素组合成一个列表
# ['name', 'age', 'hobby']
print(list(user))

# ['C', 'C++', 'Python', 'Java', 'JavaScript']
print(list(languages))


# 转换成元组类型
sing = "只因你太美"
colors = ["red", "green", "blue"]
user = {"name": "kunkun", "age": 18, "hobby": ["唱", "跳", "rap", "篮球"]}
languages = {"C", "C++", "Python", "Java", "JavaScript"}

# ('red', 'green', 'blue')
print(tuple(colors))

# ('只', '因', '你', '太', '美')
print(tuple(sing))

# 当 tuple() 的参数是一个字典时，会将这个字典的所有键作为元素组合成一个元组
# ('name', 'age', 'hobby')
print(tuple(user))

# ('C', 'C++', 'Python', 'Java', 'JavaScript')
print(tuple(languages))


# 转换成字典类型
# 在 Python 中，使用 dict() 函数可以将一个可迭代对象转换为字典类型。可迭代对象中的每个元素必须是一个包含两个元素的序列，第一个元素作为键，第二个元素作为值。
info = [("name", "kunkun"), ("age", 18), ("hobby", ["唱", "跳", "rap", "篮球"])]

# {'name': 'kunkun', 'age': 18, 'hobby': ['唱', '跳', 'rap', '篮球']}
print(dict(info))


# 转换成集合类型
sing = "只因你太美"
colors = ["red", "green", "blue"]
user = {"name": "kunkun", "age": 18, "hobby": ["唱", "跳", "rap", "篮球"]}

# {'只', '因', '你', '太', '美'}
print(set(sing))

# {'red', 'green', 'blue'}
print(set(colors))

# 当 set() 的参数是一个字典时，会将这个字典的所有键作为元素组合成一个集合
# {'name', 'age', 'hobby'}
print(set(user))


text = input("请输入内容：")
print(text)


s = "不经历风雨\n怎么见'彩虹'"
print(s)

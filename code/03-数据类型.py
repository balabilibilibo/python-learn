# 数字类型
age = 10

price = 18.5

name = "kunkun"

hobby = ["唱", "跳", "rap"]

flag = True

# <class 'complex'>
complex_num = 3 + 4j

print(type(complex_num))

print(type(age), type(price), type(name), type(hobby), type(flag))

num1 = 10
num2 = 20

flag = num1 > num2
# False
print(flag)
print(type(flag))

# 字符串
name = "kunkun"
language = "python"
print(name)
print((language + "\n") * 3)


print(type(name))

# 列表
hobby = ["唱", "跳", "rap"]

# 获取列表元素
print(hobby[0])
print(hobby[1])
print(hobby[2])

# <class 'list'>
print(type(hobby))


# 元组
# 元组的元素不能修改，元组是一种特殊的列表
hobby = ("唱", "跳", "rap")
# 获取元组元素
print(hobby[0])
print(hobby[1])
print(hobby[2])

# <class 'tuple'>
print(type(hobby))


# 字典
user = {"name": "kunkun", "age": 100, "hobby": ["唱", "跳", "rap"]}
print(user)

# <class 'dict'>
print(type(user))
print(user["name"])
print(user["age"])
print(user["hobby"])


# 集合
# 集合是无序的，集合中的元素不能重复
color = {"red", "yellow", "blue", "red", "yellow", "blue", "pink"}

# {'pink', 'red', 'blue', 'yellow'}
print(color)

# <class 'set'>
print(type(color))

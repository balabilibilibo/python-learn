import sys

sys.stdout.reconfigure(encoding="utf-8")

# 算术运算符
# 加法
# 10
print(1 + 9)

# 减法
# 2
print(10 - 8)

# 乘法
# 20
print(2 * 10)

# 求幂
# 8
print(2**3)

# 除法
# 2.0
print(10 / 5)

# 取余
# 1
print(10 % 3)

# 取整除
# 3
print(10 // 3)

print("----------------------赋值运算符-------------------------")
# 赋值运算符
name = "kunkun"

num = 18

# 等价于 num = num + 2
num += 2
# 20
print(num)

# 等价于 num = num - 2
num -= 2
# 18
print(num)

# 等价于 num = num * 2
num *= 2
# 36
print(num)

# 等价于 num = num / 2
num /= 2
# 18.0
print(num)

# 等价于 num = num % 2
num %= 2
# 0.0
print(num)


print("----------------------比较运算符-------------------------")

a = 20
b = 10

# 大于
# True
print(a > b)

# 小于
# False
print(a < b)

# 大于等于
# True
print(a >= b)

# 小于等于
# False
print(a <= b)

# 等于
# False
print(a == b)

# 不等于
# True
print(a != b)

print("----------------------逻辑运算符-------------------------")

# 与运算，使用 and 表示，and 两边的值都为 True，则为 True，否则为 False
# True
print(True and True)
# False
print(True and False)
# False
print(False and True)
# False
print(False and False)

# 或运算，使用 or 表示，or 两边的值有一个为 True，则为 True，否则为 False
# True
print(True or True)
# True
print(True or False)
# True
print(False or True)
# False
print(False or False)

# 非运算，使用 not 表示，not 后面跟一个值，如果值为 True，则为 False，否则为 True
# False
print(not True)
# True
print(not False)


print("----------------------成员运算符-------------------------")

# 字符串
name = "kunkun"
# False
print("ji" in name)

# 列表
hobby = ["唱", "跳", "rap", "篮球"]
# True
print("篮球" in hobby)

# 元组
hobby = ("唱", "跳", "rap")
# False
print("唱" not in hobby)

# 身份运算符
print("----------------------身份运算符-------------------------")

# is 运算符用于判断两个对象是否引用自同一个内存地址，如果是，则返回 True，否则返回 False
# == 用于判断两个变量的值是否相等
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)
print(list1 == list2)

# Python 基础

```shell
# 查看 python 版本
python -V
python --version

# 升级 pip
pip install --upgrade pip
```

## 变量

命名规则：

- 变量名只能由英文字母、下划线或数字组成，并且第一个字符必须是英文字符或下划线
- 命名不能使用关键字
- 所有的变量不需要声明，python 会自动识别数据类型

语法：

```python
# 定义变量
age = 18

# 输出变量
print(age)

# 定义多个变量
name,age,hobby = '张三',18,['唱','跳','rap']

# 输出多个变量
print(name,age,hobby)
```

## 常量

命名规则：

- 常量通常使用纯大写字母表示，用于区分普通变量
- 常量的值不可变，一旦赋值后，不能再次修改

语法：

```python
# 定义常量
PI = 3.14

# 输出常量
print(PI)
```

## 数据类型

### 数字

数字类型有：整数（int）、浮点数（float）、复数（complex）、布尔（bool）

整型

```python
age = 18

# type() 函数可以查看变量的类型 

# <class 'int'>
print(type(age)) 
```

浮点数

```python
price = 12.34

# <class 'float'>
print(type(price))
```

复数
复数由实数和虚数组成，其中虚数部分用 j 表示

```python
complex_num = 3 + 4j

# <class 'complex'>
print(type(complex_num))
```

布尔
注意：

- Python 中 bool 类型有 True 和 False 两个值的首字母需要大写
- Python 中 bool 类型属于数字数据类型，True 等价于 1，False 等价于 0
  布尔类型只有两个值：True 和 False

```python
num1 = 10
num2 = 20

flag = num1 > num2

# False
print(flag)

# <class 'bool'>
print(type(flag))
```

### 字符串

```python
msg = 'hello world'
print(msg)

name = "kunkun"
language = "python"
print(name)
print((language + "\n") * 3)

# <class 'str'>
print(type(name))
```

### 列表

```python
# 列表
hobby = ["唱", "跳", "rap"]

# 获取列表元素
print(hobby[0])
print(hobby[1])
print(hobby[2])

# <class 'list'>
print(type(hobby))
```

### 元组

元组的元素不能修改，元组是一种特殊的列表

```python
hobby = ("唱", "跳", "rap")

# 获取元组元素
print(hobby[0])
print(hobby[1])
print(hobby[2])

# <class 'tuple'>
print(type(hobby))
```

### 字典

字典是由多个键值对组成的，键与值之间用冒号 : 分割，多个键值对之间用逗号 , 分割，字典是无序的

```python
user = {"name": "kunkun", "age": 100, "hobby": ["唱", "跳", "rap"]}
print(user)

# <class 'dict'>
print(type(user))
print(user["name"])
print(user["age"])
print(user["hobby"])
```

### 集合

集合是由多个元素组成的，集合中的元素不能重复，集合中的元素可以是任何类型

```python
color = {"red", "yellow", "blue", "red", "yellow", "blue", "pink"}

# {'pink', 'red', 'blue', 'yellow'}
print(color)

# <class 'set'>
print(type(color))
```

## 判断变量类型

type() 是 Python 中的一个内置函数，用于返回变量的类型。
语法：

```python
type(var/val)

name = "kunkun"
age = 18


# <class 'str'>
print(type(name))

# <class 'int'>
print(type(age))

# <class 'int'>
print(type(1))
```

常见的变量类型有：int（整数）、float（浮点数）、bool（布尔值）、complex（复数）、str（字符串）、list（列表）、tuple（元组）、dict（字典）、set（集合）

判断变量的数据类型
使用 type() 函数判断变量的类型

```python
num = 10
num2 = "10"
msg = "hello python"

# True
print(type(num) == int)

# False
print(type(num2) == int)

# True
print(type(msg) == str)
```

使用 isinstance() 函数用于判断一个对象是否属于某种类型，或是否为指定类的实例
注意：

- object（必选）： 是一个对象
- type（必选）：它是一个类型名、类名或者由类型名或类名组成的元组，如果是元组，则会判断对象是否为元组中所包含的类型之一
语法：

```python
isinstance(object, type)

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
```

## 运算符

算术运算符

```python
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

# 除法，除法结果永远是float浮点数
# 2.0
print(10 / 5)

# 取余
# 1
print(10 % 3)

# 取整除
# 3
print(10 // 3)
```

赋值运算符

```python
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
```

比较运算符

```python
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
```

逻辑运算符

```python
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
```

成员运算符
在 Python 中，成员运算符用于判断某个元素是否在某个序列（字符串、列表、元组、字典）中，成员运算符有 in 和 not in 两个，返回结果为 True 或 False

```python
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
```

身份运算符
身份运算符用于判断两个变量的引用对象是否为同一个，返回结果为 True 或 False
注意：

- is 运算符用于判断两个对象是否引用自同一个内存地址，如果是，则返回 True，否则返回 False
- == 用于判断两个变量的值是否相等

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# False
print(list1 is list2)
# True
print(list1 == list2)
```

## 类型转换

Python 中，类型转换是 Python 的一个重要功能，它可以将一种数据类型转换为另一种数据类型，常用的内置类型转换函数有以以下几种：

- int()：将其他类型转换为整数
- float()：将其他类型转换为浮点数
- str()：将其他类型转换为字符串
- bool()：将其他类型转换为布尔值
- list()：将其他类型转换为列表
- tuple()：将其他类型转换为元组
- dict()：将其他类型转换为字典
- set()：将其他类型转换为集合

转换成整数类型

```python
# 转换成整数类型
num = int("123")  
# 123
print(num)

# 浮点数转换为整数，取整
num2 = int(3.14)
# 3
print(num2)
```

转换成浮点数类型

```python
num3 = float(123)
# 123.0
print(num3)

num4 = float("3.14")
# 3.14
print(num4)
```

转换成布尔类型
在 Python 中，使用 bool() 函数可以将其他类型转换为布尔值，值得注意的是：

- 所有空值都会返回 False，例如：False、None、0、''、空列表、空元祖、空字典、空集合等
- 所有非空值都会返回 True

```python
num5 = bool(0)
# False
print(num5)

num6 = bool(1)
# True
print(num6)

num7 = bool(None)
# False
print(num7)
```

转换成字符串类型

```python
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
```

转换成列表类型

```python
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

```

转换成元组类型

```python
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
```

转换成字典类型
在 Python 中，使用 dict() 函数可以将一个可迭代对象转换为字典类型。可迭代对象中的每个元素必须是一个包含两个元素的序列，第一个元素作为键，第二个元素作为值。

```python
info = [("name", "kunkun"), ("age", 18), ("hobby", ["唱", "跳", "rap", "篮球"])]

# {'name': 'kunkun', 'age': 18, 'hobby': ['唱', '跳', 'rap', '篮球']}
print(dict(info))
```

转换成集合类型

```python
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
```

## 注释

语法：

```python
# 这是单行注释

"""
这是多行注释
这是多行注释
"""
```

## 输出语法

print() 是 Python 中的一个内置函数，用于输出数据，print() 函数的参数可以是字符串、数字、布尔值、列表、元组、字典、集合等等，print() 函数的参数可以有多个，多个参数之间用逗号隔开。print() 函数的参数可以有格式化符，格式化符用于格式化输出的数据。

```python
print(值列表, sep='分割符', end='结束符', file=文件对象, flush=布尔值)

# sep（可选）：用于设置分割符，默认是 “空格”。
# end（可选）：用于设置结束符，默认是 “\n（换行）”
# file（可选）：表示输出到哪个文件，默认是标准输出。
# flush（可选）：表示是否强制刷新缓存区，默认是不刷新。
```

## 输入语法

input() 是 Python 中的一个内置函数，用于从用户输入数据，input() 函数的参数可以是字符串，字符串中的内容会作为提示信息输出给用户。input() 函数的返回值是一个字符串，字符串中的内容是用户输入的数据。

```python
text = input("请输入内容：")
print(text)
```

## 转义字符

```python
常用的转义字符有：
\'：单引号
\"：双引号
\n：换行
\t：制表符
\r：回车
\b：退格
\\：反斜杠

s = "不经历风雨\n怎么见'彩虹'"

# 不经历风雨
# 怎么见'彩虹'
print(s)
```

# 流程控制

在 Python 中，流程控制语句有：if 语句、while 语句、for 语句、break 语句、continue 语句、pass 语句。使用缩进的方式来控制代码块

if 语句

```python
# if 语句
score = input("请输入分数：")
score = int(score)
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")


# if 嵌套
num = int(input("请输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("这是一个能够3整除的偶数")
    else:
        print("不能被3整除的偶数")
else:
    print("奇数")
```

三元运算符
语法：

```python
# 条件表达式
x if a else b

score = int(input("请输入分数："))
print("及格" if score >= 60 else "不及格")

a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
result = a - b if a > b else b - a
print(result)
```

while循环

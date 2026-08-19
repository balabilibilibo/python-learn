import sys
import copy

sys.stdout.reconfigure(encoding="utf-8")


def testList():
    # languages = ["C", "Python", "C++", "Java", "Go", "Rust", "JavaScript"]

    # # 在下标为 0 的位置插入 C语言
    # languages.insert(0, "C")

    # # 在列表末尾添加新元素
    # languages.append("JavaScript")

    # # ['C', 'Python', 'C++', 'Java', 'Go', 'Rust', 'JavaScript']
    # print(languages)

    # # 列表的长度：7
    # print(len(languages))

    languages = ["C", "Python", "C++", "Java", "Go", "Rust", "JavaScript"]

    del languages[0]

    # ['Python', 'C++', 'Java', 'Go', 'Rust', 'JavaScript']
    print(languages)

    # JavaScript
    print(languages.pop())

    # ['Python', 'C++', 'Java', 'Go', 'Rust']
    print(languages)

    # Java
    print(languages.pop(2))

    # ['Python', 'C++', 'Go', 'Rust']
    print(languages)

    languages.remove("Rust")

    # ['Python', 'C++', 'Go']
    print(languages)

    # ['Python', 'C++', 'Go', 'Python']
    languages.append("Python")

    languages.remove("Python")

    # ['C++', 'Go', 'Python']
    print(languages)

    hobbys = [
        "唱",
        "跳",
        "rap",
    ]

    hobbys[2] = "篮球"

    # ["唱", "跳", "篮球"]
    print(hobbys)

    # 给一个不存在的位置赋值会报错，以下代码会报错
    # hobbys[3] = "篮球"

    users = ["admin", "kunkun", "wuxidixi"]

    del users[:]

    users.clear()

    users *= 0

    # 给列表中的每一个元素都分配一个空值，以达到清空列表的目的
    users[:] = []

    # []
    print(users)

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10]
    nums = nums1 + nums2

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums)

    # extend() 方法会修改原列表
    nums1.extend(nums2)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums1)

    # 使用解包合并列表, * 表示解包
    languages1 = ["C", "Python", "C++", "Java", "Go", "Rust", "JavaScript"]
    languages2 = ["C#", "Swift", "Kotlin"]
    languages3 = ["Dart", "Flutter"]
    languages = [*languages1, *languages2, *languages3]

    # ['C', 'Python', 'C++', 'Java', 'Go', 'Rust', 'JavaScript', 'C#', 'Swift', 'Kotlin', 'Dart', 'Flutter']
    print(languages)

    # 复制列表
    colors = ["red", "green", "blue"]

    # 使用切片复制(浅拷贝)
    result = colors[:]

    # 使用 list() 方法(浅拷贝)
    result = list(colors)

    # 使用乘法运算符(浅拷贝)
    result = colors * 1

    # 使用列表的 coppy() 方法(浅拷贝)
    result = colors.copy()

    # 使用 copy.copy() 方法(浅拷贝)
    result = copy.copy(colors)

    # 使用 copy.deepcopy() 方法(深拷贝)
    result = copy.deepcopy(colors)

    # ['red', 'green', 'blue']
    print(result)

    # 使用 copy.deepcopy() 方法(深拷贝)
    # result = copy.deepcopy(colors)

    # # ['red', 'green', 'blue']
    # print(result)

    nums = [1, 2, 3, [4, 5, 6]]
    result = copy.copy(nums)
    result[3].append(7)

    # [1, 2, 3, [4, 5, 6, 7]]
    print(nums)
    # [1, 2, 3, [4, 5, 6, 7]]
    print(result)

    nums = [1, 2, 3, [4, 5, 6]]
    result = copy.deepcopy(nums)
    result[3].append(7)

    # [1, 2, 3, [4, 5, 6]]
    print(nums)
    # [1, 2, 3, [4, 5, 6, 7]]
    print(result)

    # 遍历列表
    languages = ["C", "Python", "C++", "Java", "Go", "Rust", "JavaScript"]
    # for 循环遍历列表
    # for language in languages:
    #     print(language)

    # for i in range(len(languages)):
    #     print(languages[i])

    # while 循环遍历列表
    # i = 0
    # while i < len(languages):
    #     language = languages[i]
    #     print(language)
    #     i += 1

    # while languages:
    #     language = languages.pop()
    #     print(language)

    # enumerate() 方法遍历列表
    # enumerate() 是 Python 一个内置的函数,它接受一个列表作为参数,然后返回一个由元组组成的迭代器,每个元组包含 2 个元素,第一个元素是索引,第二个元素是列表中的元素

    for index, language in enumerate(languages):
        print(index, language)

    # 列表切片
    # list[start:end:step]
    languages = ["C", "Python", "C++", "Java", "Go", "Rust", "JavaScript"]

    # ['C', 'Python', 'C++']
    print(languages[0:3])

    # ['C', 'Python', 'C++', 'Java', 'Go', 'Rust', 'JavaScript']
    print(languages[0:])

    # ['C', 'Python', 'C++']
    print(languages[:3])

    ["C", "C++", "Go", "JavaScript"]
    print(languages[::2])

    # ['JavaScript', 'Rust', 'Go', 'Java', 'C++', 'Python', 'C']
    print(languages[::-1])

    # ['Go', 'Rust']
    print(languages[-3:-1])

    # 列表去重
    colors = ["red", "green", "blue", "pink", "red", "yellow", "blue"]

    # 使用循环 + 判断
    result = []
    for color in colors:
        if color not in result:
            result.append(color)

    # ['red', 'green', 'blue', 'pink', 'yellow']
    print(result)

    # 使用 set()
    result = list(set(colors))
    # ['yellow', 'blue', 'pink', 'red', 'green']
    print(result)

    # 使用 dict.fromkeys(),会保留列表元素原有的顺序
    result = list(dict.fromkeys(colors))
    # ['red', 'green', 'blue', 'pink', 'yellow']
    print(result)

    # 二维列表
    nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]


# 列表排序
# # 使用列表的sort() 方法
# nums = [3, 2, 1, 4, 5, 6, 7, 8, 9]

# # 默认升序
# nums.sort()
# # 等价于 nums.sort(reverse=False)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums)

# # 降序
# nums.sort(reverse=True)

# # [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(nums)


# users = [
#     {"name": "kunkun", "age": 18},
#     {"name": "wuxidixi", "age": 19},
#     {"name": "xiaoming", "age": 17},
# ]
# users.sort(key=lambda user: user["age"])

# # [{'name': 'xiaoming', 'age': 17}, {'name': 'kunkun', 'age': 18}, {'name': 'wuxidixi', 'age': 19}]
# print(users)


# 使用内置的 sorted() 方法
nums = [3, 2, 1, 4, 5, 6, 7, 8, 9]

# 默认升序
result = sorted(nums)
# 等价于 sorted(nums, reverse=False)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(result)


# 降序
result = sorted(nums, reverse=True)

# [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(result)


users = [
    {"name": "kunkun", "age": 18},
    {"name": "wuxidixi", "age": 19},
    {"name": "xiaoming", "age": 17},
]

result = sorted(users, key=lambda user: user["age"])

# [{'name': 'xiaoming', 'age': 17}, {'name': 'kunkun', 'age': 18}, {'name': 'wuxidixi', 'age': 19}]
print(result)


# 列表推导式
for i in range(1, 10):
    print(i, end="\t")


nums = [i * 2 for i in range(1, 6)]

# [2, 4, 6, 8, 10]
print(nums)


users = ["iaoming", "kunkun", "wuxidixi"]
result = [i.upper() for i in users]

# ['IAOMING', 'KUNKUN', 'WUXIDIXI']
print(result)


# 加上判断条件,需要将判断条件写 for 循环在后面
nums = [2, 4, 5, 6, 7, 1]
result = [i for i in nums if i % 2 == 0]

# [2, 4, 6]
print(result)

# 使用 if-else 语句,需要放在 for 循环前面
nums = [2, 4, 5, 6, 7, 1]
result = [i if i % 2 == 0 else i * 2 for i in nums]

# [2, 4, 10, 6, 14, 2]
print(result)

import sys

sys.stdout.reconfigure(encoding="utf-8")


# if 语句
def testIf():
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


def testTernaryOperator():
    # 三元运算符
    score = int(input("请输入分数："))
    print("及格" if score >= 60 else "不及格")

    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    result = a - b if a > b else b - a
    print(result)


def testWhile():
    # i = 1
    # total = 0
    # while i <= 100:
    #     total += i
    #     i += 1
    # print(total)

    # while 循环使用 else 子句

    # 在循环结构中执行了 break 语句或者发生了异常，则不会执行 else 子句
    i = 0
    while i < 10:
        if i == 5:
            print(i)
            # break
        i += 1
    else:
        print("循环结束")


# for 循环
# for i in range(start,end,step)
def testFor():
    # for i in range(1, 10):
    #     for j in range(1, i + 1):
    #         print("{} * {} = {}".format(i, j, i * j), end="\t")
    #     print()

    # # 设置步长为负数
    # # 下方的打印结果是：10 9 8 7 6 5 4 3 2 1
    # for i in range(10, 0, -1):
    #     print(f"i:{i}")

    # for 循环使用 else 子句
    # 在循环结构中执行了 break 语句或者发生了异常，则不会执行 else 子句
    # for i in range(10):
    #     if i == 5:
    #         print(i)
    #         break
    # else:
    #     print("循环结束")

    # 遍历字符串
    str = "hello world"
    for i in str:
        print(i)

    # 遍历列表
    hobby = ["唱", "跳", "rap"]
    for i in hobby:
        print(i)

    # 遍历元组
    languages = ("Python", "C++", "Java", "Go", "Rust")
    for item in languages:
        print(item)

    # 遍历字典
    user = {"name": "kunkun", "age": 18, "hobby": ["唱", "跳", "rap"]}
    for key, value in user.items():
        print(key, value)


# testFor()


# break 语句
def testBreak():
    while True:
        username = input("请输入用户名：")
        if username == "kunkun":
            print(f"大家好，我是 {username}，我是练习时长两年半的练习生")
            break
        else:
            print("用户名错误")

    # 输出结果是：0 1 2 3 4
    for i in range(10):
        if i == 5:
            break
        print(i)


# continue 语句
def testContinue():
    # 以下输出结果是：1 2 3 4 6 7 8 9 10
    i = 0
    while i < 10:
        i += 1
        if i == 5:
            continue
        else:
            print(i)

    # 以下输出结果是：0 1 2 3 4 6 7 8 9
    for i in range(10):
        if i == 5:
            continue
        print(i)


# pass 语句
for i in range(10):
    if i % 2 == 0:
        print(i)
    else:
        # pass 在这里是一个空代码快，如果将 pass 删除，程序会报错
        pass

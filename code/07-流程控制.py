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


def testWhile(){}
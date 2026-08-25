import sys

sys.stdout.reconfigure(encoding="utf-8")

tup = ("admin", "kunkun", "wuxidixi", "ikun", "kunkun")

# 元组的元素是不能进行修改的,以下语句会报错
# tup[0] = "ikun"

# 获取元素下标
item = tup.index("kunkun")

# 1
print(item)

# 获取元素个数
count = tup.count("kunkun")

# 2
print(count)

# 元组解包
userInfo = ("kunkun", 18, ["唱", "跳", "rap", "篮球"])

name, age, hobbys = userInfo

# kunkun 18 ['唱', '跳', 'rap', '篮球']
print(name, age, hobbys)


# 访问元组
# 元组通过下标的方式来访问元组中的元素

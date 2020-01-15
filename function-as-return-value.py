"""
利用闭包返回一个计数器函数，每次调用它返回递增整数
"""


def create_counter():
    count = 0

    def counter():
        nonlocal count  # 内层函数访问外层函数的变量需要加nonlocal，但是内层函数却能直接访问外层的list
        count += 1
        return count
    return counter


# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
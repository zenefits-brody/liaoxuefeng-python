"""
https://www.liaoxuefeng.com/wiki/1016959663602400/1017451447842528

请用匿名函数改造下面的代码
"""


def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)

import math
from functools import reduce

my_tuple = (1, 2, 3)
my_tuple_with_list = (1, 2, [3, 4])
my_list = [1, 2, 3]
list_with_tuple = [1, 2, (3, 4)]
list_with_tuple_with_list = [1, 2, (3, 4, [5, 6])]

# my_tuple as input of set function
tuple_set = set(my_tuple)

# tuple containing list can't be used to create a set
# tuple_with_list_set = set(my_tuple_with_list)

# list as input
list_set = set(my_list)

# list with tuple
list_with_tuple_set = set(list_with_tuple)

# list with tuple with list can't be used to create a set
# list_with_tuple_with_list_set = set(list_with_tuple_with_list)


def quadratic(a, b, c):
    difference = b ** 2 - 4 * a * c
    if difference < 0:
        return
    sqrt_result = math.sqrt(difference)
    divisor = 2 * a
    x1 = (-b + sqrt_result) / divisor
    x2 = (-b - sqrt_result) / divisor
    return x1, x2


def person(name, age, *, city, job):
    print(name, age, city, job)


def person_with_args(name, age, *args, city, job):
    print(name, age, args, city, job)


# person_with_args('Bob', 5, city='pinghu', job='SDE')

# trim a string
def trim(string):
    length = len(string)
    first_non_space = -1
    last_non_space = -1
    for i in range(length):
        if string[i] != ' ':
            first_non_space = i
            break
    for j in range(length - 1, -1, -1):
        if string[j] != ' ':
            last_non_space = j
            break

    if first_non_space == -1:
        return ''

    return string[first_non_space:last_non_space+1]


# if trim('hello  ') != 'hello':
#     print('测试失败!')
#     print('1')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(my_list):
    if not my_list:
        return None, None

    minimum = maximum = my_list[0]

    for i in my_list:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i

    return minimum, maximum


# 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')


# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 写一个generator，不断输出杨辉三角每一行的list
def triangles():
    yield [1]
    last = [1, 1]
    yield last
    while True:
        next = get_next_from_last(last)
        yield next
        last = next


def get_next_from_last(last):
    next = [1]
    for i in range(len(last) - 1):
        next.append(last[i] + last[i + 1])
    next.append(1)
    return next


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name.capitalize()


# 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(prod_list):
    def time_fn(last_result, item):
        return last_result * item

    return reduce(time_fn, prod_list)


# Test
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    char2num_map = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, '.': '.'}

    def char2num(char):
        return char2num_map[char]

    def get_divisor(num_list):
        dot_index = -1
        for i in range(len(num_list)):
            if num_list[i] == '.':
                dot_index = i

        if dot_index == -1:
            return 1
        return 10 ** (len(num_list) - 1 - dot_index)

    def reduce_fn(last_result, item):
        if item == '.':
            return last_result
        return last_result * 10 + item

    num_list = list(map(char2num, s))

    divisor = get_divisor(num_list)

    num_list = [x / divisor for x in num_list if x != '.']

    return reduce(reduce_fn, num_list)


# Test
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')






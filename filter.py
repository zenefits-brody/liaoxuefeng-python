# https://www.liaoxuefeng.com/wiki/1016959663602400/1017404530360000


# 利用filter()筛选出回数
def is_palindrome(n):
    n_string = str(n)

    # n_string == n_string[::-1]
    # 用切片可以直接测试回文！

    for i in range(0, len(n_string) // 2, 1):
        if n_string[i] != n_string[-1-i]:
            return False

    return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

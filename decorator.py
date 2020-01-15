"""
https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584

请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
"""


import time
import functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        time_difference = (end_time - start_time) * 1000
        print('%s executed in %s ms' % (fn.__name__, time_difference))
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')


"""
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
"""


def log(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('begin call')
        result = fn(*args, **kw)
        print('end call')
        return result
    return wrapper


"""
再思考一下能否写出一个@log的decorator，使它既支持

@log
def f():
    pass

又支持

@log('execute')
def f():
    pass
"""


def log(text_or_fn):
    if isinstance(text_or_fn, str):
        def decorator(fn):
            @functools.wrap(fn)
            def wrapper(*args, **kw):
                fn(*args, **kw)

            return wrapper
        return decorator
    else:
        fn = text_or_fn

        @functools.wrap(fn)
        def wrapper(*args, **kw):
            fn(*args, **kw)

        return wrapper

"""
https://www.liaoxuefeng.com/wiki/1016959663602400/1017496679217440
"""


class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('{}, score: {}'.format(self.__name, self.__score))


bart = Student('Bart Police', 98)
nicole = Student('Nicole Lan', 88)
# print(bart.__name)  # AttributeError: 'Student' object has no attribute '__name'
bart.print_score()
bart.__name = 'new name'  # This doesn't error, but it's not actually changing the name of the student
bart.print_score()

"""
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
"""


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


"""
Below is a question I got about creating new attributes

xiao_ming.age = 18

foo.a = 'a'

They are both assigning a value to a non-existed attribute, why one succeeds but not the other?
"""


class Person:
    def __init__(self, name):
        self.name = name


xiao_ming = Person('Xiao Ming')
# print(xiao_ming.age)  # AttributeError: 'Person' object has no attribute 'age'
print(hasattr(xiao_ming, 'age'))  # False
xiao_ming.age = 18  # This doesn't error
print(xiao_ming.age)  # 18
print(hasattr(xiao_ming, 'age'))  # True

foo = {}
# print(foo.a)  # AttributeError: 'dict' object has no attribute 'a'
# foo.a = 'a'  # AttributeError: 'dict' object has no attribute 'a'
print(hasattr(foo, 'a'))  # False

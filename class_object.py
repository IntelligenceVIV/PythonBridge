# @Time    : 2019/4/19 23:36
# @Author  : Noah
# @File    : class_object.py
# @Software: PyCharm
# @description: class (inherit polymorphism encapsulation)=> object
class A(object):
    __slots__ = ['value', 'name', 'address', 'text']

    def __init__(self, value):
        self.value = value

    # (object class static) method
    # method => property
    @property
    def get(self):
        return self.value

    @classmethod
    def open(cls, number):
        return "Hello Index {number}".format_map({'number': str(number)})

    @staticmethod
    def about():
        return "Static Method"

    # __str__()返回用户看到的字符串
    def __str__(self):
        return self.value

    # __repr__()返回程序开发者看到的字符串
    def __repr__(self):
        return self.value

    # __call__()直接在实例本身上调用
    def __call__(self):
        return "The Number is: ".format(self.value)


class B(object):
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value ** 2


# 多重继承 => 子类可以扩展父类的功能
class C(A, B):
    pass


#############################################################################
# class => object
a = A(100)
b = B(101)
c = C(102)

# Call object method
print(c.get)

print(c.open(1))

print(c.about())

# 可以直接对实例进行调用
print(a())

#############################################################################
# 确定对象是否是类的实例
isinstance(a, A)

# 确定B是A的子类
issubclass(B, A)

# 是否是函数或方法
callable(b.get)

# 知道类的基类
print(B.__bases__)

# 知道对象属于哪个类
print(c.__class__)

# 知道对象中存储的所有值
print(c.__dict__)

#############################################################################
# 和属性有关系

# 测试对象有指定的属性
hasattr(a, 'value')

# 返回对象指定的属性值
getattr(a, 'value', '访问的属性不存在')

# 设置对象的属性值
setattr(a, 'msg', 'Hello World')

# 删除对象属性
delattr(a, 'msg')


# 限制类能添加的属性 __slots__ 核心作用是可以在创建大量实例的时候更加节省内存

#############################################################################
# Example of Fibonacci sequence

class Fibonacci(object):
    # def __init__(self):
    #     self.a = 1
    #     self.b = 1

    # def __iter__(self):
    #     return self
    #
    # def next(self):
    #     self.a, self.b = self.b, self.a + self.b
    #     if self.a > 10000:
    #         raise StopIteration()
    #     return self.a

    # def __getitem__(self, item):
    #     for i in range(item):
    #         self.a, self.b = self.b, self.a + self.b
    #     return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for i in range(item):
                a, b = b, a + b
            return a

        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            a, b = 1, 1
            slice_lst = []
            for i in range(stop):
                if i >= start:
                    slice_lst.append(a)
                a, b = b, a + b
            return slice_lst


obj = Fibonacci()

# for _ in range(10):
#     print(obj.next())

# print(obj[3])  # __getitem__

# print(obj[0:10])

#############################################################################

# __iter__ 该方法返回一个迭代对象

# __getitem__ 按照下标取出元素(有序)

#############################################################################

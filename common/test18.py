# -*- coding: utf-8 -*-
# author = "Louis"
class H:
    def info(sel):
        print(1)

    def name(self):
        pass


def f(k):
    if k <= 10 and k > 0:
        if k > 5:
            if k > 8:
                x = 0
            else:
                x = 1
        else:
            if k > 2:
                x = 3
            else:
                x = 4
    print(x)
if __name__ == '__main__':
    # a = H()
    # print(dir(H))
    # a.info()
    # print(dir(a))
    f(3)
    f(4)
    f(5)


    def chanageInt(number2):
        number2 = number2 + 1


        print("changeInt: number2 = ", number2)

    number1 = 2
    chanageInt(number1)
    print("number:", number1)


    def chanageList(list):
        list.append("end")
        print("list", list)


    strs = ['1', '2']
    chanageList(strs)
    print('strs', strs)


    # class hello():
    #     def showInfo(sef):
    #         print(self.x)

    class Hello():
        def __init__(self, name):
            self.name = name

        def showInfo(self):
            print(self.name)


    class A:
        def a(self):
            print("a")

    class B:
        def b(self):
            print("b")

    class C:
        def c(self):
            print("c")

    class D(A, C):
        def d(self):
            print("d")
    # d = D()
    # d.a()
    # d.b()
    # d.d()

    # print="heo"
    # print(print)

    # l = ['1', '2', '3']
    # s = ','.join(l)
    # print(s)

    # s = 'abcdef'
    # print(s[::-1])
    # print(s)

    # 装饰器的作用是什么？
    # 装饰器的作用是在不改变函数原功能的基础上为函数添加新的功能。
    # 装饰器的原则是什么？
    # 1. 不修改被装饰对象的源代码。
    # 2. 不修改被装饰对象的调用方式。
    # 装饰器的基本语法：
    def wrapper(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner

    # 可迭代对象、迭代器对象的区别
    # 迭代对象不一定是迭代器对象，迭代器对象一定是可迭代的。

    # hasattr、setattr、getattrs的使用方法。
    # hasattr判断一个实例对象中是否包含有某个属性或者方法。hasattr(obj, 'name')
    print(hasattr(D, 'c'))
    h = Hello('a')
    print(hasattr(h, 'name'))
    # setattr给一个实例对象增加一个key-value形式的键值。
    print(setattr(h,'age', 1))
    print(getattr(h, 'age'))
    # getattr获取实例对象中的属性或者方法
    getattr(h, 'showInfo')()


    # return、yield的使用区别？
    # 在一个函数里return只能执行一次，只要遇到return就会停止执行该函数。
    # 一个函数里yield可以执行多次，每次遇到都会记录函数执行环境并保存该环境，等待下一次被调用。通过next()函数来进行访问

    # lambda函数： 匿名函数, 其中包含的表达式不超过一个
    # 使用过哪些模块： threading os sys re numpy pickle requests random collections time datetime

    # 什么是GIL？
    # 全局解释器锁：一个进程中，同一时刻只能有一个线程来执行代码，该线程将持有python的解释器控制权。
    # 互斥锁？
    # 当多个线程要更改共享数据时，先将其锁定，此时资源的状态为"锁定"状态，其他线程不能更改该资源；
    # 直到该线程释放资源，将资源的状态变成"非锁定"状态，其他的线程才能再次锁定该资源。
    # 互斥锁保证了每次只有一个线程进行写入操作，从而保证在多线程操作的情况下数据的正确性。

    # python里面测试框架有哪些？
    # unittest \ nose \ doctest \ pytest

    # python中用于底层网络交互的库有哪些？
    # requests, socket, urllib3, grab, pycurl

    # python常见的命令行 交互自动化 模块有哪些？
    # import module

    # python网络交互时，二进制打包解包的模块有哪些？
    # pack() upk()

    # 列出五个标准库  五个第三方库
    # os sys re math io time datetime collections threading
    # requests numpy(开源数值计算) djangorestframework pandas(大数据处理) xrld(表格操作)

    # python内建的数据类型: int str list set dict float bool tuple

    a = [1,2,3,4]
    b = [4,3,1]
    c = a + b
    c.sort()
    print(c)

    import re
    p = re.compile(r'^isoftstone(.*)@.com$')
    def get_re_data(p, s):
        m = re.match(p, s)
        if m is not None:
            return m.groups()[0]
        return None
    print(get_re_data(p, "aa"))
    print(get_re_data(p, "isoftstone@xx.com"))

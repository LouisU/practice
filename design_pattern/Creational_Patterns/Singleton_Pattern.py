# -*- coding: utf-8 -*-
# author = "Louis"
import threading
import time

# 用__new__实现的单实例，但是对于多线程来说是不安全的。
# class Singleton:
#     def __init__(self):
#         # time.sleep(10)
#         print("#2")
#
#     def __new__(cls, *args, **kwargs):
#         print("#1")
#         if not hasattr(Singleton, "_instance"):
#             Singleton._instance = super().__new__(cls)
#
#         return Singleton._instance
class Config:

    def __init__(self, env, position):
        self.env = env
        self.position = position

    def __new__(cls, *args, **kwargs):
        print("#1")
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

# 单实例，对多线程也安全。用了锁机制。
# class Singleton:
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         # print("#2")
#         pass
#     def __new__(cls, *args, **kwargs):
#         # print("#1")
#         if not hasattr(Singleton, "_instance"):
#             # time.sleep(2)
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = super().__new__(cls)
#         return Singleton._instance


def task(arg):
    obj = Singleton()
    print(obj)


if __name__ == '__main__':
    obj1 = Config('dev', 'China')
    print(obj1.env, obj1.position)
    obj2 = Config('production', 'India')
    print(obj1.env, obj1.position)
    print(obj2.env, obj2.position)
    # print(obj1, obj2)
    #
    print(obj1 is obj2)

    # for i in range(10):
    #     t = threading.Thread(target=task, args=[i,])
    #     t.start()
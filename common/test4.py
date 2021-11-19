# -*- coding: utf-8 -*-
# author = "Louis"

import threading
# 单实例，对多线程也安全。用了锁机制。
class Singleton:
    _instance_lock = threading.Lock()

    def __init__(self):
        # print("#2")
        pass
    def __new__(cls, *args, **kwargs):
        # print("#1")
        if not hasattr(Singleton, "_instance"):
            # time.sleep(2)
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = super().__new__(cls)
        return Singleton._instance

if __name__ == '__main__':
    st1 = Singleton()
    st2 = Singleton()
    print(st1)
    print(st2)

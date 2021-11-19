# -*- coding: utf-8 -*-
# author = "Louis"
import time
from random import randint


def count_iterator(n):
    i = 0
    while i < n:
        yield i
        i += 1
    return n


def check_n(n):
    if isinstance(n, int):
        if n > 0:
            return True
        else:
            raise ValueError("n should great than 0")
    else:
        raise ValueError("n should be a int")


class ArrayGenerator:

    @staticmethod
    def orderedList(n):
        check_n(n)
        ret_list = []
        for i in count_iterator(n):
            ret_list.append(i)
        return ret_list

    @staticmethod
    def randomList(n):
        check_n(n)
        ret_list = []
        for i in count_iterator(n):
            ret_list.append(randint(0, n))
        return ret_list


class SortingTest:
    @staticmethod
    def isOrdered(alist):
        list_len = len(alist)
        if list_len < 2:
            return True
        i = 1
        while i < list_len:
            if alist[i - 1] <= alist[i]:
                i += 1
            else:
                return False
        return True


def count(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("class:{} function: {} spend: {} s".format(func.__class__, func.__name__, (end - start)))
        return result

    return wrapper


if __name__ == '__main__':
    print(ArrayGenerator.randomList(10))
    print(ArrayGenerator.orderedList(10))
    print(ArrayGenerator.randomList('1'))

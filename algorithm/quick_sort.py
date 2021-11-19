# -*- coding: utf-8 -*-
# author = "Louis"
from common import tools
import random


# 每次选最左端的元素作为v
class quickSort:

    @classmethod
    @tools.count
    def sort(cls, arr):
        cls.sortR(arr, 0, len(arr)-1)

    @classmethod
    def sortR(cls, arr, l, r, depth=1):
        if l >= r:
            # print("*"*depth+"arr[{}:{}] = {} return".format(l, r, arr[l:r]))
            return
        p = cls.partition(arr, l, r, depth)
        # print("*"*depth + "{}".format(arr))
        cls.sortR(arr, l, p - 1, depth + 1)
        cls.sortR(arr, p + 1, r, depth + 1)

    @classmethod
    def partition(cls, arr, l, r, depth):
        # 左闭 右开
        # print("*" * depth + "arr[{}:{}]={}".format(l, r, arr[l:r]))
        j = l
        # 循环不变量 保持arr[l+1:j]< v , 保持arr[j+1: i] >= v
        for i in range(j + 1, r+1):
            if arr[i] < arr[l]:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
            # print('*' * depth + "{} {} ing j={} i={}".format(
            #     arr[l:j + 1], arr[j + 1:i + 1], j, i))

        arr[j], arr[l] = arr[l], arr[j]
        # print('*' * depth + "{} over".format(arr))
        return j


# 随机选择v
class quickSort2:

    @classmethod
    @tools.count
    def sort(cls, arr):
        cls.sortR(arr, 0, len(arr)-1)

    @classmethod
    def sortR(cls, arr, l, r, depth=1):
        if l >= r:
            # print("*"*depth+"arr[{}:{}] = {} return".format(l, r, arr[l:r]))
            return
        p = cls.partition(arr, l, r, depth)
        # print("*"*depth + "{}".format(arr))
        cls.sortR(arr, l, p-1, depth + 1)
        cls.sortR(arr, p + 1, r, depth + 1)

    @classmethod
    def partition(cls, arr, l, r, depth):
        # 左闭 右开
        # print("*" * depth + "arr[{}:{}]={}".format(l, r, arr[l:r]))
        random_index = random.randint(l, r)
        arr[l], arr[random_index] = arr[random_index], arr[l]
        j = l
        # 循环不变量 保持arr[l+1:j]< v , 保持arr[j+1: i] >= v
        for i in range(j + 1, r+1):
            if arr[i] < arr[l]:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
            # print('*' * depth + "{} {} ing j={} i={}".format(
            #     arr[l:j + 1], arr[j + 1:i + 1], j, i))

        arr[j], arr[l] = arr[l], arr[j]
        # print('*' * depth + "{} over".format(arr))
        return j


# 每次选中间的元素作为排序数
class quickSort3:

    @classmethod
    @tools.count
    def sort(cls, arr):
        cls.sortR(arr, 0, len(arr))

    @classmethod
    def sortR(cls, arr, l, r, depth=1):
        if l >= r:
            # print("*"*depth+"arr[{}:{}] = {} return".format(l, r, arr[l:r]))
            return
        p = cls.partition(arr, l, r, depth)
        # print("sort*"*depth + "{}".format(arr))
        cls.sortR(arr, l, p, depth + 1)
        cls.sortR(arr, p + 1, r, depth + 1)

    @classmethod
    def partition(cls, arr, l, r, depth):
        # 左闭 右开
        # print("*" * depth + "arr[{}:{}]={}".format(l, r, arr[l:r]))
        mid_index = int((r - 1 + l) / 2)
        arr[l], arr[mid_index] = arr[mid_index], arr[l]
        j = l
        # 循环不变量 保持arr[l+1:j]< v , 保持arr[j+1: i] >= v
        for i in range(j + 1, r):
            if arr[i] < arr[l]:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
            # print('*' * depth + "{} {} ing j={} i={}".format(
            #     arr[l:j + 1], arr[j + 1:i + 1], j, i))

        arr[j], arr[l] = arr[l], arr[j]
        # print('*' * depth + "{} over".format(arr))
        return j


# 双路快速排序
class quickSort4:

    @classmethod
    @tools.count
    def sort2way(cls, arr):
        cls.sortR(arr, 0, len(arr)-1)

    @classmethod
    def sortR(cls, arr, l, r, depth=1):
        if l >= r:
            # print("*"*depth+"arr[{}:{}] = {} return".format(l, r, arr[l:r]))
            return
        p = cls.partition(arr, l, r, depth)
        # print("*"*depth + "{}".format(arr))
        cls.sortR(arr, l, p - 1, depth + 1)
        cls.sortR(arr, p + 1, r, depth + 1)

    @classmethod
    def partition(cls, arr, l, r, depth):
        # 左闭 右开
        # print("*" * depth + "arr[{}:{}]={}".format(l, r, arr[l:r]))
        random_index = random.randint(l, r)
        arr[l], arr[random_index] = arr[random_index], arr[l]
        # 循环不变量
        #    保持arr[l+1:i] <= v(就是l+1到i-1索引包括i-1 的元素都小于v),
        #    保持arr[j+1: r] >= v
        # 当i>j时， 具体操作就是维持循环不变量
        i = l + 1
        j = r
        while True:
            while i <= j and arr[i] < arr[l]:
                i += 1
            while j >= i and arr[j] > arr[l]:
                j -= 1
            if i >= j:
                break
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j -= 1
        arr[j], arr[l] = arr[l], arr[j]
        return j

# 三路快速排序
class quickSort5:

    @classmethod
    @tools.count
    def sort3way(cls, arr):
        cls.sortR(arr, 0, len(arr))

    @classmethod
    def sortR(cls, arr, l, r, depth=1):
        if l >= r:
            # print("*"*depth+"arr[{}:{}] = {} return".format(l, r, arr[l:r]))
            return
        lt, gt = cls.partition(arr, l, r, depth)
        # print("*"*depth + "{}".format(arr))
        cls.sortR(arr, l, lt, depth + 1)
        cls.sortR(arr, gt, r, depth + 1)

    @classmethod
    def partition(cls, arr, l, r, depth):
        # 左闭 右开
        # print("*" * depth + "arr[{}:{}]={}".format(l, r, arr[l:r]))
        random_index = random.randint(l, r - 1)
        arr[l], arr[random_index] = arr[random_index], arr[l]
        # 循环不变量
        #    保持arr[l+1:lt+1] < v(就是l+1到i索引包括i 的元素都小于v),
        #    保持arr[lt+1: i+1] = v
        #    保持arr[gt:r] > v
        # 当i<gt时， 具体操作就是维持循环不变量
        lt = l
        i =  l + 1
        gt = r
        while i < gt :
            if arr[i] < arr[l]:
                lt += 1
                arr[lt], arr[i] = arr[i], arr[lt]
                i += 1
            elif arr[i] > arr[l]:
                gt -= 1
                arr[gt], arr[i] = arr[i], arr[gt]
            else:
                i += 1
        arr[lt], arr[l] = arr[l], arr[lt]
        return lt,gt

class specialArray:

    @classmethod
    def generateSpecialArray(cls, n):
        arr = [None for i in range(n)]
        cls.generateSpecialArrayR(arr, 0, 0, n)
        return arr

    @classmethod
    def generateSpecialArrayR(cls, arr, value, l, r, depth=1):
        if l >= r:
            return
        mid = int((r - 1 + l) / 2)
        arr[mid] = value
        arr[mid], arr[l] = arr[l], arr[mid]
        # print("*"*depth + "arr:{}".format(arr))
        cls.generateSpecialArrayR(arr, value + 1, l + 1, r, depth + 1)
        arr[mid], arr[l] = arr[l], arr[mid]
        # print("*"*depth + "arr:{}".format(arr))


if __name__ == '__main__':
    from common import tools
    import insertion_sort
    from merge_sort import MergeSort3
    import copy
    import sys

    sys.setrecursionlimit(1000000)
    s_a = specialArray.generateSpecialArray(10000)
    # n = [10000, 100000]
    def test(arr):
        arr2 = copy.deepcopy(arr)
        # arr3 = copy.deepcopy(arr)
        arr4 = copy.deepcopy(arr)
        # arr5 = copy.deepcopy(arr)

        quickSort.sort(arr)
        quickSort2.sort(arr2)
        # quickSort3.sort(arr3)
        quickSort4.sort2way(arr4)
        # quickSort5.sort3way(arr5)

        print("arr: {}".format(tools.SortingTest.isOrdered(arr)))
        print("arr2: {}".format(tools.SortingTest.isOrdered(arr2)))
        # print("arr3: {}".format(tools.SortingTest.isOrdered(arr3)))
        print("arr4: {}".format(tools.SortingTest.isOrdered(arr4)))
        # print("arr5: {}".format(tools.SortingTest.isOrdered(arr5)))
        print("1")

    # for i in [ 1, 10, 100]:
    #     test(tools.ArrayGenerator.randomList(i))

    # For randomlist
    print("-"*10+"For random list.\n")
    n = 10000
    arr = tools.ArrayGenerator.randomList(n)
    test(arr)

    # For orderList
    print("-"*10+"For ordered list.\n")
    n = 10000
    arr = tools.ArrayGenerator.orderedList(n)
    test(arr)

    # For all the same value list
    print("-"*10+"For all the same value list.\n")
    n = 10000
    arr = [0 for _ in range(n)]
    test(arr)


    # For the worst example list
    print("-"*10+"For worst example list.\n")
    n = 10000
    arr =specialArray.generateSpecialArray(n)
    test(arr)

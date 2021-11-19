# coding=utf-8
# Author="Louis"
from common import tools
import insertion_sort
from copy import deepcopy


# 该merge_sort3 和merge_sort对应。
#  merge_sort描述的是[left,right]的操作和代码
#  merge_sort3本文件描述[left,right)的操作和代码
class MergeSort:

    def merge(self, arr, left, mid, right):
        temp = arr[left:right]
        i, j = 0, mid - left
        for k in range(len(temp)):
            if i >= mid - left:
                arr[k + left] = temp[j]
                j += 1
            elif j >= right - left:
                arr[k + left] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k + left] = temp[i]
                i += 1
            else:
                arr[k + left] = temp[j]
                j += 1

    def sortR(self, arr, left, right, depth=1):
        if left >= right - 1:
            return
        # 将arr[left:right+1]一份为二
        mid = int((right + left) / 2)
        # print("*"*depth+"all:{}".format(arr[left:right+1]))
        self.sortR(arr, left, mid, depth + 1)
        # print('*'*depth + "merge left:{}".format(arr[left:mid+1]))
        self.sortR(arr, mid, right, depth + 1)
        # print('*'*depth + "merge right:{}".format(arr[mid+1:right+1]))
        self.merge(arr, left, mid, right)
        # print('*'*depth+'allsorted:{}'.format(arr[left:right+1]))

    @tools.count
    def sort(self, arr):
        self.sortR(arr, 0, len(arr))


# 优化merge的执行情况
class MergeSort2:

    def merge(self, arr, left, mid, right):
        temp = arr[left:right + 1]
        i, j = 0, mid - left + 1
        for k in range(len(temp)):
            if i > mid - left:
                arr[k + left] = temp[j]
                j += 1
            elif j > right - left:
                arr[k + left] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k + left] = temp[i]
                i += 1
            else:
                arr[k + left] = temp[j]
                j += 1

    def sortR(self, arr, left, right, depth=1):
        if left >= right:
            return
        # 将arr[left:right+1]一份为二
        mid = int((right + left) / 2)
        # print("*"*depth+"all:{}".format(arr[left:right+1]))
        self.sortR(arr, left, mid, depth + 1)
        # print('*'*depth + "merge left:{}".format(arr[left:mid+1]))
        self.sortR(arr, mid + 1, right, depth + 1)
        # print('*'*depth + "merge right:{}".format(arr[mid+1:right+1]))
        if arr[mid] > arr[mid + 1]:
            self.merge(arr, left, mid, right)
        # print('*'*depth+'allsorted:{}'.format(arr[left:right+1]))

    @tools.count
    def sort(self, arr):
        l = 0
        r = len(arr) - 1
        self.sortR(arr, l, r)


# 优化sort方法，使用插入排序算法优化
class MergeSort3:

    def merge(self, arr, left, mid, right):
        temp = arr[left:right + 1]
        i, j = 0, mid - left + 1
        for k in range(len(temp)):
            if i > mid - left:
                arr[k + left] = temp[j]
                j += 1
            elif j > right - left:
                arr[k + left] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k + left] = temp[i]
                i += 1
            else:
                arr[k + left] = temp[j]
                j += 1

    def sortR(self, arr, left, right, depth=1):
        # if left >= right:
        #     return
        if right - left <= 15:
            return insertion_sort.main_4_merger_sort(arr, left, right)
        # 将arr[left:right+1]一份为二
        mid = int((right + left) / 2)
        # print("*"*depth+"all:{}".format(arr[left:right+1]))
        self.sortR(arr, left, mid, depth + 1)
        # print('*'*depth + "merge left:{}".format(arr[left:mid+1]))
        self.sortR(arr, mid + 1, right, depth + 1)
        # print('*'*depth + "merge right:{}".format(arr[mid+1:right+1]))
        if arr[mid] > arr[mid + 1]:
            self.merge(arr, left, mid, right)
        # print('*'*depth+'allsorted:{}'.format(arr[left:right+1]))

    @tools.count
    def sort(self, arr):
        l = 0
        r = len(arr) - 1
        self.sortR(arr, l, r)


# 优化merge中的temp这个临时空间
class MergeSort4:

    def merge(self, arr, left, mid, right, temp):
        temp[left:right + 1] = arr[left:right + 1]
        i, j = left, mid + 1
        for k in range(left, right + 1):
            if i > mid:
                arr[k] = temp[j]
                j += 1
            elif j > right:
                arr[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1

    def sortR(self, arr, left, right, temp, depth=1):
        if left >= right:
            return
        # 将arr[left:right+1]一份为二
        mid = int((right + left) / 2)
        # print("*"*depth+"all:{}".format(arr[left:right+1]))
        self.sortR(arr, left, mid, temp, depth + 1)
        # print('*'*depth + "merge left:{}".format(arr[left:mid+1]))
        self.sortR(arr, mid + 1, right, temp, depth + 1)
        # print('*'*depth + "merge right:{}".format(arr[mid+1:right+1]))
        self.merge(arr, left, mid, right, temp)
        # print('*'*depth+'allsorted:{}'.format(arr[left:right+1]))

    @tools.count
    def sort(self, arr):
        l = 0
        r = len(arr) - 1
        temp = deepcopy(arr)
        self.sortR(arr, l, r, temp)


# 自底向上的归并算法
class MergeSort5:

    def merge(self, arr, left, mid, right):
        temp = arr[left:right + 1]
        i, j = 0, mid - left + 1
        for k in range(len(temp)):
            if i > mid - left:
                arr[k + left] = temp[j]
                j += 1
            elif j > right - left:
                arr[k + left] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k + left] = temp[i]
                i += 1
            else:
                arr[k + left] = temp[j]
                j += 1

    @tools.count
    def sort1(self, arr):
        n = len(arr)
        size = 1

        while size < n:
            for i in range(0, n, 2 * size):
                l = i
                mid = size + i - 1 if size + i - 1 <= n - 1 else n - 1
                r = i + 2 * size - 1 if i + 2 * size - 1 <= n - 1 else n - 1
                if mid + 1 <= n - 1 and arr[mid] > arr[mid + 1]:
                    self.merge(arr, l, mid, r)
                # print(arr[i:i + 2 * size])
            size += size

    @tools.count
    def sort2(self, arr):
        n = len(arr)

        for i in range(0, n, 16):
            l = i
            r = i + 16 if i + 16 <= n - 1 else n - 1
            insertion_sort.main_4_merger_sort(arr, l, r)

        size = 16
        while size < n:
            for i in range(0, n, 2 * size):
                l = i
                mid = size + i - 1 if size + i - 1 <= n - 1 else n - 1
                r = i + 2 * size - 1 if i + 2 * size - 1 <= n - 1 else n - 1
                if mid + 1 <= n - 1 and arr[mid] > arr[mid + 1]:
                    self.merge(arr, l, mid, r)
                # print(arr[i:i + 2 * size])
            size += size


if __name__ == "__main__":
    from common.tools import ArrayGenerator
    from copy import deepcopy
    from common import tools

    arr = ArrayGenerator.randomList(10)
    arr2 = deepcopy(arr)
    arr3 = deepcopy(arr)
    arr4 = deepcopy(arr)
    arr5 = deepcopy(arr)
    arr6 = deepcopy(arr)
    # unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
    # arr = [1, 4, 7, 9, 2, 5, 6, 8]
    MergeSort().sort(arr)
    MergeSort2().sort(arr2)
    MergeSort3().sort(arr3)
    MergeSort4().sort(arr4)
    MergeSort5().sort1(arr5)
    MergeSort5().sort2(arr6)
    print(tools.SortingTest.isOrdered(arr))
    print(tools.SortingTest.isOrdered(arr2))
    print(tools.SortingTest.isOrdered(arr3))
    print(tools.SortingTest.isOrdered(arr4))
    print(tools.SortingTest.isOrdered(arr5))
    print(tools.SortingTest.isOrdered(arr6))
    print("#")
    # print(merge_sort.mergeSort(unsortedArray))

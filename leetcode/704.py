# -*- coding: utf-8 -*-
# author = "Louis"
# 给定一个n个元素有序的（升序）整型数组nums 和一个目标值target
# 写一个函数搜索nums中的 target，
# 如果目标值存在返回下标，否则返回 -1。

class Solution:
    def search(self, arr, target):
        return self.searchR(arr, 0, len(arr), target)

    def searchR(self, arr, l, r, target):
        if l >= r:
            return -1
        mid = int(l + (r - l) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.searchR(arr, l, mid, target)
        else:
            return self.searchR(arr, mid + 1, r, target)


if __name__ == '__main__':
    pass

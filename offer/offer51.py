# -*- coding: utf-8 -*-
# author = "Louis"
# 剑指
# Offer
# 51.
# 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。
#
#
#
# 示例
# 1:
# 输入: [7, 5, 6, 4]
# 输出: 5
#
# 限制：
# 0 <= 数组长度 <= 50000
#
from common import tools


class Solution:
    count = 0

    def reversePairs(self, nums):
        return self.sort(nums)

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
                self.count += mid - left - i + 1
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
        return self.count
if __name__ == '__main__':
    alist = [7,5,6,4]
    print(Solution().sort(alist))
    print('#')

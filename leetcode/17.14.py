# -*- coding: utf-8 -*-
# author = "Louis"
# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
#
# 示例：
#
# 输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
# 提示：
#
# 0 <= len(arr) <= 100000
# 0 <= k <= min(100000, len(arr))


import random


class Solution:
    def smallestK(self, arr, k):
        if k == 0:
            return []
        k_index = self.sort(arr, 0, len(arr), k - 1)
        return arr[0: k_index + 1]

    def sort(self, arr, l, r, k):
        if l >= r:
            return k
        p = self.partition(arr, l, r)
        if k < p:
            return self.sort(arr, l, p, k)
        elif k > p:
            return self.sort(arr, p + 1, r, k)
        else:
            return p

    def partition(self, arr, l, r, ):
        random_index = random.randint(l, r - 1)
        arr[l], arr[random_index] = arr[random_index], arr[l]

        i = l + 1
        j = r - 1
        while True:
            while i <= j and arr[i] <= arr[l]:
                i += 1
            while i <= j and arr[j] >= arr[l]:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        arr[l], arr[j] = arr[j], arr[l]
        return j

    # 非递归的方式实现select K
    def sort2(self, arr, k):
        l = 0
        r = len(arr)
        # 循环不变量: 在arr[l:r)中定位索引为第k-1个位置的值
        while l < r:
            p = self.partition(arr, l, r)
            if k < p:
                r = p
            elif k > p:
                l = p + 1
            else:
                return p
        return -1

if __name__ == '__main__':
    pass

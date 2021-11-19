# -*- coding: utf-8 -*-
# author = "Louis"
# 输入整数数组 arr ，找出其中最小的 k 个数。
# 例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#
# 示例 1：
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#
# 示例 2：
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
#
# 限制：
# 0 <= k <= arr.length <= 10000
# 0 <= arr[i]<= 10000
import random


class Solution:
    def getLeastNumbers(self, arr, k):
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


if __name__ == '__main__':
    arr = [3, 2, 1]
    k = 2
    print(Solution().getLeastNumbers(arr, k))
    arr = [0,1,2,1]
    k = 4
    print(Solution().getLeastNumbers(arr, k))
    arr = [1,3,5,7,2,4,6,8]
    k = 6
    print(Solution().getLeastNumbers(arr, k))
    arr = [1,2,3]
    k = 0
    print(Solution().getLeastNumbers(arr, k))
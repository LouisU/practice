# -*- coding: utf-8 -*-
# author = "Louis"
# 在未排序的数组中找到第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
# 示例2:
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
import random


class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        return nums[self.sort(nums, 0, len(nums), k)]

    def sort(self, nums, l, r, k):
        if l >= r:
            return k
        p = self.partition(nums, l, r)
        if k < p:
            return self.sort(nums, l, p, k)
        elif k > p:
            return self.sort(nums, p + 1, r, k)
        else:
            return p

    # 采用二路快排，
    #     三路快排不合适(arr[i]和arr[l]值相等的index很可能不会返回
    #     一般快排 二分快排 随机快排都可能遇到特殊测试数据使得算法退化成O(n^2)
    def partition(self, arr, l, r):
        random_index = random.randint(l, r - 1)
        arr[l], arr[random_index] = arr[random_index], arr[l]
        # 二路快排 循环不变量 arr[l+1:i+1]<=V arr[j:r]>=V
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
    nums = [-1, -1]
    k = 2
    res = Solution().findKthLargest(nums, k)
    print(res)
    print("#")
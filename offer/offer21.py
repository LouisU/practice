# -*- coding: utf-8 -*-
# author = "Louis"

# class Solution:
#     def exchange(self, nums):
#         j = -1
#         i = 0
#         # 循环不变量 [0,j]左闭右闭 都是奇数。[j+1, i-1]左闭右闭 都是偶数。当i<len(nums)时循环进行。
#         # 初始时j=-1, [0,-1]为空。  初始时j=-1, i=0, 那么[0, -1]为空。
#         while i < len(nums):
#             if nums[i] % 2 == 1:
#                 j += 1
#                 nums[j], nums[i] = nums[i], nums[j]
#             i += 1
#         return nums
class Solution:
    def exchange(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            while l < r and nums[l] % 2 == 1:
                l += 1
            while l < r and nums[r] % 2 == 0:
                r -= 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums


if __name__ == '__main__':
    a = [1,2,3,5,6,8,7]
    Solution().exchange(a)

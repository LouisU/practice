# -*- coding: utf-8 -*-
# author = "Louis"
import collections


# class Solution:
#      def findRepeatNumber(self, nums: [int]) -> int:
#         dic = set()
#         for num in nums:
#             if num in dic: return num
#             dic.add(num)
#         return -1
# class Solution:
#     def findRepeatNumber(self, nums):
#         s = set()
#         for num in nums:
#             if num in s:
#                 return num
#             s.add(num)
#         return -1
class Solution:
    def findRepeatNumber(self, nums):

        i = 0
        while i < len(nums):

            if nums[i] == i:
                # 值 和 索引 对应了
                i += 1
            else:  # nums[i]!=i, 该值应该放到与该值相等的索引中
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                else:
                    nums[nums[i]], num[i] = nums[i], nums[nums[i]]  # 这样值和索引就相等了
        return -1

if __name__ == '__main__':
    pass

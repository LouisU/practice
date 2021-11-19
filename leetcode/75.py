# -*- coding: utf-8 -*-
# author = "Louis"


# 给定一个包含红色、白色和蓝色，一共n 个元素的数组，
# 原地对它们进行排序，使得相同颜色的元素相邻，
# 并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
# 示例 1：
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
#
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 示例 3：
#
# 输入：nums = [0]
# 输出：[0]
# 示例 4：
#
# 输入：nums = [1]
# 输出：[1]

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sort(nums, 0, len(nums))

    def sort(self, arr, l, r):
        # 循环不变量：arr[0:j]为0 arr[j+1:i]为1 arr[gt:r]为2
        # 当i=gt是循环结束
        j = -1
        i = 0
        gt = r
        while i < gt:

            if arr[i] == 0:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            elif arr[i] == 2:
                gt -= 1
                arr[gt],arr[i] = arr[i], arr[gt]
            else:
                i += 1





if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print("##")

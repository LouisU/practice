# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    def maxLength(self, arr):
        # write code here
        l = r = 0
        max_len = 0
        for i in range(len(arr)):
            if arr[i] not in arr[l:r]:
                r = i + 1
            else:
                l = l + arr[l:r].index(arr[i]) + 1
                r = i + 1
            max_len = max(r - l, max_len)
        return max(r - l, max_len)

    # def maxLength(self, arr):
    #     # write code here
    #     l = len(arr)
    #     a = {}
    #     maxl = 0
    #     j = -1
    #     for i in range(l):
    #         if arr[i] in a and j < a[arr[i]]:
    #             j = a[arr[i]]
    #         a[arr[i]] = i
    #         if (i - j) > maxl:
    #             maxl = i - j
    #     return maxl


if __name__ == '__main__':
    pass

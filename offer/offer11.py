# -*- coding: utf-8 -*-
# author = "Louis"
class Solution:
    def minArray(self, numbers):
        l = 0
        r = len(numbers) - 1
        while l < r:
            m = (l+r) // 2
            if numbers[m] > numbers[r]:
                l = m + 1
            elif numbers[m] < numbers[r]:
                r = m
            else:
                r -= 1
        return numbers[l]


if __name__ == '__main__':
    a = [1, 3, 3]
    print(Solution().minArray(a))

# -*- coding: utf-8 -*-
# author = "Louis"
# 中心扩散法
class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        if A == A[::-1]:
            return n
        max_len = 1
        i = 0
        while i <= n - 1:
            left = right = i
            while left >=0 and right <= n - 1:
                if A[left] == A[right]:
                    max_len = max(max_len, right - left + 1)
                    left -= 1
                    right += 1
                else:
                    break
            left, right = i, i+1
            while left >=0 and right <= n -1:
                if A[left] == A[right]:
                    max_len = max(max_len, right - left + 1)
                    left -= 1
                    right += 1
                else:
                    break
            i += 1
        return max_len

if __name__ == '__main__':
    pass

# -*- coding: utf-8 -*-
# author = "Louis"
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            if n & 1:
                count +=1

            n = n >> 1
        return count

if __name__ == '__main__':
    Solution().NumberOf1(-10)

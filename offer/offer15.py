# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res

if __name__ == '__main__':
    pass

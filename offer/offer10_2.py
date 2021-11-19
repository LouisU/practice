# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            cur, pre = 1, 1
            for _ in range(2, n+1):
                cur, pre = cur+pre, cur
            return cur % 1000000007

if __name__ == '__main__':
    pass

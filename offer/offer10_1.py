# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    # d = {0: 0, 1: 1}

    # def fib(self, n: int) -> int:

    #     if n in self.d.keys():
    #         return self.d[n]
    #     else:
    #         self.d[n] = self.fib(n - 1) + self.fib(n - 2)
    #         return self.d[n] % 1000000007

    def fib(self, n):
        if n <= 1:
            return n
        pre = 0
        cur = 1
        for i in range(2, n + 1):
            cur, pre = cur + pre, cur
        return cur % 1000000007

if __name__ == '__main__':
    pass

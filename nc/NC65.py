# -*- coding: utf-8 -*-
# author = "Louis"
class Solution:
    d = {0: 0, 1: 1}

    def fib(self, n: int) -> int:

        if n in self.d.keys():
            return self.d[n]
        else:
            self.d[n] = self.fib(n - 2) + self.fib(n - 1)
            return self.d[n]


if __name__ == '__main__':
    print(Solution().fib(45))

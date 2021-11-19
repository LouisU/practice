# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int):
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res
if __name__ == '__main__':
    pass

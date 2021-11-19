# -*- coding: utf-8 -*-
# author = "Louis"
class Solution:
    # def reverseLeftWords(self, s: str, n: int) -> str:

    #     return ''.join([s[n:], s[:n]])
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])

        return ''.join(res)

if __name__ == '__main__':
    pass

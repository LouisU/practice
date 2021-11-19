# -*- coding: utf-8 -*-
# author = "Louis"
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, str1, str2):
        # write code here
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        l = 1
        r = len(str2)
        max_len, max_s, max_e = 0, 0, 0
        while l < r:
            mid = (r + l + 1) // 2
            res, s, e = self.find(str1, str2, mid)
            if e - s > max_len:
                max_len, max_s, max_e = e - s, s, e
            if res:
                l = mid
            else:
                r = mid - 1

        return str2[max_s:max_e]

    def find(self, s1, s2, length):
        for j in range(len(s2) - length + 1):
            commpare = s2[j:j + length]
            if commpare in s1:
                return length, j, j + length
        return 0, 0, 0

if __name__ == '__main__':
    pass

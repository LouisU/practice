# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    def singleNumber(self, nums):
        dic = {}
        for num in nums:
            if dic.get(num, False) is False:
                dic[num] = 1
            else:
                dic[num] += 1

        for key, value in dic.items():
            if value == 1:
                return key
        return False


if __name__ == '__main__':
    pass

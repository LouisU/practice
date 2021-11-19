# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    # def MoreThanHalfNum_Solution(self, numbers):
    #     # write code here
    #     l = len(numbers)
    #     half = int(l/2)
    #     max_index = -1
    #     for i in range(len(numbers)):
    #         times = numbers.count(numbers[i])
    #         if times > half:
    #             max_index = i
    #             break
    #     return numbers[max_index]

    def MoreThanHalfNum_Solution(self, numbers):
        numbers.sort()
        return numbers[len(numbers)//2]

if __name__ == '__main__':
    pass

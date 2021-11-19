# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    def findContinuousSequence(self, target):

        i,j=1,2
        res = []
        while i<j:
            total = (j + i)*(j-i+1)/2
            if total == target:
                res.append([h for h in range(i, j + 1)])
                j+=1
            elif total > target:
                i+=1
            else:
                j+=1

        return res


    # 此法错误
    # def findContinuousSequence(self, target):
    #     if target == 1:
    #         return [1]
    #     arr = []
    #
    #     half = target // 2
    #     for value in range(2, half):
    #         number = target // value
    #         tem_arr = []
    #         if target % value == 0 and number % 2 == 1:
    #             balance = number // 2
    #             start = value - balance
    #             if start < 0:
    #                 continue
    #
    #             for j in range(number):
    #                 tem_arr.append(start+j)
    #             arr.append(tem_arr)
    #
    #     if target % 2 == 1:
    #         arr.append([half, half+1])
    #
    #     return arr
if __name__ == '__main__':
    print(Solution().findContinuousSequence(100))

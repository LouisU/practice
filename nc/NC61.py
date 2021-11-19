# -*- coding: utf-8 -*-
# author = "Louis"

# 两数之和
class Solution:
    # def twoSum(self , numbers , target ):
    #     # write code here
    #     i = j = 0
    #     arr_len = len(numbers)
    #     for i in range(arr_len):
    #         for j in range(i+1, arr_len):
    #             if numbers[i]+numbers[j] == target:
    #                 return i+1, j+1
    def twoSum(self , numbers , target ):
        # write code here
        i = j = 0
        arr_len = len(numbers)
        for i in range(arr_len):
            left = target - numbers[i]
            if left in numbers and numbers.index(left) != i:
                if i < numbers.index(left):
                    return i + 1, numbers.index(left) + 1
                else:
                    return numbers.index(left) + 1, i + 1

# arr.index(x) O(n)
# x in arr   O(n)
if __name__ == '__main__':
    a = [2,2,4]
    t = 4
    print(Solution().twoSum(a,t))
    import time

    arr = [i for i in range(100000000)]
    s = time.time()
    if 9999 in arr:
        print(1)
    print(time.time() - s)

    s = time.time()
    for i in arr:
        if i == 9999:
            print(1)
            break
    print(time.time() - s)


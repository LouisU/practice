# -*- coding: utf-8 -*-
# author = "Louis"
# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
class Solution:
    d = {}
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            if number in self.d.keys():
                return self.d[number]
            else:
                self.d[number] = self.jumpFloor(number-1) + self.jumpFloor(number-2)
                return  self.d[number]



if __name__ == '__main__':
    pass

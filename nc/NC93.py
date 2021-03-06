# -*- coding: utf-8 -*-
# author = "Louis"

# 题目描述
# 设计LRU缓存结构，该结构在构造时确定大小，
# 假设大小为K，并有如下两个功能
# set(key, value)：将记录(key, value)
# 插入该结构
# get(key)：返回key对应的value值
# [要求]
# 1. set和get方法的时间复杂度为O(1)
# 2. 某个key的set或get操作一旦发生，认为这个key的记录成了最常使用的。
# 3. 当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。
# 若opt = 1，接下来两个整数x, y，表示set(x, y)
# 若opt = 2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回 - 1
# 对于每个操作2，输出一个答案
# 示例1
# 输入
# [[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3
# 返回值
# [1, -1]
# 说明
# 第一次操作后：最常使用的记录为("1", 1)
# 第二次操作后：最常使用的记录为("2", 2)，("1", 1)
# 变为最不常用的
# 第三次操作后：最常使用的记录为("3", 2)，("1", 1)
# 还是最不常用的
# 第四次操作后：最常用的记录为("1", 1)，("2", 2)
# 变为最不常用的
# 第五次操作后：大小超过了3，所以移除此时最不常使用的记录("2", 2)，加入记录("4", 4)，并且为最常使用的记录，然后("3", 2)
# 变为最不常使用的记录
# 备注:
# 1 \leq
# K \leq
# N \leq
# 10 ^ 51≤K≤N≤10
# 5
#
# -2 \times
# 10 ^ 9 \leq
# x, y \leq
# 2 \times
# 10 ^ 9−2×10
# 9
# ≤x, y≤2×10
# 9

class Solution:
    d = {}

    def LRU(self, operators, k):
        # write code here

        for op_k_v in operators:
            if op_k_v[0] == 1:
                self.set(op_k_v[1], op_k_v[2])
                self.adjust(k)
            else:
                print(self.get(op_k_v[1]))

    def get(self, key):
        value = self.d.get(key, -1)
        if value != -1:
            self.d.pop(key)
            self.d[key] = value
        return value

    def set(self, key, value):
        if key in self.d.keys():
            self.d.pop(key)
            self.d[key] = value
        else:
            self.d[key] = value

    def adjust(self, length):
        d_len = len(self.d)
        if d_len > length:
            self.d.pop(list(self.d.keys())[0])




if __name__ == '__main__':
    pass

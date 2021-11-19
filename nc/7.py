# -*- coding: utf-8 -*-
# author = "Louis"
# 题目描述
# 数据表记录包含表索引和数值（int范围的正整数），
# 请对表索引相同的记录进行合并，
# 即将相同索引的数值进行求和运算，
# 输出按照key值升序进行输出。
#
# 输入描述:
# 先输入键值对的个数
# 然后输入成对的index和value值，以空格隔开
#
# 输出描述:
# 输出合并后的键值对（多行）
#
# 示例1
# 输入
# 4
# 0 1
# 0 2
# 1 2
# 3 4
# 输出
# 0 3
# 1 2
# 3 4

if __name__ == '__main__':

    k_v_len = int(input())
    arr = [0 for _ in range(k_v_len)]
    for _ in range(k_v_len):
        index, value = input().split(" ")
        arr[int(index)] += int(value)
    for i, v in enumerate(arr):
        if v != 0:
            print(i, v)

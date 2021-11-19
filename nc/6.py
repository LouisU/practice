# -*- coding: utf-8 -*-
# author = "Louis"
# 题目描述
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
#
# 输入描述:
# 输入一个正浮点数值
#
# 输出描述:
# 输出该数值的近似整数值
#
# 示例1
# 输入
# 5.5
# 输出
# 6

def func(f_num_str):
    f_num_list = f_num_str.split('.')
    if int(f_num_list[1][0]) >=5:
        print(int(f_num_list[0])+1)
    else:
        print(int(f_num_list[0]))

def func2(f_num_str):
    print(int(float(f_num_str)+0.5))

if __name__ == '__main__':
    f_num = input()
    func2(f_num)
# -*- coding: utf-8 -*-
# author = "Louis"
# 题目描述
# •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
#
# 输入描述:
# 连续输入字符串(输入多次,每个字符串长度小于100)
#
# 输出描述:
# 输出到长度为8的新字符串数组
#
# 示例1
# 输入
# abc
# 123456789
# 输出
# abc00000
# 12345678
# 90000000
def printString(str_line):
    arr = []
    step = 8
    r = step
    l = 0
    while True:
        if len(str_line) - r >= 0:
            arr.append(str_line[l:r])
        else:
            arr.append(str_line[l:len(str_line)] + "0" * (step - (len(str_line) - l)))
            break
        l += step
        r += step
    for _ in arr:
        print(_)
def printString2(str_line):
    arr = []
    while True:
        if len(str_line) > 8:
            arr.append(str_line[:8])
            str_line = str_line[8:]
        else:
            arr.append(str_line[8:] + "0" * (8 - len(str_line)))
            break
    for _ in arr:
        print(_)

if __name__ == '__main__':

    a = input()
    b = input()
    printString(a)
    printString(b)

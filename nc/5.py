# -*- coding: utf-8 -*-
# author = "Louis"

# 题目描述
# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
#
# 最后一个数后面也要有空格
#
# 输入描述:
# 输入一个long型整数
#
# 输出描述:
# 按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
#
# 示例1
# 输入
# 180
# 输出
# 2 2 3 3 5
#################方案一 ， 执行时间太长 不会通过。
def pop_zhi():
    n = 2
    while True:
        if n <= 3:
            yield n
        else:
            mid_int = int(n / 2) + 1
            is_it = True
            for i in range(2, mid_int):
                if n % i == 0:
                    is_it = False
                    break
            if is_it:
                yield n
        n += 1


def is_zhi(n):
    mid_int = int(n / 2) + 1
    is_it = True
    for i in range(2, mid_int):
        if n % i == 0:
            is_it = False
            break
    return is_it
#############方案二： 递归算法
    # 说下原理，上面评论区为啥不判断是不是质因子：因为从2开始除这个数，2
    # 如果能除尽，就用2除（换言之就轮不到4，8，10
    # 等来除）；2
    # 不能除，那用3去除，3
    # 能除尽就除，除不尽i继续递增；假如i递增到4了
    # （同志们想想是不是直接将4pass了？因为4如果能除尽，那么它前面的2就已经去除了，根本轮不到4除），
    # i再增到5，能除尽就除，除不尽用下一个6去除，
    # 同理，肯定pass，因为6如果能除尽，前面的3早就除了，轮不到6去除。。。
    # 由此可知，得到的因子自然就是质因子了

# num1 = a * num2
# num2 = b * num3
# ...
# numX = 1 * numX
#   求解最基本问题：当num是质数时， 打印print(num, end=' ')。
#   把原问题转化成更小的问题： 当num不是质数时，那么num=一个质数*num2,问题转化为求num2有哪些质数组成
def func(num):
    is_it = True
    mid_int = int(num ** 0.5) + 1
    for i in range(2, mid_int) :
        yu = num % i
        if yu == 0:
            b = num // i
            is_it = False
            print(i, end=' ')
            func(b)
            break
    if is_it:
        print(num,end=' ')


if __name__ == '__main__':
    # a = pop_zhi()
    # for i in range(100):
    #     print(next(a))
    # for i in range(1000):
    #     if is_zhi(i):
    #         print(i)
    #     else:
    #         if i % 2 == 0:
    #             print("{} / 2".format(i))
    #         elif i % 3 == 0:
    #             print("{} / 3".format(i))
    #         elif i % 5 == 0:
    #             print("{} / 5".format(i))
    #         elif i % 7 == 0:
    #             print("{} / 7".format(i))
    #         else:
    #             print("{} / xx".format(i))
    # num = int(input())

    # num = int(input())
    # def func(num):
    #     prime_num = 1
    #     for i in range(2, int(num ** 0.5 + 2)):
    #         if num % i == 0:
    #             prime_num = 0
    #             b = int(num / i)
    #             print(str(i), end=' ')
    #             func(b)
    #             break
    #     if prime_num == 1:
    #         print(str(num), end=' ')


    func(1)






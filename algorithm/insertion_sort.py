# coding=utf-8
"""
核心：通过构建有序序列，对于未排序序列，
在已排序序列中从后向前扫描(对于单向链表则只能从前往后遍历)，
找到相应位置并插入。
实现上通常使用in-place排序(需用到O(1)的额外空间)

从第一个元素开始，该元素可认为已排序
取下一个元素，对已排序数组从后往前扫描
若从排序数组中取出的元素大于新元素，则移至下一位置
重复步骤3，直至找到已排序元素小于或等于新元素的位置
插入新元素至该位置
重复2~5
"""
from common import tools


# @tools.count
# def main(alist):
#     if len(alist) < 2:
#         return alist
#
#     # 循环不变量是alist[0:i]已经排序，alist[i:n]还未排序
#     for i in range(1, len(alist)):
#         insert_value = alist[i]
#         for j in range(i):
#             if alist[i - j - 1] > insert_value:
#                 alist[i - j], alist[i - j - 1] = alist[i - j - 1], insert_value
#             else:
#                 break
#     return alist


@tools.count
def main(alist):

    if len(alist) < 2:
        return alist
    # 循环不变量是alist[0:i]已经排序，alist[i:n]还未排序
    for i in range(1, len(alist)):
        insert_value = alist[i]
        i_loop = i - 1
        while i_loop >= 0:
            if alist[i_loop] > insert_value:
                alist[i_loop + 1] = alist[i_loop]
                i_loop -= 1
            else:
                alist[i_loop+1] = insert_value
                break
        if i_loop == -1:
            alist[0] = insert_value

    return alist


def main_4_merger_sort(alist, left, right):

    if len(alist) < 2:
        return alist
    # 循环不变量是alist[0:i]已经排序，alist[i:n]还未排序
    for i in range(left+1, right+1):
        insert_value = alist[i]
        i_loop = i - 1
        while i_loop >= left:
            if alist[i_loop] > insert_value:
                alist[i_loop + 1] = alist[i_loop]
                i_loop -= 1
            else:
                alist[i_loop+1] = insert_value
                break
        if i_loop < left:
            alist[left] = insert_value

    return alist
if __name__ == "__main__":
    # alist = [1,6,4,7,2]
    # print(main(alist))
    from copy import deepcopy
    nums = [1000, 10000]
    for i in nums:
        alist = tools.ArrayGenerator.randomList(i)
        alist2 = deepcopy(alist)
        print(tools.SortingTest.isOrdered(main(alist)))
        print(tools.SortingTest.isOrdered(main_4_merger_sort(alist2, 0, len(alist2)-1)))

        alist = tools.ArrayGenerator.orderedList(i)
        print(tools.SortingTest.isOrdered(main(alist)))

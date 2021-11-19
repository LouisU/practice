# coding=utf-8
# def bubble_sort(alist):
#
#     # 取列表最左边的元素，开始于右边相邻的元素对对比。
#     #       如果左边大于右边，那么左右元素互换位置。取右边的值与下一个元素比较。
#     #       如果左边小于右边，取右边的值与下一个元素比较。
#     # 直到比较完列表最右端的元素。
#
#     len_list = len(alist)
#     if len_list <= 1:
#         return alist
#
#     for j in range(len_list):
#         print("{} - {}".format(j, alist))
#         for i in range(1, len_list - j):
#             if alist[i - 1] > alist[i]:
#                 alist[i], alist[i - 1] = alist[i - 1], alist[i]
#     return alist

def bubble_sort(alist):
    if len(alist) <= 1:
        return alist
    r = len(alist) - 1
    while r > 0:
        l = 0
        while l < r:
            if alist[l] > alist[l+1]:
                alist[l], alist[l+1] = alist[l+1], alist[l]
            l += 1
        r -= 1
    return alist

if __name__ == "__main__":
    alist = [1, 7, 4, 9, 3, 0, -1, 11, -9]
    print(bubble_sort(alist))

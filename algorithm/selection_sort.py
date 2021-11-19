# coding=utf-8
from common import tools
# 一个无序数组 用选择排序的方法排序。
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other_student):
        return True if (other_student.score - self.score) > 0 else False

    def __repr__(self):
        return "score:{} name:{}\n".format(
            self.score, self.name
        )

@tools.count
def main(alist):
    # 循环不变量 alist[0:i]是有序子序列，alist[i+1,n]为无序子序列
    list_len = len(alist)
    for i in range(list_len):
        min_index = i
        for j in range(i, list_len):
            is_ture = alist[j] < alist[min_index]
            if is_ture:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


if __name__ == "__main__":
    nums = [1000, 10000]
    for i in nums:
        alist = tools.ArrayGenerator.randomList(i)
        print(tools.SortingTest.isOrdered(main(alist)))

        alist = tools.ArrayGenerator.orderedList(i)
        print(tools.SortingTest.isOrdered(main(alist)))
    # alist = [
    #     Student("Louis", 59),
    #     Student("Bob", 10),
    #     Student("Andy", 89),
    #     Student("XU", 78)
    # ]
    # print(main(alist))

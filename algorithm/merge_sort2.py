# -*- coding: utf-8 -*-
# author = "Louis"

class Solution:
    # 递归
    def mergeList(self, unsort_list):

        if len(unsort_list) <= 1:
            return unsort_list

        mid = int(len(unsort_list) / 2)
        left_list = self.mergeList(unsort_list[:mid])
        print('l_list_sorted:{}'.format(left_list))
        right_list = self.mergeList(unsort_list[mid:])
        print('r_list_sorted:{}'.format(right_list))
        return self.mergeListSorted(left_list, right_list)

    # 非递归
    def mergeList2(self, unsort_list):
        unsort_list_len = len(unsort_list)
        if unsort_list_len <=1:
            return unsort_list
        sorted_list = []
        level = 2

        while level//2 <= unsort_list_len:
            for i in range(0, unsort_list_len, level):
                start = i
                end = i + level if i+level <= unsort_list_len else unsort_list_len
                tem_list = unsort_list[start:end]
                # mid = len(tem_list) // 2
                mid = level // 2
                leftlist = tem_list[:mid]
                rightlist = tem_list[mid:]
                result_list = self.mergeListSorted(leftlist, rightlist)
                unsort_list[start:end] = result_list
            level *= 2

        return unsort_list

    def mergeListSorted(self, alist, blist):

        a_len, b_len = len(alist), len(blist)
        i = j = 0
        clist = []
        while a_len and b_len:
            if alist[i] < blist[j]:
                clist.append(alist[i])
                i += 1
                a_len -= 1
            else:
                clist.append(blist[j])
                j += 1
                b_len -= 1

        if a_len:
            clist.extend(alist[-a_len:])
        if b_len:
            clist.extend(blist[-b_len:])

        return clist


if __name__ == '__main__':
    a = [4,1,3, 12, 7,-1, 10,9,15, 5,6,2]
    print(Solution().mergeList2(a))
# -*- coding: utf-8 -*-
# author = "Louis"

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 算法很浪漫
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pHead1_index = pHead1
        pHead2_index = pHead2
        while pHead1_index != pHead2_index:

            if pHead1_index is not None:
                pHead1_index = pHead1_index.next
            else:
                pHead1_index = pHead2
            if pHead2_index is not None:
                pHead2_index = pHead2_index.next
            else:
                pHead2_index = pHead1
        return pHead1_index


if __name__ == '__main__':
    pass


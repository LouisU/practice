# -*- coding: utf-8 -*-
# author = "Louis"
# 合并有序链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
#
# @param l1 ListNode类
# @param l2 ListNode类
# @return ListNode类
#
class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        # write code here
        lhead = lend = ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next

            lend.next = temp
            lend = lend.next

        if l1 is None:
            lend.next = l2
        if l2 is None:
            lend.next = l1

        return lhead.next



if __name__ == '__main__':
    pass

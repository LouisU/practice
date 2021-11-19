# -*- coding: utf-8 -*-
# author = "Louis"

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        p = None
        while pHead is not None:
            p = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = p

        return pre

# write code here


if __name__ == '__main__':
    pass

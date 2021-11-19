# -*- coding: utf-8 -*-
# author = "Louis"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # def deleteNode(self, head: ListNode, val: int):

    #     dummy_head = pre_head = ListNode(None)
    #     pre_head.next = head
    #     while head is not None:
    #         if head.val == val:
    #             pre_head.next = head.next
    #             break
    #         head = head.next
    #         pre_head = pre_head.next

    #     return dummy_head.next

    def deleteNode(self, head: ListNode, val: int):

        if val == head.val:
            return head.next
        pre = head
        cur = head.next
        while cur is not None:
            if cur.val == val:
                pre.next = cur.next
                break
            cur = cur.next
            pre = pre.next

        return head

if __name__ == '__main__':
    pass

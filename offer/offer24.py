# -*- coding: utf-8 -*-
# author = "Louis"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return head

        dummy_head = ListNode(None)
        while head is not None:
            node = head
            head = head.next
            node.next = dummy_head.next
            dummy_head.next = node
        return dummy_head.next
if __name__ == '__main__':
    pass

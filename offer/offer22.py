# -*- coding: utf-8 -*-
# author = "Louis"
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def getKthFromEnd(self, head, k):
        ahead = head
        latter = head
        while k > 0:
            ahead = ahead.next
            k -= 1
        while ahead is not None:
            ahead = ahead.next
            latter = latter.next

        return latter


if __name__ == '__main__':
    pass

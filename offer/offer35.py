# -*- coding: utf-8 -*-
# author = "Louis"
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        mhead = head
        dummy_head = Node(0)
        last_head = dummy_head
        while mhead is not None:
            node = Node(mhead.val)
            dic[mhead] = node
            last_head.next = node
            last_head = last_head.next
            mhead = mhead.next
        mhead = head
        while mhead is not None:
            if mhead.random is None:
                dic[mhead].random = None
            else:
                dic[mhead].random = dic[mhead.random]
            mhead = mhead.next

        return dummy_head.next

if __name__ == '__main__':
    pass

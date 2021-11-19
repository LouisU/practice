# -*- coding: utf-8 -*-
# author = "Louis"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def reversePrint(self, head):
#         mhead = head
#         arr = []
#         while mhead is not None:
#             arr.append(mhead.val)
#             mhead = mhead.next
#         arr.reverse()
#         return arr
class Solution:
    def reversePrint(self, head):
        if head:
            return self.reversePrint(head.next) + [head.val]
        else:
            return []

if __name__ == '__main__':
    a = [1,3,2]
    head = ListNode(None)
    while len(a):
        val = a.pop()
        node = ListNode(val)
        node.next = head.next
        head.next = node
    head = head.next

    print(Solution().reversePrint(head))



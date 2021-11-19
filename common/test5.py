# -*- coding: utf-8 -*-
# author = "Louis"


# 2.
# 两数相加
# 给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
# 并且它们的每个节点只能存储一位数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字
# 0
# 之外，这两个数都不会以
# 0
# 开头。
# 示例：
# 输入：2 -> 4 -> 3, 5 -> 6 -> 4
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generateListNode(l: list):
    l1 = ListNode(None)
    l3 = l1
    for val in l:
        l3.next = ListNode(val)
        l3 = l3.next
    return l1.next

class Solution_001:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        overflow = 0
        res_link = ListNode(None)
        res_last_node = res_link
        while l1 is not None or l2 is not None:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            ab_sum = a + b + overflow
            overflow = ab_sum // 10
            res = ab_sum % 10
            node = ListNode(res)
            res_last_node.next = node
            res_last_node = res_last_node.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return res_link.next
if __name__ == '__main__':
    l1 = generateListNode([2, 5, 3, 1])
    l2 = generateListNode([5, 6, 4])
    res_link = Solution_001().addTwoNumbers(l1, l2)
    while res_link is not None:
        print(res_link.val, end=' ')
        res_link = res_link.next

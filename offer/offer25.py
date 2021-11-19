# -*- coding: utf-8 -*-
# author = "Louis"


'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：

0 <= 链表长度 <= 1000
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "listNode:{}".format(self.val)


class Solution:
    def mergeTwoLists(self, l1, l2):
        new_list = pre = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
               cur_node = l1
               l1 = l1.next
            else:
                cur_node = l2
                l2 = l2.next
            pre.next = cur_node
            pre = pre.next
        if l1 is None:
            pre.next = l2
        if l2 is None:
            pre.next = l1

        return new_list.next


if __name__ == '__main__':
    alist = ListNode(1)
    alist.next = ListNode(2)
    alist.next.next = ListNode(4)
    alist.next.next.next = ListNode(7)
    alist.next.next.next.next = ListNode(10)

    blist = ListNode(5)
    blist.next = ListNode(6)
    blist.next.next = ListNode(9)
    blist.next.next.next = ListNode(12)

    so = Solution()
    new_list = so.mergeTwoLists(alist, blist)
    while new_list:
        print(new_list.val)
        new_list = new_list.next

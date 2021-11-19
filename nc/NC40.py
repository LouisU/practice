# -*- coding: utf-8 -*-
# author = "Louis"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addInList(self, head1, head2):
        # write code here
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)
        overflow_before = 0
        head3 = ListNode(None)
        while head1 is not None or head2 is not None:
            a = b = 0
            if head1 is not None:
                a = head1.val
                head1 = head1.next
            if head2 is not None:
                b = head2.val
                head2 = head2.next
            value = a + b + overflow_before
            overflow, value = value // 10, value % 10
            overflow_before = overflow

            temp = head3.next
            head3.next = ListNode(value)
            head3.next.next = temp

        return head3.next

    def reverse(self, head):
        new_link = ListNode(None)
        while head is not None:
            temp = new_link.next
            new_link.next = head
            head = head.next
            new_link.next.next = temp
        return new_link.next


if __name__ == '__main__':
    pass

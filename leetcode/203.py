# -*- coding: utf-8 -*-
# author = "Louis"

# 删除链表中值为val的所有元素；


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self != None:
            return "{}->{}".format(self.val, self.next)
# 没有虚拟节点
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:


        while(head != None and head.val==val):
            head = head.next
        if (head == None):
            return head
        prev = head
        while(prev.next):
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return head
# 有虚拟头节点
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        vhead = ListNode(None, head)

        prev = vhead
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return vhead.next

# 用递归的思想
class Solution3:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 将问题拆分一个基本问题和更小的问题的组合；
        if(head == None):
            return head

        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        return head


def list2link(a):
    for i in range(len(a)):
        if i == 0:
            head = ListNode(a[i], None)
            tail = head
        else:
            tail.next = ListNode(a[i], None)
            tail = tail.next
    return head

if __name__ == '__main__':
    a = [7,7,7,7]
    b = [1,2,6,3,4,5,6]
    heada = list2link(a)
    headb = list2link(b)

    head = Solution3().removeElements(heada, 7)
    print(head)
    head = Solution3().removeElements(headb, 6)
    print(head)

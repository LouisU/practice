# -*- coding: utf-8 -*-
# author = "Louis"

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "node value: {} next node is exist:{}".format(
            self.value, True if self.next else False)

# 链表首有head指针， 链表尾有tail指针
class NodeLink:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def add(self, index, value):
        prev = self.head
        node = Node(value, None)
        if index == 0:
            node.next = self.head
            self.head = node
            if self.size == 0:
                self.tail = node
        elif index == self.size:
            self.tail.next = node
            self.tail = node
        else:
            for i in range(index - 1):
                prev = prev.next
            node.next = prev.next
            prev.next = node
        self.size += 1

    def addFirst(self, value):
        self.add(0, value)

    def addLast(self, value):
        self.add(self.size, value)

    def get(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.value

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.size-1)

    def set(self, index, value):
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.value = value

    def contains(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def remove(self, index):
        prev = self.head
        if index == 0:
            self.head = self.head.next
            prev.next = None
            self.size -= 1
            return prev.value
        else:
            for i in range(index-1):
                prev = prev.next

            delNode = prev.next
            prev.next = delNode.next
            delNode.next = None
            self.size -= 1
            return delNode.value

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self.size - 1)

    def __repr__(self):
        s = "head: "
        e = ' tail.'
        node = self.head
        m = ''
        while node:
            m = "{}{}{}".format(m, node.value, "->")
            node = node.next
        return "{} {} {}".format(s, m, e)


if __name__ == '__main__':
    link = NodeLink()
    link.addLast(999)
    print("a")
    for i in range(10):
        link.addFirst(i)
    print(link)
    link.add(5, 100)
    link.addLast(99)
    print(link)
    print(link.size, link.head)
    print(link.get(0), link.get(1), link.get(11))
    link.set(11, 199)
    print(link.getFirst(), link.getLast())
    print(link.contains(0), link.contains(101))
    print(link)
    print(link.remove(3))
    print(link)
    print(link.removeFirst())
    print(link)
    print(link.removeLast())
    print(link)

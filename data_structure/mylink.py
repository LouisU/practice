# -*- coding: utf-8 -*-
# author = "Louis"

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "node value: {} next node is exist:{}".format(
            self.value, True if self.next else False)


# 不用虚拟头结点
class NodeLink:

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def add(self, index, value):
        if index < 0 or index > self.size:
            raise ValueError("index should between 0-{}".format(self.size))
        if index == 0:
            self.head = Node(value, self.head)
            self.size += 1
            return
        prev = self.head
        for i in range(index - 1):
            prev = prev.next
        prev.next = Node(value, prev.next)
        self.size += 1

    def addFirst(self, value):
        self.add(0, value)

    def addLast(self, value):
        self.add(self.size, value)

    def get(self, index):
        if index < 0 or index > self.size:
            raise ValueError("index should between 0-{}".format(self.size))
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.value

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.size - 1)

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
        if index == 0:
            delNode = self.head
            self.head = self.head.next
            delNode.next = None
        else:
            prev = self.head
            for i in range(index - 1):
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


# 用虚拟头结点
class NodeLink2:

    def __init__(self):
        self.dummy_head = Node(None, None)
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def add(self, index, value):
        prev = self.dummy_head
        node = Node(value, None)
        for i in range(index):
            prev = prev.next

        node.next = prev.next
        prev.next = node
        self.size += 1

    def addFirst(self, value):
        self.add(0, value)

    def addLast(self, value):
        self.add(self.size, value)

    def get(self, index):
        cur = self.dummy_head.next
        for i in range(index):
            cur = cur.next
        return cur.value

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.size - 1)

    def set(self, index, value):
        cur = self.dummy_head.next
        for i in range(index):
            cur = cur.next
        cur.value = value

    def contains(self, value):
        cur = self.dummy_head.next
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def remove(self, index):
        prev = self.dummy_head
        for i in range(index):
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
        node = self.dummy_head.next
        m = ''
        while node:
            m = "{}{}{}".format(m, node.value, "->")
            node = node.next
        return "{} {} {}".format(s, m, e)


# (不用虚拟头节点)用递归的思想来实现链表的操作
class NodeLink3:

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def add(self, index, value):
        if index < 0 or index > self.size:
            raise ValueError("index should between 0--{}".format(self.size))
        self.head = self.addR(self.head, index, value)
        self.size += 1

    def addR(self, link, index, value):
        if index == 0:
            return Node(value, link)
        link.next = self.addR(link.next, index - 1, value)
        return link

    def addFirst(self, value):
        self.add(0, value)

    def addLast(self, value):
        self.add(self.size, value)

    def get(self, index):
        return self.getR(self.head, index)

    def getR(self, link, index):
        if index == 0:
            return link.value
        return self.getR(link.next, index - 1)

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.size - 1)

    def set(self, index, value):
        return self.setR(self.head, index, value)

    def setR(self, link, index, value):
        if index == 0:
            link.value = value
            return
        return self.setR(link.next, index - 1, value)

    def contains(self, value):
        return self.containsR(self.head, value)

    def containsR(self, link, value):
        if link == None:
            return False
        elif link.value == value:
            return True
        return self.containsR(link.next, value)

    def remove(self, index):
        if index < 0 or index > self.size:
            raise ValueError("index should between 0-{}".format(self.size))
        self.head = self.removeR(self.head, index)
        self.size -= 1

    def removeR(self, link, index):
        if index == 0:
            return link.next
        link.next = self.removeR(link.next, index - 1)
        return link

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self.size - 1)

    def removeElements(self, val):
        self.head = self.removeElementsR(self.head, val)

    def removeElementsR(self, link, val):
        if link == None:
            return link

        if link.value == val:
            self.size -= 1
            link = self.removeElementsR(link.next, val)
        else:
            link.next = self.removeElementsR(link.next, val)
        return link

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
    link = NodeLink3()
    for i in range(10):
        link.addFirst(i)
    link.add(0, 6)
    link.add(6, 6)
    link.addLast(6)
    link.removeElements(6)
    print(link.get(2))
    link.add(5, 100)
    link.addLast(99)
    print(link)
    # print(link.size, link.dummy_head)
    print(link.get(0), link.get(1), link.get(11))
    link.set(11, 199)
    print(link.getFirst(), link.getLast())
    print(link.contains(0), link.contains(101))
    print(link)
    print(link.remove(5))
    print(link)
    print(link.removeFirst())
    print(link)
    print(link.removeLast())
    print(link)

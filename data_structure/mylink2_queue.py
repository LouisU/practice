# -*- coding: utf-8 -*-
# author = "Louis"
from mylink2 import NodeLink


class queue:

    def __init__(self):
        self.queue = NodeLink()

    def enqueue(self, value):
        self.queue.addLast(value)

    def dequeue(self):
        return self.queue.removeFirst()

    def isEmpty(self):
        return self.queue.isEmpty()

    def getSize(self):
        return self.queue.getSize()

    def __repr__(self):
        return self.queue.__repr__()


if __name__ == '__main__':

    q = queue()
    print(q.isEmpty())
    for i in range(10):
        q.enqueue(i)
        print(q)

    print(q.isEmpty())
    print(q.getSize())
    for i in range(10):
        q.dequeue()
        print(q)
    print(q.isEmpty())
    print(q.getSize())
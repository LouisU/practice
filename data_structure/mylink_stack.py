# -*- coding: utf-8 -*-
# author = "Louis"
from mylink import NodeLink


class linkStack:

    def __init__(self):
        self.stack = NodeLink()

    def isEmpty(self):
        return self.stack.isEmpty()

    def getSize(self):
        return self.stack.getSize()

    def push(self, value):
        return self.stack.addFirst(value)

    def pop(self):
        return self.stack.removeFirst()

    def peek(self):
        return self.stack.getFirst()

    def __repr__(self):
        return self.stack.__repr__()


if __name__ == '__main__':
    stack = linkStack()
    print(stack.isEmpty())
    for i in range(10):
        stack.push(i)
        print(stack)
    print(stack.getSize())
    print(stack.isEmpty())
    for i in range(10):
        stack.pop()
        print(stack)
    print(stack.isEmpty())
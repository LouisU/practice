# -*- coding: utf-8 -*-
# author = "Louis"
from myarray import myArray

# 后进先出
class Stack:

    def __init__(self):
        self.stack = myArray()

    def push(self, value):
        # print(value)
        return self.stack.addLast(value)

    def pop(self):
        return self.stack.removeLast()

    def peek(self):
        return self.stack.getLast()

    def isEmpty(self):
        if self.stack.size == 0:
            return True
        else:
            return False

    def getSize(self):
        return self.stack.size

    def __repr__(self):
        return self.stack.__repr__()

if __name__ == '__main__':
    my_stack = Stack()
    for i in range(10):
        my_stack.push(i)
        print(my_stack)
    print(my_stack.isEmpty())
    print(my_stack.getSize())
    print("----------")
    for i in range(10):
        print(my_stack.pop())
        print(my_stack)
    print("----------")
    print(my_stack.getSize())
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)

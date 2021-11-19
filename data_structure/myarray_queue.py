# -*- coding: utf-8 -*-
# author = "Louis"
from myarray import myArray
from random import randint
from common import tools
# 这种出队时间复杂度是O(n), 当队列中有百万级别的数据量，
# 出队将会很慢。
class arrayQueue:

    def __init__(self):
        self.queue = myArray()

    def enqueue(self, value):
        return self.queue.addLast(value)

    def dequeue(self):
        return self.queue.removeFirst()

    def isEmpty(self):
        return self.queue.isEmpty()

    def getFront(self):
        return self.queue.getFirst()

    def getSize(self):
        return self.queue.size

    def __repr__(self):
        return self.queue.__str__()




class loopQueue:
    def __init__(self, capacity):
        self.queue = [None]  * (capacity + 1)
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if (self.tail + 1) % len(self.queue) == self.head:
            self.resize(self.getCapacity() * 2)
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % len(self.queue)
        self.size += 1
        return value

    def dequeue(self):
        if not self.isEmpty():
            ret_value, self.queue[self.head]= self.queue[self.head], None
            self.head = (self.head + 1) % len(self.queue)
            self.size -= 1
            if self.size < self.getCapacity() // 4 and self.getCapacity() // 4 != 0:
                self.resize(self.getCapacity() // 2)
            return ret_value
        else:
            raise IndexError("Out of range")

    def resize(self, capacity):
        new_queue = [None]  * (capacity + 1)
        loop_key = self.head
        i = 0
        for i in range(self.size):
            new_queue[i] = self.queue[(loop_key + i) % len(self.queue)]

        self.tail = i if self.size == 0 else i + 1
        self.head = 0
        self.queue = new_queue

    def isFull(self):
        if (self.tail + 1) % len(self.queue) == self.head:
            return True
        return False

    def isEmpty(self):
        if self.head == self.tail:
            return True
        return False

    def getFront(self):
        return self.queue[self.head]

    def getCapacity(self):
        return len(self.queue) - 1

    def getSize(self):
        return self.size

    def __repr__(self):
        return "{} head={} tail={} size={} capacity={}".format(
            self.queue[self.head:self.tail], self.head, self.tail, self.size, self.getCapacity()
        )


# 不浪费一个空间j
class loopQueueFull:
    def __init__(self, capacity):
        self.queue = [None]  * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def isFull(self):
        if self.tail == self.head and self.size == len(self.queue):
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            self.resize(self.getCapacity() * 2)
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % len(self.queue)
        self.size += 1
        return value

    def dequeue(self):
        if not self.isEmpty():
            ret_value, self.queue[self.head]= self.queue[self.head], None
            self.head = (self.head + 1) % len(self.queue)
            self.size -= 1
            if self.size < self.getCapacity() // 4 and self.getCapacity() // 4 != 0:
                self.resize(self.getCapacity() // 2)
            return ret_value
        else:
            raise IndexError("Out of range")

    def resize(self, capacity):
        new_queue = [None]  * capacity
        loop_key = self.head
        i = 0
        for i in range(self.size):
            new_queue[i] = self.queue[(loop_key + i) % len(self.queue)]

        self.tail = i
        self.head = 0
        self.queue = new_queue

    def isEmpty(self):
        if self.size == 0 and self.head == self.tail:
            return True
        return False

    def getFront(self):
        return self.queue[self.head]

    def getCapacity(self):
        return len(self.queue)

    def getSize(self):
        return self.size

    def __repr__(self):
        return "{} head={} tail={} size={} capacity={}".format(
            self.queue[self.head:self.tail], self.head, self.tail, self.size, self.getCapacity()
        )


# 浪费一格空间，但不用size变量
class loopQueueWithoutSize:
    def __init__(self, capacity):
        self.queue = [None]  * (capacity + 1)
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if (self.tail + 1) % len(self.queue) == self.head:
            self.resize(self.getCapacity() * 2)
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % len(self.queue)
        return value

    def dequeue(self):
        if not self.isEmpty():
            ret_value, self.queue[self.head]= self.queue[self.head], None
            self.head = (self.head + 1) % len(self.queue)
            if self.getSize() < self.getCapacity() // 4 and self.getCapacity() // 4 != 0:
                self.resize(self.getCapacity() // 2)
            return ret_value
        else:
            raise IndexError("Out of range")

    def resize(self, capacity):
        new_queue = [None]  * (capacity + 1)
        loop_key = self.head
        i = 0
        while loop_key != self.tail:
            new_queue[i] = self.queue[loop_key]
            i += 1
            loop_key = (loop_key + 1) % len(self.queue)

        self.tail = i
        self.head = 0
        self.queue = new_queue

    def isFull(self):
        if self.getSize() + 1 == len(self.queue):
            return True
        return False

    def isEmpty(self):
        if self.head == self.tail:
            return True
        return False

    def getFront(self):
        return self.queue[self.head]

    def getCapacity(self):
        return len(self.queue) - 1

    def getSize(self):
        v = self.tail - self.head
        if v >= 0:
            return v
        else:
            return len(self.queue) + v

    def __repr__(self):
        return "{} head={} tail={} size={} capacity={}".format(
            self.queue[self.head:self.tail], self.head, self.tail, self.getSize(), self.getCapacity()
        )

# 浪费一格空间，但不用size变量
class Deque:
    def __init__(self, capacity):
        self.queue = [None]  * (capacity + 1)
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if (self.tail + 1) % len(self.queue) == self.head:
            self.resize(self.getCapacity() * 2)
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % len(self.queue)
        return value

    def dequeue(self):
        if not self.isEmpty():
            ret_value, self.queue[self.head]= self.queue[self.head], None
            self.head = (self.head + 1) % len(self.queue)
            if self.getSize() < self.getCapacity() // 4 and self.getCapacity() // 4 != 0:
                self.resize(self.getCapacity() // 2)
            return ret_value
        else:
            raise IndexError("Out of range")

    def addFirst(self, value):
        if self.isFull():
            self.resize(self.getCapacity() * 2)
        self.head = (self.head - 1) % len(self.queue)
        self.queue[self.head] = value
        return value

    def removeLast(self):
        if not self.isEmpty():
            self.tail = (self.tail - 1)
            ret_value, self.queue[self.tail] = self.queue[self.tail], None
            if self.getSize() < self.getCapacity() // 4 and self.getCapacity() // 4 != 0:
                self.resize(self.getCapacity() // 2)
            return ret_value
        else:
            raise IndexError("Out of range")

    def resize(self, capacity):
        new_queue = [None]  * (capacity + 1)
        loop_key = self.head
        i = 0
        while loop_key != self.tail:
            new_queue[i] = self.queue[loop_key]
            i += 1
            loop_key = (loop_key + 1) % len(self.queue)

        self.tail = i
        self.head = 0
        self.queue = new_queue

    def isFull(self):
        if self.getSize() + 1 == len(self.queue):
            return True
        return False

    def isEmpty(self):
        if self.head == self.tail:
            return True
        return False

    def getFront(self):
        return self.queue[self.head]

    def getCapacity(self):
        return len(self.queue) - 1

    def getSize(self):
        v = self.tail - self.head
        if v >= 0:
            return v
        else:
            return len(self.queue) + v

    def __repr__(self):
        if self.isEmpty():
            queue_list = []
        else:
            if self.head < self.tail:
                queue_list = self.queue[self.head:self.tail]
            else:
                queue_list = self.queue[self.head:] + self.queue[:self.tail]
        return "{} head={} tail={} size={} capacity={}".format(
            queue_list, self.head, self.tail, self.getSize(), self.getCapacity()
        )

@tools.count
def testQueue(array_queue, n):
    for _ in range(n):
        array_queue.enqueue(randint(0, n))
    for _ in range(n):
        array_queue.dequeue()


if __name__ == '__main__':
    # my_queue = loopQueue(10)
    # for i in range(1, 20):
    #     if i % 3 == 0:
    #         print("pop out: {}".format(my_queue.dequeue()))
    #     print(my_queue.enqueue(i))
    #     print(my_queue)
    #
    # print("-----")
    # print(my_queue)
    # print("size: {}".format(my_queue.getSize()))
    # print("-----")
    # for _ in range(10):
    #     print("pop out: {}".format(my_queue.dequeue()))
    #     print(my_queue)
    # print("------")
    # print(my_queue.getFront())
    # print(my_queue.dequeue())
    # print(my_queue)
    # print(my_queue.dequeue())
    # print(my_queue)
    #
    # print(my_queue.dequeue())
    # print(my_queue)
    #
    # print(my_queue.dequeue())
    # print(my_queue)
    # 
    # print(my_queue.dequeue())
    # print(my_queue)
    #
    # times = (1000, 5000, 10000)
    #
    # for t in times:
    #     queues = (loopQueue(capacity=10), arrayQueue())
    #     for q in queues:
    #         print("t={} class={}".format(t, q.__class__))
    #         testQueue(q,t)
    #         print('\n')
    # q = loopQueue(capacity=10)
    # for i in range(10):
    #     q.enqueue(i)
    #     print(q)
    #
    # print(q.isFull())
    # q.enqueue(10)
    # for _ in range(11):
    #     q.dequeue()
    #     print(q)
    # print(q.isEmpty())
    # print("#1")
    # q.dequeue()
    # print("#2")
    # q.dequeue()
    # print("#3")
    # q.dequeue()


    q = Deque(capacity=10)
    q.enqueue(1)
    print(q)
    q.enqueue(2)
    print(q)
    q.enqueue(3)
    print(q)
    q.addFirst(100)
    print(q)
    q.addFirst(101)
    print(q)
    q.addFirst(102)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.removeLast()
    print(q)
    q.removeLast()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    # q.dequeue()
    # print(q)

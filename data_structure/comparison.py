# -*- coding: utf-8 -*-
# author = "Louis"

from myarray_stack import Stack
from mylink_stack import linkStack
from mylink2_queue import queue
from myarray_queue import loopQueue, arrayQueue
from common import tools

@tools.count
def compare_stack(class_name, n):

    for i in range(n):
        class_name.push(i)
    for i in range(n):
        class_name.pop()


@tools.count
def compare_queue(class_name, n):
    for i in range(n):
        class_name.enqueue(i)
    for i in range(n):
        class_name.dequeue()


if __name__ == '__main__':
    arr_s = Stack()
    link_s = linkStack()
    compare_stack(arr_s, 1000)
    compare_stack(arr_s, 1000000)
    compare_stack(link_s, 1000)
    compare_stack(link_s, 1000000)

    arr_q = arrayQueue()
    loop_q = loopQueue(capacity=10)
    link_q = queue()
    for i in [1000, 10000, 100000]:
        print("n={}".format(i))
        compare_queue(link_q, i)
        compare_queue(loop_q, i)
        compare_queue(arr_q, i)
        print("--------\n")
# -*- coding: utf-8 -*-
# author = "Louis"
def count_iterator(start, end, order=1):
    """

    :param start:
    :param end:
    :param order:  1表示从小到大返回，0表示从大到小返回
    :return:
    """
    if end <= 0 and start > end:
        raise ValueError("end should be a value great than start")
    end = end - 1
    while end >= start:
        if order == 1:
            yield start
            start += 1
        else:
            yield end
            end -= 1
    return

class myArray:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.my_array = [None] * self.capacity

    def isEmpty(self):
        if self.size:
            return False
        return True

    def get(self, index):
        self.check_index_is_legal(index)
        return self.my_array[index]

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.size - 1)

    def add(self, index, value):
        self.check_index_is_legal(index)
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        for i in count_iterator(index, self.size, order=0):
            self.my_array[i + 1] = self.my_array[i]
        self.my_array[index] = value
        self.size += 1
        return value

    def addLast(self, value):
        return self.add(self.size, value)

    def addFirst(self, value):
        return self.add(0, value)

    def remove(self, index):
        self.check_index_is_legal(index)
        if self.size == 0:
            raise IndexError("Out of range")
        del_value = self.my_array[index]
        if self.size <= (self.capacity // 4) and (self.capacity // 4) != 0:
            self.resize(self.capacity // 2)

        # 删除指定元素后，将后面的元素往前面移动一格
        for i in count_iterator(index, self.size):
            self.my_array[i] = self.my_array[i + 1]

        self.size -= 1
        return del_value

    def removeLast(self):
        return self.remove(self.size - 1)

    def removeFirst(self):
        return self.remove(0)

    def set(self, index, value):
        self.check_index_is_legal(index)
        self.my_array[index] = value

    def check_index_is_legal(self, index):
        if index < 0 or index > self.size:
            raise IndexError("{} is out of list range. ".format(index))

    def resize(self, capacity):
        new_array = [None] * capacity
        new_array[:self.capacity] = self.my_array[:self.capacity]
        self.my_array = new_array
        self.capacity = capacity

    def __repr__(self):
        return "{} size={}, capacity={}".format(self.my_array[:self.size], self.size, self.capacity)


# Python中创建数组，默认是开辟多大空间？
# Python中创建数组 和 创建元组 默认空间的对比？

if __name__ == '__main__':
    my_array = myArray()
    # print(my_array)
    # my_array.add(0, 1)
    # print(my_array, my_array.size)
    # my_array.add(0, 2)
    # print(my_array, my_array.size)
    for i in range(10):
        my_array.addLast(i)
        print(my_array)
    my_array.addLast(11)
    for i in range(11):
        my_array.removeLast()
        print(my_array)
    # print(my_array.set(10, 100))
    # print(my_array, my_array.size)
    #
    # for i in reversed_count_iterator(5, 10):
    #     print(i)

# -*- coding: utf-8 -*-
# author = "Louis"


class DLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DLinkedNode(None, None)
        self.tail = DLinkedNode(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.moveNodeToFirst(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveNodeToFirst(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            if self.capacity > 0:
                self.capacity -= 1
            else:
                mv_node = self.removeLastNode()
                self.cache.pop(mv_node.key)
            self.addNodeToFirst(node)

    def moveNodeToFirst(self, node):

        self.removeNode(node)
        self.addNodeToFirst(node)

    def addNodeToFirst(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next
        # self.clearNode(node)

    def removeLastNode(self):
        node = self.tail.pre
        self.removeNode(node)
        return node
        # key = mv_node.key

        # mv_node.pre.next = self.tail
        # self.tail.pre = mv_node.pre
        # self.clearNode(mv_node)
        # self.cache.pop(key)

    # def clearNode(self, node):
    #     node.next = None
    #     node.pre = None

if __name__ == '__main__':
    c = LRUCache(2)
    c.put(1,1)
    print(c.get(1))
    c.put(2,2)
    print(c.get(2))
    print(c.get(1))
    c.put(3,3)
    print(c.get(2))
    print(c.get(1))
    print(c.get(3))
    print(c.get(4))


# import collections
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dic = collections.OrderedDict()

#     def get(self, key: int) -> int:
#         if key in self.dic:
#             value = self.dic.pop(key)
#             self.dic[key] = value
#             return value
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.pop(key)

#         else:
#             if self.capacity > 0:
#                 self.capacity -= 1
#             else:
#                 self.dic.popitem(False)
#         self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



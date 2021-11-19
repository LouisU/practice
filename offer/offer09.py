# -*- coding: utf-8 -*-
# author = "Louis"
class CQueue:

    def __init__(self):
        self.in_arr, self.out_arr = [], []

    def appendTail(self, value: int) -> None:
        self.in_arr.append(value)

    def deleteHead(self) -> int:
        if len(self.out_arr) != 0:
            return self.out_arr.pop()
        else:
            if len(self.in_arr) == 0: # in_arr out_arr都为空
                return -1
            else:                     # out_arr为空 in_arr不为空
                while len(self.in_arr):
                    val = self.in_arr.pop()
                    self.out_arr.append(val)
                return self.out_arr.pop()

if __name__ == '__main__':
    obj = CQueue()
    print(obj.deleteHead())
    obj.appendTail(5)
    obj.appendTail(2)
    print(obj.deleteHead())
    print(obj.deleteHead())
    print(1)


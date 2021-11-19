# -*- coding: utf-8 -*-
# author = "Louis"
from common.spend_time import count
@count
def LinearSearch(alist, target):
    # for index, num in enumerate(alist):
    #     if num == target:
    #        return index
    for i in range(len(alist)):
        if alist[i] == target:
            return i
    return False



if __name__ == '__main__':
    a = [1,12,34.1,'a',92,1,2,34,9]
    target ='a'
    print(LinearSearch(a, target))

# -*- coding: utf-8 -*-
# author = "Louis"
from collections.abc import Iterator
def mfunc(numbers, colors):
    count = len(numbers)
    color_to_number_dict = {}
    number_to_color_dict = {}
    for i in range(count):
        if numbers[i] not in number_to_color_dict:
            number_to_color_dict[numbers[i]] = [colors[i]]
        else:
            number_to_color_dict[numbers[i]].append(colors[i])

        if colors[i] not in color_to_number_dict:
            color_to_number_dict[colors[i]] = [numbers[i]]
        else:
            color_to_number_dict[colors[i]].append(numbers[i])
    max_card = 0

    for color, nums in color_to_number_dict.items():
        temp_count = 0
        for num in nums:
            temp_count += len(number_to_color_dict[num])
        max_card = max(temp_count, max_card)

    return max_card


class Company:

    def __init__(self, employee_list):
        self.employess_list = employee_list

    def __iter__(self):
        return MyIterator(self.employess_list)

    # def __getitem__(self, item):
    #     print("getitem")
    #     return self.employess_list[item]

    # def __next__(self):
    #     return self

class MyIterator(Iterator):
    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.index = -1
    def __next__(self):
        self.index += 1
        try:
            return self.iter_list[self.index]
        except IndexError:
            raise StopIteration

def decorator():
    def wrapper():
        pass
    return wrapper
def curve_pre():
    def curve():
        pass
    return curve

f = curve_pre()
f()
if __name__ == '__main__':
    n = ['1','4', '3', '4',  '5']
    c = ['r', 'y',  'b',  'b', 'r']
    mfunc(n, c)

    com = Company(employee_list=["a", 'b', 'c', 'd'])
    # print(com[0], com[1])
    for i in com:
        print(i)


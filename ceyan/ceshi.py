# -*- coding: utf-8 -*-
# author = "Louis"


class Spam:
    num = 0

    @staticmethod
    def count():
        Spam.num += 1

    def __init__(self):
        self.count()

class Sub(Spam):
    num = 0

class Other(Spam):
    num = 0

x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(),Other(),Other()
print(x.num, y1.num, y2.num)
print(Spam.num, Sub.num, Other.num)



if __name__ == '__main__':
    nums = [1,2,3,4,5]
    for data in nums:
        nums.remove(data)

    print(nums)



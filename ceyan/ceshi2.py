# -*- coding: utf-8 -*-
# author = "Louis"

num=0

def f():
    def inner():
        nonlocal num
        num = 2

    num =1
    print(num)
    inner()
    print(num)

if __name__ == '__main__':
    f()
    print(num)
    y = ("1"
        "22"
         "333"
    )
    print(y, len(y))

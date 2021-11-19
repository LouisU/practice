# coding=utf-8
# 1.4 查找最大或最小的 N 个元素
# 问题
# 怎样从一个集合中获得最大或者最小的 N 个元素列表？


# 解决方案一: 使用heapq模块中的函数nlargest()和nsmallest()
import heapq
numss = [1, 8, 2, 10, 23, 91, 39, -12]
print(heapq.nlargest(3, numss))
print(heapq.nsmallest(3, numss))

# heapq模块的函数nlargest()和nsmallest()接受一个关键字参数
# 用于更复杂的数据结构中
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

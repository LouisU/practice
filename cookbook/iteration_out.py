# 迭代对象如果使用for循环时，当迭代对象值取尽不会报错
print("-"*20)
iterms = [1,2,3]
it = iter(iterms)
for i in it:
    print(i)
    
# 当不使用for循环的时候，想自己遍历迭代对象中的元素，解决方案如下：
# 方案一： 可以捕捉StopIteration来实现自己遍历
print("-"*20)
it = iter(iterms)
def manual_iter(ite):
    try:
        while True:
            i = next(it) 
            print(i)
    except StopIteration:
        pass

manual_iter(it)

# 方案二:  可以返回一个指定值来标记可迭代对象的结尾，比如None.
print("-"*20)

it = iter(iterms)
def manual_iter(ite):
    while True:
        i = next(it, None) 
        if i == None:
            break
        print(i)
manual_iter(it)
print("-"*20)
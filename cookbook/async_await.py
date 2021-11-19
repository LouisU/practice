# -*- coding: utf-8 -*-
# author = "Louis"
import asyncio
import requests
import time

def function():
    return 1

def generator():
    yield 1

async def async_function():
    return 1

async def async_generator():
    yield 1


# import types
# print(type(function) is types.FunctionType)
# print(type(generator()) is types.GeneratorType)
# print(type(async_function()) is types.CoroutineType)
# print(type(async_generator()) is types.AsyncGeneratorType)

def run(coroutine):
    try:
        print(coroutine.send(None))
        print("#")
    except StopIteration as e:
        print("*")
        print(e)
        print(e.value)
        return e.value

async def await_coroutine():
    print("1")
    print(await async_function())
    print(2)

async def test2(i):
    r = await other_test(i)
    print(i,r)

async def other_test(i):
    r = requests.get(i)
    print(i)
    await asyncio.sleep(4)
    print(time.time()-start)
    return r

url = ["https://segmentfault.com/p/1210000013564725",
       "https://www.jianshu.com/p/83badc8028bd",
       "https://www.baidu.com/"]

loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(test2(i)) for i in url]
start = time.time()
loop.run_until_complete(asyncio.wait(task))
endtime = time.time()-start
print(endtime)
loop.close()

# 注意：
# 1. await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误。
# 2. await后面的对象需要是一个Awaitable，或者实现了相关的协议。


    # run(async_function())  # 为什么print()没有执行？
    # run(await_coroutine())



# -*- coding: utf-8 -*-
# author = "Louis"
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import time

def get_html(times):
    time.sleep(times)
    print("get sleeptime {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中, submit是立即返回的。
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# # done 方法用于判定某个任务是否完成
# print(task1.done())
# # cancel 方法取消正在待执行队列的任务，不会取消正在执行的任务。
# #     当executor.submit()提交任务后，会去看有没有空闲的worker
# #            有空闲的worker就马上执行任务 否则任务就进入待执行队列。
# print(task2.cancel())
# time.sleep(5)
# print(task1.done())
# # result 方法可以获取task的执行结果
# print(task1.result())


# 要获取已经成功的task的返回
urls = [3, 2, 4]
all_task = [executor.submit(get_html,(url)) for url in urls]
# as_completed方法 就是获取已经完成的task。  as_completed是谁先完成就先返回谁。
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} success".format(data))
wait(all_task)
print("Main")


# # 也可以通过executor获取已经完成的task.  map的返回顺序是和urls的顺序返回。
# for data in executor.map(get_html, urls):
#     print("get {} success".format(data))
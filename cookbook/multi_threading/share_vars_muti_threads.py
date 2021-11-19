# -*- coding: utf-8 -*-
# author = "Louis"

import threading
import time
from queue import Queue
# 多线程之间共享变量
# 不建议使用全局变量 数组 元组，线程不安全。
# 建议使用Queue， 应为Queue本身就是线程安全的数据类型。

# 多线程应用到爬虫案例：一个线程爬文章列表页，另一个线程爬取详情页。
# 当一个线程在爬文章列表页时，发出网络请求后，需要等待网络响应。这个时候，跳到爬取详情页的线程去执行。
# 这样，等待网络响应的时间就没有白白浪费。
def get_detail_html(queue):
    while True:
        # print("get detail html detail started.")
        print("find url: {}".format(queue.get()))
        # print("get detail html end.")


def get_url_list(queue):
    while True:
        print("get url list started.")
        for i in range(1000):
            queue.put("https://www.test.com/{}".format(i))
        print("get url list end.")


if __name__ == '__main__':
    url_list = Queue(maxsize=1000)
    thread1 = threading.Thread(target=get_detail_html, args=(url_list,))
    thread2 = threading.Thread(target=get_url_list, args=(url_list,))
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    # thread1.join()
    # thread2.join()

    print("last time: {}".format(time.time() - start_time))
    # 主线程 子线程 分清楚.
    #       当前执行__main__的线程称为主线程，
    #       在主线程中通过threading.Thread()开的是子线程
    # 默认情况下，当主线程执行完 没有退出 等到子线程都执行完了，才退出主线程
    #
    # 那么，当主线程执行完了，不管子线程有没有执行完，主线程义无反顾的退出。这个怎么设置？
    #       将子线程设置成守护进程。这样只要主线程结束，设置为守护进程的子进程将直接退出(子线程会被kill掉)。
    #       thread_object.setDeamon(True)
    #
    # 那么，如果先让主线程阻塞，等子线程执行完了，再继续执行主线程。这个怎么设置？
    #       thread_object.join().当主线程遇到这个语句时，就会等thread_object这个子线程执行完，在继续。
    #

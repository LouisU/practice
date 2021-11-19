# -*- coding: utf-8 -*-
# author = "Louis"

import threading
import time


# 用threading.Thread 开子进程。将自定的方法变成子进程里面执行的方法。

# 多线程应用到爬虫案例：一个线程爬文章列表页，另一个线程爬取详情页。
# 当一个线程在爬文章列表页时，发出网络请求后，需要等待网络响应。这个时候，跳到爬取详情页的线程去执行。
# 这样，等待网络响应的时间就没有白白浪费。
def get_detail_html(url):
    print("get detail html detail started.")
    time.sleep(2)
    print("get detail html end.")


def get_url_list(url):
    print("get url list started.")
    time.sleep(4)
    print("get url list end.")


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_url_list, args=("",))
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

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

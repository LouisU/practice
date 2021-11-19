# -*- coding: utf-8 -*-
# author = "Louis"

import threading
import time
# 用类的方式来实现多线程。 这种方式比较实用。

# 多线程应用到爬虫案例：一个线程爬文章列表页，另一个线程爬取详情页。
# 当一个线程在爬文章列表页时，发出网络请求后，需要等待网络响应。这个时候，跳到爬取详情页的线程去执行。
# 这样，等待网络响应的时间就没有白白浪费。
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print("get detail html detail started.")
        time.sleep(2)
        print("get detail html end.")


class GetUrlList(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print("get url list started.")
        time.sleep(4)
        print("get url list end.")


if __name__ == '__main__':
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetUrlList("get_url_list")
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    # thread1.join()
    # thread2.join()

    print("last time: {}".format(time.time() - start_time))

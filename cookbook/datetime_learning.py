# coding=utf-8
from datetime import datetime

from datetime import timedelta
import spend_time


print("-"*20)

text = "2021-03-12"
# 时间转换


@spend_time.count
def transfer_string_to_date_by_strptime(s_date):
    y = datetime.strptime(text, "%Y-%m-%d")
    return y


print(transfer_string_to_date_by_strptime(text))

print("-"*20)

# datetime.strptime是一个纯python实现的方法，性能并不高。
# 如果代码中有大量的将字符串日期转换为datetime.datetime, 且已经知道字符串日期的格式，可以自己实现转换。
# 由时间执行时间来看，自己定义的时间转换方法比strptime 要快将近160倍


@spend_time.count
def transfer_string_to_date(s_date):
    s_year, s_month, s_day = s_date.split('-')
    return datetime(int(s_year), int(s_month), int(s_day))


print(transfer_string_to_date(text))

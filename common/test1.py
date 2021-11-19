# -*- coding: utf-8 -*-
# author = "Louis"

def mfunc(arr, n):
    res = []
    sum = 0
    last_index = -1
    for i in range(n):
        min_value, mid_value = min(arr[i]), sorted(arr[i])[1]
        min_value_index, mid_value_index = arr[i].index(min_value), arr[i].index(mid_value)
        if last_index == -1:
            last_index = min_value_index
            value = min_value
        else:
            if last_index == min_value_index:
                value = mid_value
                last_index = mid_value_index
            else:
                value = min_value
                last_index = min_value_index

        sum += value
    res.append(sum)
    sum = 0
    last_index = -1
    for i in range(n):
        min_value, mid_value = min(arr[i]), sorted(arr[i])[1]
        min_value_index, mid_value_index = arr[i].index(min_value), arr[i].index(mid_value)
        if last_index == -1:
            last_index = mid_value_index
            value = mid_value
        else:
            if last_index == min_value_index:
                value = mid_value
                last_index = mid_value_index
            else:
                value = min_value
                last_index = min_value_index

        sum += value
    res.append(sum)
    sum = 0
    last_index = -1
    for i in range(n):
        min_value, mid_value = min(arr[i]), sorted(arr[i])[1]
        min_value_index, mid_value_index = arr[i].index(min_value), arr[i].index(mid_value)
        if last_index == -1:
            value = max(arr[i])
            last_index = arr[i].index(value)
        else:
            if last_index == min_value_index:
                value = mid_value
                last_index = mid_value_index
            else:
                value = min_value
                last_index = min_value_index

        sum += value
    res.append(sum)
    return min(res)




if __name__ == "__main__":
    # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # arr = []
    # for i in range(n):
    #     line = sys.stdin.readline().strip()
    #     values = list(map(int, line.split()))
    #     arr.append(arr)
    arr = [
        [15, 8, 17],
        [12, 20, 9],
        [11,7,5]
    ]
    n=3
    print(mfunc(arr, n))
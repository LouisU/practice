# -*- coding: utf-8 -*-
# author = "Louis"

class BinarySearch:

    def search(self, arr, target):
        return self.searchR(arr, 0, len(arr)-1, target)

    def search2(self, arr, target):
        l = 0
        r = len(arr) - 1
        # 循环不变量: 在arr[l:r)中查找target
        while l < r:
            mid = int((r + l + 1) / 2)
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def searchR(self, arr, l, r, target):
        if l >= r:
            return -1
        mid = int((l + r) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.searchR(arr, l, mid - 1, target)
        else:
            return self.searchR(arr, mid + 1, r, target)


# 查找有序数组中大于target的最小值
class Solution:

    def upper(self, arr, target):
        index2 = self.search2(arr, target)
        # print("the first value greater then target({}) is : arr[{}]".format(
        #     target, index2))
        # index = self.search(arr, 0, len(arr), target)
        # print("the first value greater then target({}) is : arr[{}]".format(
        #     target, index))
        return index2

    def search(self, arr, l, r, target):
        if l >= r:
            return l
        # 循环不变量 保持在[l:r]中查找
        while r > l:
            mid = int((r + l) / 2)
            if target <= arr[mid]:
                return self.search(arr, l, mid, target)
            else:
                return self.search(arr, mid + 1, r, target)

    def search2(self, arr, target):
        l, r, = 0, len(arr)
        # 循环不变量 保持在[l,r)中查找
        #    当target <= arr[mid]时 说明[mid,r)中的所有元素都大于target. 那么r = mid, 保持在[l,r)中查找
        #    当target > arr[mid]时 说明[l,mid+1)中的所有元素都小于target.那么l = mid + 1  保持在[l,r)中查找
        #    最后退出while循环的两种情况：
        #         1. 在target>arr[mid]的情况下 执行了l=mid+1后，导致r=l, 退出while循环。
        #                   说明[0,l)中的元素都<=target,[l,r]都大于target, 而l = r,
        #                   说明在arr数组中r这个位置指向的值就大于target的，arr数组r之前的所有元素的值都小于target
        #                   特例： target>arr[len(arr)-1] 的时候，说明arr所有的元素都小于target, 那么l=r=len(arr)
        #         2. 在target<=arr[mid]的情况下 执行了r=mid后，导致r=l, 退出while循环。
        #                   说明[0,l)中的元素都<=target,[l,r]都大于target
        #                   说明在arr数组中r这个位置指向的值就大于target的，arr数组r之前的所有元素的值都小于target.
        #                   特例： target<=arr[0]的时候 说明arr所有元素都大于target, 那么l=r=0
        while r > l:
            mid = int((r + l) / 2)
            if arr[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l

    def upper_ceil(self, arr, target):
        u = self.upper(arr, target)
        if u - 1 >= 0 and arr[u - 1] == target:
            return u - 1
        return u

    def search3(self, arr, l, r, target):

        while l < r:
            mid = int((r + l) / 2)
            if arr[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

    def lower_ceil(self, arr, target):
        # 当target存在arr,且有多个target值，那么返回等于target值的最小index
        # 当target不存在arr中，那么返回最小的大于target值的index
        return self.search3(arr, 0, len(arr), target)

    # 查找小于target的最大值。
    # 循环不变量： 搜索范围arr[l,r]
    # 循环不变量的初始值 l=-1, r=len(arr) -1.
    #       因为 [1,20,33,99]当target=0时，整个数组都没有小于target的值，所以应该返回-1.
    #                       当target=100时，整个数组的元素都小于target的值，那么数组最右边的值就是小于target的最大值。
    def lower(self, arr, target):
        l = -1
        r = len(arr) - 1
        while l < r:
            # mid = int((l + r) / 2)
            # mid是取下整数  l =0, r=1时，mid=0,
            # 有arr[mid]<target，l=mid=0, r=1. 进入死循环。 由于int()取下整数导致死循环。
            mid = int((l + 1 + r) / 2)   # mid取上整数
            if arr[mid] == target:
                # 当中间值等于target时
                # 说明mid左边都小于等于target, mid右边都大于等于target
                # 我们要取小于target的最大值。就去看左边
                # 因为等于target的元素没有保留在[l,r]区间中的的必要，所有r = mid-1
                r = mid - 1
            elif arr[mid] > target:
                # 当中间的值大于target时
                # 说明mid的右边都大于target, 说明左边可能还有大于target的数。
                # 那么我们看mid左边, 去看是否有小于target的数。
                # 因为大于target的元素已经没有保留在[l,r]区间中的必要，所有r=mid - 1
                r = mid - 1
            else:
                # 当中间值小于target时。
                # 说明mid左边都小于target，而右边可能还有比target小的数，
                # 那么我们看mid右边，去看是否还有小于target的数。
                # 因为小于target的数 还是有必要保留在[l,r]区间内的，所以l=mid
                l = mid
        return l


    def lower_floor(self, arr, target):
        # 当target在arr中存在，且有多个元素=target, 那么返回=target的且最左边的index.
        # 当target不存在，那么返回<target的最大值。
        #    即 lower_floor 返回<= target的最小索引
        l = -1
        r = len(arr) - 1
        while l < r:
            # mid = int((l + r) / 2)
            # mid是取下整数  l =0, r=1时，mid=0,
            # 有arr[mid]<target，l=mid=0, r=1. 进入死循环。 由于int()取下整数导致死循环。
            mid = int((l + 1 + r) / 2)  # mid取上整数
            if arr[mid] == target:
                # 当中间值等于target时
                # 说明mid左边都小于等于target, mid右边都大于等于target
                # 我们要取小于target的最大值。就去看左边
                # 因为等于target的元素没有保留在[l,r]区间中的的必要，所有r = mid-1
                r = mid - 1
            elif arr[mid] > target:
                # 当中间的值大于target时
                # 说明mid的右边都大于target, 说明左边可能还有大于target的数。
                # 那么我们看mid左边, 去看是否有小于target的数。
                # 因为大于target的元素已经没有保留在[l,r]区间中的必要，所有r=mid - 1
                r = mid - 1
            else:
                # 当中间值小于target时。
                # 说明mid左边都小于target，而右边可能还有比target小的数，
                # 那么我们看mid右边，去看是否还有小于target的数。
                # 因为小于target的数 还是有必要保留在[l,r]区间内的，所以l=mid
                l = mid
        if l+1 <= len(arr)-1 and arr[l+1] == target:
            return l + 1
        return l

    def upper_floor(self, arr, target):
        # 当target在arr中存在，且有多个元素=target, 那么返回=target的且最右边的index.
        # 当target不存在，那么返回<target的最大值。
        #      即 upper_floor返回<=target的最大索引
        l = -1
        r = len(arr) - 1
        while l < r:
            # mid = int((l + r) / 2)
            # mid是取下整数  l =0, r=1时，mid=0,
            # 有arr[mid]<target，l=mid=0, r=1. 进入死循环。 由于int()取下整数导致死循环。
            mid = int((l + 1 + r) / 2)  # mid取上整数
            if arr[mid] == target:
                # --> 当arr[mid]=target那么我们认为该mid可能是<=target的最大值，
                # -->   但是mid右边还可能存在于target相等的元素。
                # -->   既然arr[mid]=target， 那么认为mid左边都小于或者等于target,即使=target也都不是最大的=target的索引
                # -->   所以我们取mid右边，且保留mid在[l,r]区间中
                l = mid    # --> 取mid右侧找
            elif arr[mid] > target:
                # 当中间的值大于target时
                # 说明mid的右边都大于target, 说明左边可能还有大于target的数。
                # 那么我们看mid左边, 去看是否有小于target的数。
                # 因为大于target的元素已经没有保留在[l,r]区间中的必要，所有r=mid - 1
                r = mid -1
            else:
                # 当中间值小于target时。
                # 说明mid左边都小于target，而右边可能还有比target小的数，
                # 那么我们看mid右边，去看是否还有小于target的数。
                # 因为小于target的数 还是有必要保留在[l,r]区间内的，所以l=mid
                l = mid
        return l


if __name__ == '__main__':
    a = [1, 1, 3, 3, 5, 5]
    print(BinarySearch().search(a, 5))  # 查找值是否存在
    for i in range(9):
        print('-----{}'.format(i))
        print(Solution().lower_floor(a, i))
        print(Solution().upper_floor(a, i))

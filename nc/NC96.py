# -*- coding: utf-8 -*-
# author = "Louis"


class Solution:
    def isPail(self, head):
        v_head = head
        arr = []
        while v_head is not None:
            arr.append(v_head.val)
            v_head = v_head.next

        arr_len = len(arr)
        m_arr = arr_len // 2
        for i in range(m_arr):
            if arr[i] != arr[arr_len - i - 1]:
                return False
        return True


if __name__ == '__main__':
    pass

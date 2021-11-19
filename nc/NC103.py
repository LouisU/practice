# -*- coding: utf-8 -*-
# author = "Louis"
# 题目描述
# 写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
# 示例1
# 输入
# 复制
# "abcd"
# 返回值
# 复制
# "dcba"

class Solution:
    def solve(self, str):

        l = len(str)
        h_l = int(l / 2)

        new_s = ""
        for i in range(h_l, l):
            if i != l - i - 1:
                new_s = "{}{}{}".format(str[i], new_s, str[l - i - 1])
            else:
                new_s = "{}{}".format(str[i], new_s)
        return new_s

    # def solve(self, str):
    #     return str[::-1]

if __name__ == '__main__':
    s1 = 'abcdef'
    s2 = 'abcdefg'
    print(Solution().solve(s1))
    print(Solution().solve(s2))
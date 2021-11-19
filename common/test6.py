# -*- coding: utf-8 -*-
# author = "Louis"
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
#
# 示例 1：
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
# 示例 2：
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
# 提示：
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

class Solution:

    # s1 的排列组合取其中一种
    # 判断 s2 中是否有该组合
    def func(self, s1, s2):
        self.loop = len(s1)
        for zu_he in self.zuhe(s1):
            if zu_he in s2:
                return True
            else:
                continue
        return False

    def zuhe(self,s1):
        for i in range(self.loop):
            s1 = "{}{}".format(s1[i:], s1[:i])
            yield s1

if __name__ == '__main__':

    s1 = "ab"
    s2 = "eidbaooo"
    # s2 = "eidboaoo"
    print(Solution().func(s1, s2))

    # s1 = "acb"
    # s2 = "eidbacooo"
    # # s2 = "eidboaoo"
    # print(Solution().func(s1, s2))
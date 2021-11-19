# coding=utf-8
# 给定一个字符串 s 和一个字符串 t ，
# 计算在 s 的子序列中 t 出现的个数。
# 
# 字符串的一个 子序列 是指，
# 通过删除一些（也可以不删除）
# 字符且不干扰剩余字符相对位置所组成的新字符串。
# （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
# 
# 题目数据保证答案符合 32 位带符号整数范围。
# 
#  
# 
# 示例 1：
# 
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 示例 2：
# 
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
#  
# 
# 提示：
# 
# 0 <= s.length, t.length <= 1000
# s 和 t 由英文字母组成
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/distinct-subsequences
# # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路：取t的第一个字符，判断是否在s字符串中。
#          如果不在，认为s不存在t这样的子序列
#          如果存在，获取last_index = s.index(t[1]).
#                 取t的第二个字符, 判断是否存在于s[last_index+1]
#      直到t的最后一个字符 认为s中存在一个 子序列。

# 思路：取t的第一个字符x，判断是否在s字符串中。
#          如果不在，认为s不存在t这样的子序列
#          如果存在，找到字符x存在多少个，有多少个可能是t子序列的开头。
#                 判断是否获取last_index = s.index(t[1]).
#                 取t的第二个字符, 判断是否存在于s[last_index+1]
#      直到t的最后一个字符 认为s中存在一个 子序列

# 思路：取t得前后两个字符判断是否存在子序列的可能，存在几种可能。
#           每种可能里面，截取上面两个字符中间的内容
#               取t得前后第二个字符,判断是否存在子序列的可能，存在

class Solution:
    def numDistinct(self, s, t):
        for i in range(len(t)):
            if t[i] in s:
                s.index(t[i])
            else:
                pass


class Solution:
    def numDistinct(self, s, t):
        len_t = len(t) if len(t) % 2 == 0 else len(t) + 1
        for i in range(len_t):
            # if i == len_t - 1 - i
            start, end = t[i] + t[len_t - 1 - i]
            if start in s and end in s and s.index(end) > s.index(start):
                pass


class Solution:
    def letter_position_list(self, st, letter):
        position_list = []
        for index, value in enumerate(st):
            if value == letter:
                position_list.append(index)
        return position_list

    def numDistinct(self, s, t):
        for i in t:
            if i not in s:
                return False

        count = 0
        letters_position_list = []
        for i in t:
            letters_position_list.append(self.letter_position_list)

        # 从每个列表中挑出一个值，逐渐递增，才成立。

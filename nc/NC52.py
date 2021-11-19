# -*- coding: utf-8 -*-
# author = "Louis"
# 题目描述
# 给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
# 括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
class Solution:
    def isValid(self , s ):
        # write code here
        left_stack = []
        for i in s:
            if i == "[" or i == "(" or i =='{':
                left_stack.append(i)
            else:
                if len(left_stack)==0:
                    return False
                j = left_stack.pop()
                if j == "[" and i == "]":
                    continue
                elif j == "{" and i == "}":
                    continue
                elif j == "(" and i == ")":
                    continue
                else:
                    return False
        if len(left_stack) == 0:
            return True
        return False
if __name__ == '__main__':
    pass

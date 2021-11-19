# -*- coding: utf-8 -*-
# author = "Louis"
# 题目描述
# 计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。
#
# 输入描述:
# 输入一行，代表要计算的字符串，非空，长度小于5000。
#
# 输出描述:
# 输出一个整数，表示输入字符串最后一个单词的长度。
#
# 示例1
# 输入 hello nowcoder
# 输出 8
# 说明
# 最后一个单词为nowcoder，长度为8

if __name__ == '__main__':
    str_line = "asdj"
    if len(str_line) >= 5000 or len(str_line) == 0:
        raise Exception("illegal input")
    str_line = str_line.strip()
    i = -1
    str_len = len(str_line)
    while -i <= str_len and not str_line[i].isalpha():
        i -= 1
    count = 0
    while -i <= str_len and str_line[i].isalpha():
        count += 1
        i -= 1

    print(count)



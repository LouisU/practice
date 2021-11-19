# -*- coding: utf-8 -*-
# author = "Louis"

# 题目描述
# 写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写，字符串长度小于500。
#
# 输入描述:
# 第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字母。
#
# 输出描述:
# 输出输入字符串中含有该字符的个数。
#
# 示例1
# 输入
# ABCabc
# A
# 输出
# 2

if __name__ == '__main__':
    # str_line = "nhrwlbcc8m7c5hih9mhalw98k0322wf2jjm47kk3ntm9snfrflzzundn7d608usy049asxalzjk7izj6amcqhr8uubc04g52mcjboj2fmge2l6iarizfu4yve5o4i3srf5zgqbg82ckcotdeqp760mc9gzei5dzk5gj9x9yj05o3hle0ii64krkkp5i7blh7nbu3gu5vgi2scyn4yqx3z4vcjbyzhnqkh887izotjkg2l0mit0k14vyn39"
    # letter = 't'
    #
    # str_line = str_line.upper()
    # letter = letter.upper()
    # count = 0
    # for l in str_line:
    #     if l == letter:
    #         count += 1
    # print(count)


    str_line = "nhrwlbcc8m7c5hih9mhalw98k0322wf2jjm47kk3ntm9snfrflzzundn7d608usy049asxalzjk7izj6amcqhr8uubc04g52mcjboj2fmge2l6iarizfu4yve5o4i3srf5zgqbg82ckcotdeqp760mc9gzei5dzk5gj9x9yj05o3hle0ii64krkkp5i7blh7nbu3gu5vgi2scyn4yqx3z4vcjbyzhnqkh887izotjkg2l0mit0k14vyn39"
    letter = 't'

    str_line = str_line.upper()
    letter = letter.upper()


    print(len(str_line.split(letter)) -1 )

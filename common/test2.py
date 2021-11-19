# -*- coding: utf-8 -*-
# author = "Louis"

def mfunc(t, p):
    t_len = len(t)
    p_len = len(p)

    for i in range(t_len):
        if p[0] == t[i]:
            if p == t[i:i + p_len]:
                return i + 1
    return "No"

if __name__ == '__main__':
    t = 'AVERDXIVYERDIAN'
    p = 'RDXI'
    print(mfunc(t, p))

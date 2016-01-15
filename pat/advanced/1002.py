#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
这个题，我一开始想到的方法通过数组来解决。**哈希的思想**
通过数组的下标和多项式指数相同的项对应, 然后就可以方便的进行对应项的加法。
不过，数组的方法比较浪费空间，数组的大小总是需要1000 或 1001


想想，用链表或许也能解决这个问题。而且可以不浪费空间。

想回来，那还是用数组好了，数据的元素为元组，一个元组代表多项式的一项，
只是逻辑比原来的复杂点。貌似时间复杂度也增大了。


**知道没中算法中包含的基本算法，并且掌握基本算法的基本知识**
**慎重考虑边界情况**
**float() 转换后会带小数点**
**如果是整数，就不要输出小数点了**  题目的最后一句话已经说不要考虑这种情况..
**保留一位小数**
"""


def input_parse():
    polynomial = [0] * 1001
    whole_str = raw_input()
    whole_str_list = whole_str.split(' ')
    num_term = int(whole_str_list[0])
    for i in range(0, num_term):
        exponent = int(whole_str_list[2*i+1])
        polynomial[exponent] = float(whole_str_list[2*i+2])
    return polynomial


def solution():
    output = []
    polynomial_1 = input_parse()
    polynomial_2 = input_parse()
    for i in range(0, 1001):
        r = polynomial_1[i] + polynomial_2[i]
        if r != 0:
            output.append((i, r))
    output = sorted(output, key=lambda m: m[0], reverse=True)
    length = len(output)
    if length == 0:
        print length
        return 0
    print length,
    for i in range(0, length):
        o = float(output[i][1])
        if i != (length - 1):
            print output[i][0], "%.1f" % o,
        else:
            print output[i][0], "%.1f" % o


if __name__ == '__main__':
    solution()

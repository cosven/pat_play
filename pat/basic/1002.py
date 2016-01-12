#! /usr/bin/env python
# -*- coding: utf-8 -*-

chinese_pinyin = [
    'ling',
    'yi',
    'er',
    'san',
    'si',
    'wu',
    'liu',
    'qi',
    'ba',
    'jiu'
]

num = raw_input()

digit_sum = 0
for c in num:
    digit_sum += int(c)

sum_pinyin = []
for i in range(len(str(digit_sum)), 0, -1):
    c = digit_sum / 10**(i-1)
    digit_sum -= c * 10**(i-1)
    sum_pinyin.append(chinese_pinyin[c])

print ' '.join(sum_pinyin)

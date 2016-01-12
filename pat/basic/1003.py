#! /usr/bin/evn python
# -*- coding: utf-8 -*-

import re


def judge():
    pattern_1 = re.compile(r'^(A)*P(A)+T(A)*$')
    pattern_2 = re.compile(r'P(A)+T')
    s = raw_input()
    match = pattern_1.match(s)
    if match is not None:
        m_m = pattern_2.search(s)
        m_s = pattern_2.split(s)
        if len(m_s[0]) * (len(m_m.group(0)) - 2) == len(m_s[-1]):
            print 'YES'
            return 0
    print 'NO'
    return 0


times = int(raw_input())

while times > 0:
    judge()
    times -= 1

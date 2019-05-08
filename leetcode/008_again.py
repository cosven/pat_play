"""
008.py 修正

008.py 的方法中， int+int 可能会越界。
"""


INT_MAX = 2 ** 31 - 1
INT_MIN = - 2 ** 31

REMAINDER = INT_MAX % 10


class Solution:
    def myAtoi(self, s):
        if not s:
            return 0

        # remove leading whitespace
        i = 0
        for i_, c in enumerate(s):
            if c != ' ':
                i = i_
                break

        # check if is positive or negative
        positive = True
        num = 0
        if s[i] == '+':
            pass
        elif s[i] == '-':
            positive = False
        elif s[i].isdigit():
            num += int(s[i])
        else:
            return 0

        for c in s[i+1:]:
            if not c.isdigit():
                break
            # check if overflow
            if num > INT_MAX // 10 or \
               (num == INT_MAX//10 and int(c) >= REMAINDER + 1):
                return INT_MAX if positive else INT_MIN
            else:
                num = num * 10 + int(c)
        return num if positive else -num

#! /usr/bin/env python
# -*- coding: utf-8 -*-

nums_str = raw_input()
nums = nums_str.split(' ')
num1, num2 = int(nums[0]), int(nums[1])

result = num1 + num2


def represent(num):
    flag = '' if num >= 0 else '-'
    num = abs(num)
    tmp_string = ''
    divisor = 10**3
    while True:
        reminder = num % divisor
        quotient = num / divisor
        num = quotient
        if quotient > 0:
            reminder = (3-len(str(reminder))) * '0' + str(reminder)
            tmp_string = ',' + str(reminder) + tmp_string
        else:
            tmp_string = str(reminder) + tmp_string
            break
    return flag + tmp_string

print represent(result)

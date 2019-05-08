INT_MAX = 2 ** 31 - 1
INT_MIN = - 2 ** 31


class Solution:
    def myAtoi(self, s: str) -> int:
        # if s is empty, return 0
        if not s:
            return 0

        # valid char found sentinel
        found = False

        result_s = ''
        positive = True

        # for every char in s
        for c in s:
            # if we meet a valid char, save it in our char_list
            #  set a flag if it is the first valid char
            if c.isdigit():
                found = True
                result_s += c
            else:
                if found is False:
                    if c == ' ':
                        continue
                    elif c == '+':
                        found = True
                        continue
                    elif c == '-':
                        found = True
                        positive = not positive
                    else:
                        break
                else:
                    break

        # return 0 if our char list is empty
        if not result_s:
            return 0

        num = 0
        for i, c in enumerate(result_s[::-1]):
            if positive:
                if (num + int(c) * (10 ** i)) >= INT_MAX:
                    return INT_MAX
                else:
                    num += int(c) * (10 ** i)
            else:
                if (num + int(c) * (10 ** i)) <= INT_MIN:
                    return INT_MIN
                else:
                    num -= int(c) * (10 ** i)
        return num

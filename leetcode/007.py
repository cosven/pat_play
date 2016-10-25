import os


class Solution(object):
    def reverse(self, x):
        pass

    def reverse__first_version(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        flag = -1 if x < 0 else 1
        x = flag * x
        return flag * int(str(x)[::-1])

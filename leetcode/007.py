class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        if x > ((1 << 31) - 1):
            return 0
        flag = -1 if x < 0 else 1
        x = flag * x
        while ((x / 10) > 0) and (x % 10 == 0):
            x = x / 10 
        if int(str(x)[::-1]) > ((1 << 31) - 1):
            return 0
        r_x = flag * int(str(x)[::-1]) 
        return r_x

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

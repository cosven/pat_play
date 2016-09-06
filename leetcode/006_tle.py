class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if num_rows <= 1 or len(s) <= num_rows:
            return s
        height = num_rows
        width = length / (2*height - 2)
        width_remainder = length % (2*height - 2) - height
        if width_remainder < 0:
            width_remainder = 0
        r_s = ''
        for i in range(0, height):
            for j in range(0, width * (height-1) + width_remainder + 1):
                quotients = j / (height-1)
                remainders = j % (height-1)
                if remainders == 0:
                    index = (2*height-2) * quotients + i
                    r_s += s[index] if index < len(s) else ''
                else:
                    if (i+j) % (height-1) == 0:
                        index = quotients*(2*height-2) + height + remainders - 1
                        r_s += s[index] if index < len(s) else ''
        return r_s

    def test(self):
        assert self.convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
        assert self.convert('abcdefghijk', 4) == 'agbfhceikdj'
        assert self.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'


if __name__ == '__main__':
    s = Solution()
    s.test()

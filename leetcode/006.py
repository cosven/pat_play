class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        length = len(s)
        if num_rows <= 1 or len(s) <= num_rows:
            return s
        r_s_l = [''] * num_rows
        for i in xrange(length):
            q = i / (2 * (num_rows - 1))
            r = i % (2 * (num_rows - 1))

            if r <= num_rows - 1:
                x = r
            else:
                x = 2 * (num_rows - 1) - r

            if q < 0:
                y = 0
            else:
                y = q * (num_rows - 1)
                if r <= num_rows - 1:
                    y += 0
                else:
                    y += r - (num_rows - 1)
            
            r_s_l[x] += s[i]

        return ''.join(r_s_l)

    def test(self):
        assert self.convert('abcdefghijk', 4) == 'agbfhceikdj'
        assert self.convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
        assert self.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'


if __name__ == '__main__':
    s = Solution()
    s.test()

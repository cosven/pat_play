class Solution(object):
    def longestPalindrome(self, s):
        max_len = 0
        max_str = ''

        if len(s) <= 2:
            return s

        for i, ch in enumerate(s):
            delta = 1
            count = 0
            # center is ch
            while (i - delta) >= 0 and (i + delta) < len(s):
                if s[i-delta] != s[i+delta]:
                    break
                count += 1
                delta += 1
            if count * 2 + 1 > max_len:
                max_len = count * 2 + 1
                max_str = s[i-count:i+1+count]

            # center is ch right
            delta = 0.5
            count = 0
            j = i + 0.5
            while (j - delta) >= 0 and (j + delta) < len(s):
                if s[int(j - delta)] != s[int(j + delta)]:
                    break
                count += 1
                delta += 1

            if count * 2 > max_len:
                max_len = count * 2
                max_str = s[i-count+1:i+count+1]
        return max_str

    def test(self):
        assert self.longestPalindrome('a') == 'a'
        assert self.longestPalindrome('abcba') == 'abcba'
        assert self.longestPalindrome('eabcbae') == 'eabcbae'
        assert self.longestPalindrome('abba') == 'abba'
        assert self.longestPalindrome('abbc') == 'bb'
        assert self.longestPalindrome('dbabba') == 'abba'
        assert self.longestPalindrome('decababace') == 'ecababace'
        assert self.longestPalindrome('decababaceehgagbgnag') == 'ecababace'


if __name__ == '__main__':
    s = Solution()
    s.test()

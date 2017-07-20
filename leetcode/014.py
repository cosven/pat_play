class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        min_s = strs[0]
        min_length = len(min_s)

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
                min_s = s

        if not min_length:
            return ''

        for i in range(0, min_length):
            c = min_s[i]
            for s in strs:
                if s[i] != c:
                    return s[:i]

        return min_s

    def test(self):
        assert self.longestCommonPrefix([]) == ''
        assert self.longestCommonPrefix(['ab', 'aa']) == 'a'


if __name__ == '__main__':
    s = Solution()
    s.test()

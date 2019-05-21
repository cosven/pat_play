def gen_lps(s):
    """
    lps - longest prefix suffix

    >>> gen_lps('abcabd')
    [-1, 0, 0, 1, 2, 0]
    >>> gen_lps('121212')
    [-1, 0, 1, 2, 3, 4]
    >>> gen_lps('1111')
    [-1, 1, 2, 3]
    >>> gen_lps('abababb')
    """
    lps = [0] * len(s)
    length = 0
    i = 1
    while i < len(s):
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        >>> Solution().strStr('abc', 'ab')
        0
        >>> Solution().strStr('aaaaaaaaaaaaaaaaab', 'aaac')
        -1
        >>> Solution().strStr('hello', 'll')
        2
        >>> Solution().strStr("mississippi", "issip")
        4
        """
        if needle == '':
            return 0

        lps = gen_lps(needle)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j >= len(needle):
                    return i - j
                continue
            if j >= 1:
                j = lps[j-1]
            else:
                i += 1
        return -1

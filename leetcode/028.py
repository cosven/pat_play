class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == '':
            return 0

        index = -1
        for i, c in enumerate(haystack):
            if len(needle) + i > len(haystack):
                break
            if needle[0] == c:
                ok = True
                for j in range(1, len(needle)):
                    if needle[j] != haystack[i+j]:
                        ok = False
                if ok:
                    index = i
                    break
        return index

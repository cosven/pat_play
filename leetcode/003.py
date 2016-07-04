class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        length_list = []    # only for debug

        tmp_str = ''
        tmp_length = 0
        for i, c in enumerate(s):   # O(n)
            index = tmp_str.find(c)  # O(n), can be O(1) by using dict
            if tmp_str == '' or index == -1:
                tmp_length += 1
            else:
                tmp_str = tmp_str[index+1:]
                tmp_length = tmp_length - (index + 1) + 1
            tmp_str += c
            length_list.append(tmp_length)

            if tmp_length > max_length:
                max_length = tmp_length
        return max_length

    def test(self):
        assert self.lengthOfLongestSubstring('') == 0
        assert self.lengthOfLongestSubstring('abcabcbb') == 3
        assert self.lengthOfLongestSubstring('bbbbb') == 1
        assert self.lengthOfLongestSubstring('abcde') == 5
        assert self.lengthOfLongestSubstring('pwwkew') == 3


if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring('abcdefgb')
    s.test()

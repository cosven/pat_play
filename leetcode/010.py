# -*- coding: utf-8 -*-


class Solution(object):
    def is_equal(self, c1, c2):
        if c1 == c2:
            return True
        if '.' in (c1, c2):
            return True
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True

        if not s or not p:
            return False

        p_index = 0
        last_s_c = s[0]
        for s_c in s:
            if p_index >= len(p):
                if p[p_index-1] == '*' and last_s_c == s_c:
                    continue
                else:
                    break

            if self.is_equal(s_c, p[p_index]):
                last_s_c = s_c
                p_index += 1
                continue
            else:
                if p[p_index] == '*' and last_s_c == s_c:
                    continue
                else:
                    # 如果 p 的当前字母与 s_c 不符合，检测它的下一个字符是否为 *
                    if p_index + 1 < len(p):
                        if p[p_index+1] == '*':
                            p_index += 2
                    else:
                        break
        else:
            return True
        return False

    def test(self):
        assert self.isMatch("aa", "a") is False
        assert self.isMatch("aa", "aa") is True
        assert self.isMatch("aaa", "aa") is False
        assert self.isMatch("aa", "a*") is True
        assert self.isMatch("aa", ".*") is True
        assert self.isMatch("ab", ".*") is True
        assert self.isMatch("aab", "c*a*b") is True


if __name__ == '__main__':
    s = Solution()
    s.test()

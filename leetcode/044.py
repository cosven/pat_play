"""
此解法会超时
"""


class Solution(object):
    def isMatch(self, s, p):
        for index, c in enumerate(p):
            if c == '*':
                tmp_p = p[index + 1:]
                i = 0

                for _i, _c in enumerate(tmp_p):
                    if _c != '*':
                        i = _i
                        break
                    i += 1
                else:
                    if i == 0:  # * is the last char
                        return True
                return self.starMatch(s[index:], tmp_p[i:])

            if len(s) < index + 1:
                return False
            if c in ('?', s[index]):
                continue
            return False
        if len(s) != len(p):
            return False
        return True

    def starMatch(self, s, p):
        if not p or s == p:
            return True
        if not s:
            return False

        next_star_i = None
        for i, c in enumerate(p):
            if c == '*':
                next_star_i = i
                break

        if next_star_i is not None:
            part = p[:next_star_i]
        else:
            part = p
        for i in range(0, len(s) - len(part) + 1):
            _s = s[i: i + len(part)]
            if self._equal(_s, part) and \
                    self.isMatch(s[i + len(part):], p[len(part):]):
                return True
        return False

    def _equal(self, s1, s2):
        for a, b in zip(s1, s2):
            if '?' in (a, b):
                continue
            if a == b:
                continue
            return False
        return True

    def test_all(self):
        assert self.starMatch('ab', 'a*b') is True
        assert self.isMatch('', '*') is True
        assert self.isMatch('a', 'a**') is True
        assert self.isMatch('a', 'a*?') is False
        assert self.isMatch('a', 'a*a') is False
        assert self.isMatch('ab', 'a**c') is False
        assert self.isMatch('', '?') is False
        assert self.isMatch('', '?*') is False
        assert self.isMatch('aa', 'a') is False
        assert self.isMatch('aa', 'aa') is True
        assert self.isMatch('aaa', 'aa') is False
        assert self.isMatch('aa', '*') is True
        assert self.isMatch('aa', 'a*') is True
        assert self.isMatch('ab', '?*') is True
        assert self.isMatch('aab', 'a*a*b') is True
        assert self.isMatch("zacabz", "*a?b*") is False
        assert self.starMatch("xxde", "de") is True
        assert self.isMatch("abefcdgiescdfimde", "ab*cd?i*de") is True
        assert self.isMatch("aaba", "?***") is True

    def test_new(self):
        s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
        p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
        print(self.isMatch(s, p))


if __name__ == '__main__':
    s = Solution()
    s.test_all()
    # s.test_new()

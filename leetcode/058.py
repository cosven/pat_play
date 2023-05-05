class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        last = 0
        i = 0
        while True:
            try:
                if s[i] != ' ':
                    length += 1
                else:
                    if length != 0:
                        last = length
                    length = 0
                i += 1
            except IndexError:
                break
        if length != 0:
            return length
        return last


if __name__ == '__main__':
    tests = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ]
    s = Solution()
    for t, expect in tests:
        result = s.lengthOfLastWord(t)
        assert result == expect, f'{result}, {expect}'

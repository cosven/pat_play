class Solution:

    def sumSubseqWidths(self, l):
        return self.do(l) % (10**9 + 7)

    def do(self, l):
        if len(l) <= 1:
            return 0

        l = sorted(l)
        added = 0
        length = len(l)
        for i in range(1, length):
            added += ((1 << (length - 1 - i)) * (l[length-1] - l[i-1])) % (10**9 + 7)
        return self.do(l[:-1]) + added


def test_():
    assert Solution().sumSubseqWidths([2]) == 0
    print(Solution().sumSubseqWidths([2, 1]))
    assert Solution().sumSubseqWidths([2, 1]) == 1
    assert Solution().sumSubseqWidths([2, 1, 3]) == 6
    assert Solution().sumSubseqWidths([3,7,2,3]) == 35


if __name__ == '__main__':
    test_()

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        plus1 = True
        while (l > 0 and plus1):
            num = digits[l-1]
            if num == 9:
                num = 0
                plus1 = True
            else:
                num += 1
                plus1 = False
            digits[l-1] = num
            l -= 1
        if plus1:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    tests = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
    ]
    for t, expect in tests:
        result = s.plusOne(t)
        assert result == expect, f'{result}, {expect}'

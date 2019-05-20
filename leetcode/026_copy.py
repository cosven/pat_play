class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for num in nums:
            if i == 0 or num > nums[i-1]:
                nums[i] = num
                i += 1
        return i


def test_():
    s = Solution()
    assert s.removeDuplicates([1, 1, 2]) == 2
    assert s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5


if __name__ == '__main__':
    test_()

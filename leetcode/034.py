#! /usr/bin/env python


class Solution(object):
    def searchRange(self, nums, target):
        self.target = target
        return self.find_target(0, len(nums) - 1, nums)

    def find_target(self, start, end, nums):
        target = self.target
        if not nums:
            return [-1, -1]

        if start == end:
            if nums[start] == target:
                return [start, end]
            else:
                return [-1, -1]

        if end - start == 1:
            if nums[start] == nums[end] == target:
                return [start, end]
            if target == nums[end]:
                return [end, end]
            if target == nums[start]:
                return [start, start]
            return [-1, -1]

        index = (start + end) / 2
        if nums[index] > target:
            return self.find_target(start, index, nums)
        elif nums[index] == target:
            start = self.find_start(start, index, nums)
            end = self.find_end(index, end, nums)
            if start is end is None:
                return [-1, -1]
            elif None in (start, end):
                return [start or end, start or end]
            return [start, end]
        else:
            return self.find_target(index, end, nums)

    def find_start(self, start, index, nums):
        if nums[start] == self.target:
            return start
        if index - start == 1:
            return index
        tmp = (start + index)/2
        if nums[tmp] < self.target:
            return self.find_start(tmp, index, nums)
        return self.find_start(start, tmp, nums)

    def find_end(self, index, end, nums):
        if nums[end] == self.target:
            return end
        if end - index == 1:
            return index
        tmp = (end + index)/2
        if nums[tmp] > self.target:
            return self.find_end(index, tmp, nums)
        return self.find_end(tmp, end, nums)

    def test_find_x(self):
        self.target = 2
        assert self.find_start(0, 3, [0, 1, 2, 2]) == 2

        self.target = 1
        assert self.find_end(0, 3, [1, 1, 2, 3]) == 1

    def test_(self):
        assert self.searchRange([1], 0) == [-1, -1]
        assert self.searchRange([1], 1) == [0, 0]
        assert self.searchRange([7, 8, 8, 10], 8) == [1, 2]
        assert self.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]


if __name__ == '__main__':
    s = Solution()
    s.test_find_x()
    s.test_()

"""
思路
----------
使用二分查找


二分查找的实现
-------------------

- [ ] 二分查找的边界条件

"""


def bin_search(nums, target, start, end):
    if start == end:
        return start

    length = end - start
    middle = length // 2 + start
    if target == nums[middle]:
        return middle
    elif target < nums[middle]:
        if middle == end:
            return middle
        return bin_search(nums, target, start, middle)
    else:
        if middle == start:
            return end
        return bin_search(nums, target, middle, end)


def bin_search_v2(nums, target, start, end):
    while start <= end:
        mid = (end + start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        return bin_search(nums, target, 0, len(nums))


def test_():
    assert bin_search([1], 2, 0, 1) == 1
    assert bin_search([0, 1], 2, 0, 2) == 2
    assert bin_search([0, 1, 2], 2, 0, 3) == 2


if __name__ == '__main__':
    test_()

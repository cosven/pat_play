"""
Find the kth largest element in an unsorted array. Note that it is the kth
 largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


"""

   6
 5   4
3 2 1

  5
 3 1
2
"""


def swap_if_need(nums, i, j):
    if nums[i] > nums[j]:
        return i
    nums[i], nums[j] = nums[j], nums[i]
    return j


def adjust_heap(nums, end):
    # move the root to the proper position
    last_i = i = 0
    while i < end:
        l, r = 2*i+1, 2*i+2
        # print(last_i, i, l, r, end)
        if l >= end:
            break
        if r >= end:
            i = swap_if_need(nums, i, l)
        else:
            if nums[l] >= nums[r]:
                t = l
            else:
                t = r
            i = swap_if_need(nums, i, t)
        if i == last_i:
            break
        last_i = i


class Solution:
    def findKthLargest(self, nums, k):
        for i in range(0, len(nums)):
            p_i = (i+1) // 2 - 1
            while nums[i] >= nums[p_i]:
                if i == 0:
                    break
                nums[p_i], nums[i] = nums[i], nums[p_i]
                i = p_i
                p_i = (i+1) // 2 - 1

        count = 0
        while count < k - 1:
            end = len(nums) - 1 - count
            nums[0], nums[end] = nums[end], nums[0]
            adjust_heap(nums, end)
            count += 1
        return nums[0]


def test_solution():
    assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5
    assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4) ==  4
    assert Solution().findKthLargest([5,2,4,1,3,6,0], 4) == 3
    assert Solution().findKthLargest([0,1,2,3,5,5,4,3,2,1,0,-1,-2], 4) == 3

if __name__ == '__main__':
    test_solution()

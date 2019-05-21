class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # the index of the element that used to swap
        end = len(nums) - 1
        for i, num in enumerate(nums):
            # until the val element is the last
            if i >= end:
                break

            if num == val:
                while end > i:
                    if nums[end] != val:
                        # replace each val element with the last element
                        nums[end], nums[i] = nums[i], nums[end]
                        break
                    end -= 1

        while end >= 0:
            if nums[end] == val:
                end -= 1
            else:
                break

        return end + 1

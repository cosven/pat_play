class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        self.nums1 = nums1
        self.nums2 = nums2

        self.l1 = l1
        self.l2 = l2

        if l1 == 0:
            return self._get_median(nums2)
        if l2 == 0:
            return self._get_median(nums1)

        new_nums = self._merge(nums1, nums2)
        print new_nums
        return self._get_median(new_nums)

    def _merge(self, nums1, nums2):
        new_nums = []
        i = 0
        j = 0
        return self.__merge(i, j, new_nums)

    def __merge(self, index1, index2, new_nums):
        if self.nums1[index1] > self.nums2[index2]:
            new_nums.append(self.nums2[index2])
            if index2 >= self.l2 - 1:
                new_nums.extend(self.nums1[index1:])
                return new_nums
            else:
                return self.__merge(index1, index2+1, new_nums)
        else:
            new_nums.append(self.nums1[index1])
            if index1 >= self.l1 - 1:
                new_nums.extend(self.nums2[index2:])
                return new_nums
            else:
                return self.__merge(index1 + 1, index2, new_nums)

    def _get_median(self, nums):
        l = len(nums)
        if l % 2 == 0:
            n_index = l / 2
            p_index = l / 2 - 1
            return (nums[p_index] + nums[n_index]) * 1.0 / 2
        else:
            return nums[l / 2]

    def test(self):
        assert self._get_median([1, 2, 3, 4]) == 2.5
        assert self._get_median([1, 2, 3]) == 2
        assert self.findMedianSortedArrays([1, 3], [2]) == 2.0
        assert self.findMedianSortedArrays([1, 3], [2, 4]) == 2.5
        assert self.findMedianSortedArrays([1, 2], [3, 4]) == 2.5


if __name__ == '__main__':
    s = Solution()
    s.test()

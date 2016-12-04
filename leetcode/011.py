class Solution(object):

    def maxArea(self, height):
        if len(height) == 2:
            return min(height)

        lenght = len(height)

        f_index = 0
        b_index = lenght - 1

        max_v = 0
        h_list = height

        while (f_index < b_index):
            value = self.cal_value(f_index, b_index, h_list)
            # print f_index, b_index, value, h_list
            if value >= max_v:
                max_v = value
            if h_list[f_index] < h_list[b_index]:
                f_index += 1
            else:
                b_index -= 1
            # print 'tmp: ', max_v
        return max_v

    def cal_value(self, start, end, h_list):
        return (end - start) * min([h_list[start], h_list[end]])

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height)

        lenght = len(height)

        f_index = 0
        b_index = lenght - 1

        first = height[0]
        last = height[lenght - 1]

        max_v = (lenght - 1) * min([first, last])
        return self.cal_max_l(f_index, b_index, height, max_v)

    def cal_max_l(self, start, end, h_list, max_v):
        if (start + 1) == end:
            return max_v
        start += 1
        h_list.pop(0)
        lenght = len(h_list)
        value = (lenght - 1) * min([h_list[0], h_list[-1]])
        if value >= max_v:
            print 'cal_max_l: ', value
            return self.cal_max_r(start, end, h_list, value)
        else:
            return self.cal_max_l(start, end, h_list, max_v)

    def cal_max_r(self, start, end, h_list, max_v):
        if (end - 1) == start:
            return max_v
        end -= 1
        h_list.pop(-1)
        lenght = len(h_list)
        value = (lenght - 1) * min([h_list[0], h_list[-1]])
        if value >= max_v:
            print 'cal_max_r: ', value
            return self.cal_max_l(start, end, h_list, value)
        else:
            return self.cal_max_r(start, end, h_list, max_v)

    def test(self):
        max_v = self.maxArea([3, 1, 2, 3])
        print 'max_v: ', max_v
        assert max_v == 9

    def test2(self):
        max_v = self.maxArea([3, 1, 2, 3])
        assert max_v == 9

        print '-------------------------------'

        max_v = self.maxArea([1, 2, 4, 3])
        assert max_v == 4

        print '-------------------------------'

        max_v = self.maxArea([2, 3, 4, 5, 18, 17, 6])
        assert max_v == 17


if __name__ == '__main__':
    s = Solution()
    # s.test()
    # s.test2()

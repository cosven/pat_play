class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        1. 有没有数学方法可以实现？
        2. 计算对应旋转之后对应的位置
        """
        n = len(matrix)
        if n == 0:
            return matrix
        if n % 2 != 0:
            mid = n // 2 + 1
        else:
            mid = n // 2
        for s in range(0, mid):
            i = 0
            while i < (n - 1 - 2 * s):
                l = (matrix[s][s + i],
                     matrix[s + i][n - 1 - s],
                     matrix[n - 1 - s][n - 1 - s - i],
                     matrix[n - 1 - s - i][s])
                matrix[s][s + i] = l[-1]
                matrix[s + i][n - 1 - s] = l[0]
                matrix[n - 1 - s][n - 1 - s - i] = l[1]
                matrix[n - 1 - s - i][s] = l[2]
                i += 1
        print(matrix)


if __name__ == '__main__':
     s = Solution().rotate([
        [1,2,3],
        [4,5,6],
        [7,8,9]
     ])
     s = Solution().rotate(
         [
             [ 5, 1, 9,11],
             [ 2, 4, 8,10],
             [13, 3, 6, 7],
             [15,14,12,16]
         ]
     )

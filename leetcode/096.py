class Solution:
    cache = {1: 1, 0:1}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cache:
            return self.cache[n]
        sum = 0
        ncopy = n - 1
        while ncopy >= 0:
            sum += self.numTrees(ncopy) * self.numTrees(n - 1 - ncopy)
            ncopy -= 1
        self.cache[n] = sum
        return sum


if __name__ == '__main__':
    print(Solution().numTrees(100))

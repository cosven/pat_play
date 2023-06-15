from collections import defaultdict


class Solution:
    def findJudge(self, n, trust):
        d_in = defaultdict(int)
        d_out = defaultdict(int)
        for x, y in trust:
            d_in[y] += 1
            d_out[x] += 1

        for i in range(1, n+1):
            if d_in[i] == n-1 and d_out[i] == 0:
                return i
        return -1

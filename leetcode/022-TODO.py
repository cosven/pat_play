class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return 1



if __name__ == '__main__':
    result = [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    s = Solution()
    ps = s.generateParenthesis(3)
    for p in ps:
        assert p in s
    for p in s:
        assert p in ps

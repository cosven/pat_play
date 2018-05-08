class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        m = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}
        l = []
        for digit in digits:
            if not l:
                for c in m[digit]:
                    l.append(c)
            else:
                l2 = []
                for e in l:
                    for c in m[digit]:
                        l2.append(e + c)
                l = l2

        return l


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        # 考点一
        stack = []
        pair = {'(': ')',
                '{': '}',
                '[': ']'}
        for c in s:
            if c in pair:
                stack.append(c)
            else:
                try:
                    top = stack.pop()
                # 考点三
                except IndexError:
                    return False
                else:
                    if pair[top] == c:
                        continue
                    else:
                        return False

        # 考点二
        return not bool(stack)


if __name__ == '__main__':
    assert Solution().isValid('()')
    assert Solution().isValid('()[]{}')
    assert not Solution().isValid('(]')
    assert not Solution().isValid('([)]')
    assert not Solution().isValid('(')

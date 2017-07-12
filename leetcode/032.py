class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        longest = 0

        tmp_longest = 0
        tmp_increment = 0
        last_char = ''
        middle_c_num = None
        for c in s:
            if c == '(':
                stack.append(c)
                if middle_c_num is not None:
                    middle_c_num += 1
            else:
                if len(stack) > 0:

                    if middle_c_num is not None:
                        middle_c_num -= 1
                    else:
                        middle_c_num = 0

                    stack.pop(-1)
                    tmp_increment += 1

                    if len(stack) == 0:
                        tmp_longest += tmp_increment
                        tmp_increment = 0
                    if last_char == '(':
                        if middle_c_num > 0:
                            tmp_increment = 1

                else:  # invalid
                    longest = longest if longest > tmp_longest else tmp_longest
                    tmp_increment = tmp_longest = 0
            last_char = c
        else:
            print longest, tmp_longest, tmp_increment
            if len(stack) > 0:
                tmp_longest = tmp_longest if tmp_longest > tmp_increment else tmp_increment
            else:
                tmp_longest += tmp_increment
            longest = longest if longest > tmp_longest else tmp_longest
        return longest * 2

    def test(self):
        assert self.longestValidParentheses('(()') == 2
        assert self.longestValidParentheses(')()())') == 4
        assert self.longestValidParentheses('()(()') == 2
        assert self.longestValidParentheses('(()(((()') == 2
        assert self.longestValidParentheses('()(())') == 6
        assert self.longestValidParentheses('(()()') == 4
        assert self.longestValidParentheses(')(((((()())()()))()(()))(') == 22
        assert self.longestValidParentheses(')()(((())))(') == 10
        assert self.longestValidParentheses('(()()(())((') == 8


if __name__ == '__main__':
    s = Solution()
    s.test()

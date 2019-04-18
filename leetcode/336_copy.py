def is_palindrome(word):
    i = 0
    while i < len(word) // 2:
        if word[i] != word[len(word) - 1 - i]:
            return False
        i += 1
    return True


class Solution:
    def palindromePairs(self, words):
        mapping = {}
        for i, word in enumerate(words):
            mapping[word] = i

        pairs = set()

        if '' in mapping:
            for i, word in enumerate(words):
                if word == '':
                    continue
                if is_palindrome(word):
                    pairs.add((i, mapping['']))
                    pairs.add((mapping[''], i))

        for i, word in enumerate(words):
            word_r = word[::-1]
            i_r = mapping.get(word_r)
            if i_r is not None and i != i_r:
                pairs.add((i, i_r))
                pairs.add((i_r, i))
            for j in range(1, len(word)):
                if is_palindrome(word[:j]):
                    word_sub_r = word[j:][::-1]
                    i_r = mapping.get(word_sub_r)
                    if i_r is not None and i_r != i:
                        pairs.add((i_r, i))

                if is_palindrome(word[j:]):
                    word_sub_r = word[:j][::-1]
                    i_r = mapping.get(word_sub_r)
                    if i_r is not None and i_r != i:
                        pairs.add((i, i_r))
        return list(pairs)


def test_():
    assert is_palindrome('ab') is False
    l = ["a","b","c","ab","ac","aa"]
    l = ["ab","ba","abc","cba"]
    print(set(Solution().palindromePairs(l)))


if __name__ == '__main__':
    test_()

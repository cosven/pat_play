class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_len = len(word1)
        word2_len = len(word2)
        if word2_len > word1_len:
            self.longer_word = word2
            self.shorted_word = word1
        else:
            self.longer_word = word1
            self.shorted_word = word2

        self.char_map = {}
        for index, c in enumerate(self.longer_word):
            if c in self.char_map:
                self.char_map[c].append(index)

        # {'char': (index, [(target_index, matched_num)])}
        index = 0
        while(index < len(self.shorted_word)):
            c = self.shorted_word[index]
            if c in self.char_map:
                pass

    def find_next_unmatch_index(self, index):
        pass

    def test(self):
        assert all([
            self.minDistance('hello', 'hallo') == 1,
            self.minDistance('hell', 'hello') == 1,
            self.minDistance('hll', 'hello') == 2,
        ])


if __name__ == '__main__':
    s = Solution()
    s.test()

class Solution:
    def __init__(self):
        # each cell is (x, y) tuple
        self.used_cells = []

    def exist(self, board, word):
        assert word
        if not board:
            return False

        self.word = word
        self.board = board

        self.max_x = len(board) - 1
        self.max_y = len(board[0]) - 1

        first_c = word[0]

        # find all possible start cells
        possible_start_cells = []
        for _x in range(0, self.max_x + 1):
            for _y in range(0, self.max_y + 1):
                if board[_x][_y] == first_c:
                    possible_start_cells.append((_x, _y))

        # possible start cells maybe []
        for cell in possible_start_cells:
            if len(word) == 1:
                return True
            self.used_cells = []
            self.path = []
            _x, _y = cell
            tmp_ok = self.depth_first(_x, _y, 0, word[0])
            if tmp_ok is True:
                return True
            else:
                continue
        return False

    def depth_first(self, x, y, word_index, path):
        self.used_cells.append((x, y))
        word = self.word
        board = self.board

        for index in range(word_index + 1, len(word)):
            c = word[index]
            cells = self.get_adjacent_cells(x, y)

            for cell in cells:
                if cell in self.used_cells:
                    continue
                _x, _y = cell
                # found c
                if board[_x][_y] == c:
                    if index == len(word) - 1:  # all match
                        return True
                    # try to find next c
                    # print('find next c', _x, _y, c, path+c)
                    ok = self.depth_first(_x, _y, index, path+c)
                    if ok is True:
                        return True
                    continue
            else:
                # print('exit sub', x, y, c, path, self.used_cells)
                self.used_cells.pop(-1)
                return False
        else:
            # print('exit', x, y, word_index)
            return False

    def get_adjacent_cells(self, x, y):
        x_ok_list = [x]
        y_ok_list = [y]
        if x - 1 >= 0:
            x_ok_list.append(x - 1)
        if x + 1 <= self.max_x:
            x_ok_list.append(x + 1)

        if y - 1 >= 0:
            y_ok_list.append(y - 1)
        if y + 1 <= self.max_y:
            y_ok_list.append(y + 1)

        adjacent_cells = []
        for _x in x_ok_list:
            for _y in y_ok_list:
                if (_x == x) ^ (_y == y):
                    adjacent_cells.append((_x, _y))
        return adjacent_cells

    def _test_basic(self):
        print('test basic...')
        (100, 200) in [(100, 200)]
        print('test basic success')

    def _test_cases(self):
        print('test cases...')
        print('-------------------')
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = 'ABCCED'
        assert self.exist(board, word) is True
        word = 'SEE'
        assert self.exist(board, word) is True
        word = 'ABCB'
        assert self.exist(board, word) is False
        print('test cases success')

        print('-------------------')
        board = [['a']]
        word = 'b'
        assert self.exist(board, word) is False

        print('-------------------')
        board = [['a']]
        word = 'a'
        assert self.exist(board, word) is True

        print('-------------------')
        board = [['A', 'B', 'C', 'E'],
                 ['S', 'F', 'E', 'S'],
                 ['A', 'D', 'E', 'E']]
        word = 'ABCESEEEFS'
        assert self.exist(board, word) is True

    def test_all(self):
        print('test all...')
        self._test_basic()
        self._test_cases()
        print('test success...')


if __name__ == '__main__':
    s = Solution()
    s.test_all()

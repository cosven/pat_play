from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_kv_list = [{} for _ in range(9)] # {number: y}
        y_kv_list = [{} for _ in range(9)]  # {number: x}

        for x, line in enumerate(board):
            for y, c in enumerate(line):
                if c == '.':
                    continue

                block_x_start = (x // 3) * 3
                block_x_end = (x // 3) * 3 + 3
                block_y_start = (y // 3) * 3
                block_y_end = (y // 3) * 3 + 3

                z = 0
                while z < 3:
                    yy = x_kv_list[block_x_start + z].get(c)
                    if (yy is not None and block_y_start <= yy < block_y_end):
                        return False

                    xx = y_kv_list[block_y_start + z].get(c)
                    if (xx is not None and block_x_start <= xx < block_x_end):
                        return False

                    z += 1

                if c in x_kv_list[x]:
                    return False
                else:
                    x_kv_list[x][c] = y

                if c in y_kv_list[y]:
                    return False
                else:
                    y_kv_list[y][c] = x
        return True


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    #board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    for line in board:
        print(line)
    print(Solution().isValidSudoku(board))

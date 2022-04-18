# 36. Valid Sudoku
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        rows = [[0] * 9 for _ in range(9)]
        # check columns
        cols = [[0] * 9 for _ in range(9)]
        # check 3 * 3 grids       
        grids = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    idx = int(board[i][j]) - 1
                    rows[i][idx] += 1
                    cols[j][idx] += 1
                    grids[i // 3][j // 3][idx] += 1

                    if rows[i][idx] > 1 or cols[j][idx] > 1 or grids[i // 3][j // 3][idx] > 1:
                        return False

        return True

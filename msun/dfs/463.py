# 463. Island Perimeter
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        row, col = len(grid), len(grid[0])
        
        # dfs
        def dfs(r, c):
            if  not (0 <= r < row and 0 <= c < col):
                return 1

            if grid[r][c] == 0:
                return 1

            if grid[r][c] == 2:
                return 0

            grid[r][c] = 2
            return dfs(r, c - 1) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r + 1, c)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    ans = dfs(r, c)

        return ans
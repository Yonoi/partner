# 695. Max Area of Islands
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        # dfs
        def dfs(i, j):
            if  not (0 <= i < m and 0 <= j < n):
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 2
                ans = 1
                return  1 + dfs(i, j - 1) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i + 1, j)
            else:
                return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(dfs(i, j), ans)
        return ans
    
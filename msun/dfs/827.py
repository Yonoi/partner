from typing import List
from copy import deepcopy
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        # dfs
        def dfs(tmp, i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if tmp[i][j] == 1:
                tmp[i][j] == 2
                return 1 + dfs(tmp, i - 1, j) + dfs(tmp, i + 1, j) + dfs(tmp, i, j - 1) + dfs(tmp, i, j + 1)
            else:
                return 0
        for r in range(m):
            for c in range(n):
                tmp = deepcopy(grid)
                if tmp[r][c] == 0:
                    tmp[r][c] = 1
                for i in range(n):
                    for j in range(m):
                        if tmp[i][j] == 1:
                            ans = max(dfs(tmp, i, j), ans)
        return ans
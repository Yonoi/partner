class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n
        for j in range(n):
            col = j  
            for row in grid:
                dir = row[col]
                col += dir  
                if col < 0 or col == n or row[col] != dir:  
                    break
            else:  
                ans[j] = col
        return ans

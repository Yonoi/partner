class Solution:
    def numEnclaves(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        query = []
        for i in range(n):
            if grid[0][i]:
                visited[0][i] = True
                query.append((0, i))
        
            if grid[m-1][i]:
                visited[m-1][i] = True
                query.append((m - 1, i))

        for j in range(1, m-1):
            if grid[j][0]:
                visited[j][0] = True
                query.append((j, 0))
            
            if grid[j][n-1]:
                visited[j][n-1] = True
                query.append((j, n - 1))
            
        while len(query) != 0:
            i, j = query.pop(0)
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[i][j] and not visited[x][y]:
                    visited[x][y] = True
                    query.append((x, y))
        return sum(grid[i][j] and not visited[i][j] for i in range(1, m - 1) for j in range(1, n - 1))

if __name__ == "__main__":
    s = Solution()
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    print(s.numEnclaves(grid))
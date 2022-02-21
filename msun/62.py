class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m - 1, n - 1
        if m == 0 or n == 0:
            return 1
        all_moves = m + n
        all_paths = all_moves
        maximum = max(m, n)
        for move in range(all_moves - 1, maximum, -1):
            print(move)
            all_paths *= move
        
        for move in range(all_moves - maximum, 1, -1):
            print(move)
            all_paths /= move
        
        return int(all_paths)
         



if __name__ == "__main__":
    s = Solution()
    m, n = 2, 57
    print(s.uniquePaths(m, n))
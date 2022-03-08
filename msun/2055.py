class Solution:
    def platesBetweenCandles(self, s: str, queries: list) -> list:
        n = len(s)
        pre_sum, tmp = [0] * n, 0

        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                tmp += 1
            else:
                l = i
            pre_sum[i] = tmp
            left[i] = l
        
        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r
        
        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = pre_sum[y] - pre_sum[x]
        
        return ans

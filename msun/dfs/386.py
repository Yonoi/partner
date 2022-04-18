# 386. Lexicographical Numbers
from collections import deque
from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # if n < 10:
        #     return list(range(1, n+1))
        # ans = []
        # num = 1
        # for i in range(n):
        #     ans.append(num)
        #     if num * 10 <= n:
        #         num *= 10
        #     else:
        #         while num % 10 == 9 or num + 1 > n:
        #             num //= 10
        #         num += 1   
        # return ans
        ans = []

        def dfs(num):
            if num > n:
                return
            ans.append(num)
            for i in range(10):
                dfs(num * 10 + i)
        
        for i in range(1, 10):
            dfs(i)
        
        return ans
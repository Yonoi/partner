from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        pre_sum = [0] * (cols + 2)
        for row in range(rows): 

            new_row = [int(cur) + int(pre) if cur == "1" else 0 for cur, pre in zip([0] + matrix[row] + [0], pre_sum)]
            stack = [0]
            for i in range(1, cols + 2):
                while new_row[i] < new_row[stack[-1]]:
                    cur_height = new_row[stack.pop()]
                    cur_weight = i - stack[-1] - 1
                    ans = max(ans, cur_height * cur_weight)
                stack.append(i)
            print(ans)
            pre_sum = new_row
        
        return ans
            
from typing import List
class Solution:
    def trap(self, height:List[int]) -> int:
        ans = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()

                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - height[cur]
                ans += (i - stack[-1] - 1) * h
            stack.append(i)
        return ans
            
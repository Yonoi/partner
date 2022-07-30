"739. Daily Temperatures"
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n

        for i in range(n):
            while len(stack) > 0:
                if temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    ans[idx] = i - idx
                else:
                    break
            stack.append(i)
        return ans

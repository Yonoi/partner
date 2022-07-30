"503. Next Greater Element II"
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n

        for i in range(2 * n):
            curr = i % n
            while len(stack) > 0:
                if nums[curr] > nums[stack[-1]]:
                    idx = stack.pop()
                    ans[curr] = nums[curr]
                else:
                    break
            stack.append(curr)
        return ans
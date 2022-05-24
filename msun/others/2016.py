class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans, premin = -1, nums[0]
        for j in range(1, n):
            if nums[j] > premin:
                ans = max(ans, nums[j] - premin)
            else:
                premin = nums[j]
        
        return ans
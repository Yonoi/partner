"674. Longest Continuous Increasing Subsequence"
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_length = 0

        for i in range(n-2):
            if nums[i] < nums[i+1]:
                max_length += 1
            else:
                max_length = 0
            ans = max(ans, max_length)

        return ans
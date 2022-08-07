"673. Number of Longest Increasing Subsequence"
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        longest = 0

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    dp[i] = max(dp[i], dp[j] + 1)
            
            longest = max(longest, dp[i])
        ans = 0
        for i in range(n):
            if dp[i] == longest:
                ans += count[i]

        return ans

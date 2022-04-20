# 300. Longest Increasing Subsequence
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        dp.append(1)
        
        for i in range(1, n):
            try:
                dp.append(max([each for idx, each in enumerate(dp) if nums[idx] < nums[i]]) + 1)
            except ValueError:
                dp.append(1)
        return max(dp)
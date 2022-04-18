# 16. 3Sum Closest
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans, maximum = 0, 10e4
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                summary = nums[i] + nums[left] + nums[right]
                if summary == target:
                    return target
                if abs(summary - target) < abs(maximum-target):
                    maximum = summary
                if summary > target:
                    right_tmp = right - 1
                    while left < right_tmp and nums[right_tmp] == nums[right]:
                        right_tmp -= 1
                    right = right_tmp
                else:
                    left_tmp = left + 1
                    while left_tmp < right and nums[left_tmp] == nums[left]:
                        left_tmp += 1
                    left = left_tmp
        return maximum
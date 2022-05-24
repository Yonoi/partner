class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        return f"{nums[0]}/({'/'.join(nums[1:])})" if len(nums) > 2 else  f"{'/'.join(nums)}"
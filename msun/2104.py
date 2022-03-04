class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        k, length = 1, len(nums)
        res = 0
        init = [[max(nums[i:i+2]), min(nums[i:i+2])] for i in range(length - 1)]
        tmp = init
        while len(tmp) > 0:
            res += sum([each[0] - each[1] for each in tmp])
            length = len(tmp)
            tmp = [[max(tmp[i][0], tmp[i+1][0]), min(tmp[i][1], tmp[i+1][1])] for i in range(length - 1)]    

        return res

        
        
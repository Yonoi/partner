class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int: 
        n = len(nums)

        bitwise_or = lambda x, y: x | y 
        maximum = reduce(bitwise_or, nums)
        ans = 0
        for i in range(1, 2 ** n):
            binary = '{}'.format(bin(i)[2:]).reverse()
            print(binary)
            if reduce(bitwise_or, [nums[idx] for idx, b in enumerate(binary) if b == '1']) == maximum:
                ans += 1
        return ans
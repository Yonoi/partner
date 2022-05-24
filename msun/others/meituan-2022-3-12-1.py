class Solution:
    def judge(self, nums: int) -> bool:
        if (nums % 11 == 0):
            return True
        summary = 0
        while nums:
            if (nums % 10 == 1):
                summary += 1
            nums /= 10
        return summary >= 2
if __name__ == '__main__':
    s = Solution()
    nums = 10
    print(s.judge(nums))
        
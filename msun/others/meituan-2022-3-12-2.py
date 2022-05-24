class Solution:
    def num_of_seq(self, nums: list) -> int:
        n = len(nums)
        pre_sum = [(nums[0] + 2) % 3] * n
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + (nums[i] + 2) % 3
        print(pre_sum)
        ans = 0
        for i in range(1, n):
            for j in range(i):
                if (pre_sum[i] - pre_sum[j]) % 2 == 0:
                    ans += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1, -1, 1, 1]
    print(s.num_of_seq(nums))
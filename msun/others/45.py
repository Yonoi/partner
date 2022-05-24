class Solution:
    def jump(self, nums) -> int:
        ans = 0
        idx = 0
        n = len(nums)

        while idx + nums[idx] < n - 1:
            new_idx = 0
            tmp_max = -1
            for j in range(1, nums[idx] + 1):
                if j + nums[j] > tmp_max:
                    new_idx = j
                    tmp_max = j + nums[j]
            idx += new_idx
            ans += 1
        return ans + 1

if __name__ == '__main__':
    s = Solution()
    nums = [2,3,0,1,4]
    print(s.jump(nums))
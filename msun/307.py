import math
class NumArray:

    def __init__(self, nums: list):
        self._nums = nums

        self._block_len = math.ceil(math.sqrt(len(nums)))
        self._tmp_arr_len  = math.ceil(len(self._nums) / self._block_len)
        self._tmp_sum = [0] * self._tmp_arr_len
        for i in range(self._tmp_arr_len):
            self._tmp_sum[i] = sum(self._nums[i * self._block_len : (i + 1) * self._block_len])
        print(self._tmp_sum)
    
    def update(self, index: int, val: int) -> None:
        idx = index // self._block_len
        self._tmp_sum[idx] =  self._tmp_sum[idx] - self._nums[index] + val
        self._nums[index] = val
        print(self._tmp_sum)

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        if left == right:
            res = self._nums[left]
        
        else:
            right += 1
            left_idx = left // self._block_len
            right_idx = right // self._block_len

            left_idx_reminder = left % self._block_len
            right_idx_reminder = right % self._block_len

            if left_idx < right_idx:
                res += sum(self._tmp_sum[left_idx : right_idx + 1])
                if left_idx_reminder != 0:
                    res -= sum(self._nums[left - left_idx_reminder:left])
                if right_idx_reminder != 0 and (right_idx_reminder + len(self._nums)) % self._block_len != 0:
                    res -= sum(self._nums[right:right + self._block_len - right_idx_reminder])
            else:
                res += sum(self._tmp_sum[left_idx])
                if left_idx_reminder != 0:
                    res -= sum(self._nums[left - left_idx_reminder:left])
                if right_idx_reminder != 0:
                    res -= sum(self._nums[right:(right_idx + 1) * self._block_len])


        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == "__main__":
    nums = [9, -8]
    obj = NumArray(nums)
    obj.update(0, 3)
    print(obj.sumRange(1, 1))
    print(obj.sumRange(0, 1))
    obj.update(1, -3)
    print(obj.sumRange(0, 1))
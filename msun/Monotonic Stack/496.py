"496. Next Greater Element I"

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        ans = [-1] * m
        stack = []

        hash_table = dict()
        
        for i in range(n):
            while len(stack) > 0:
                if nums2[i] > nums2[stack[-1]]:
                    idx = stack.pop()
                    hash_table[nums2[idx]] = nums2[i]
                else:
                    break
            stack.append(i)
        
        for j in range(m):
            ans[j] = hash_table.get(nums1[j], -1)

        return ans



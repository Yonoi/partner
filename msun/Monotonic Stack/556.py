"556. Next Greater Element III"
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ans = -1

        str_n = list(str(n))
        length = len(str_n)
        first_lower_idx = length
        maximum = -1

        for i in range(length-1, -1, -1):
            if int(str_n[i]) >= maximum:
                maximum = int(str_n[i])
            else:
                first_lower_idx = i
                break
        
        for j in range(length-1, first_lower_idx, -1):
            if str_n[j] > str_n[first_lower_idx]:
                str_n[first_lower_idx], str_n[j] = str_n[j], str_n[first_lower_idx]
                break
    
        if first_lower_idx != length:
            ans = int(''.join(str_n[0:first_lower_idx + 1] + sorted(str_n[first_lower_idx + 1 : ])))

        return ans if ans <= 2 ** 31 - 1 else -1
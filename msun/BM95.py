#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# pick candy
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def candy(self , arr: List[int]) -> int:
        n = len(arr)
        ans = [1] * n

        for i in range(1, n):
            if arr[i] > arr[i-1]:
                ans[i] = ans[i-1] + 1
        
        for i in range(n-1, 0, -1):
            if arr[i-1] > arr[i] and ans[i-1] < ans[i] + 1:
                ans[i-1] = ans[i] + 1
        
        return sum(ans)

            

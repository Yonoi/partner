#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算成功举办活动需要多少名主持人
# @param n int整型 有n个活动
# @param startEnd int整型二维数组 startEnd[i][0]用于表示第i个活动的开始时间，startEnd[i][1]表示第i个活动的结束时间
# @return int整型
#
class Solution:
    def minmumNumberOfHost(self , n: int, startEnd: List[List[int]]) -> int:
        start_lst = [row[0] for row in startEnd]
        end_lst = [row[1] for row in startEnd]
        start_lst.sort()
        end_lst.sort()
        ans, j = 0, 0
        for i in range(n):
            if start_lst[i] >= end_lst[j]:
                j += 1
            else:
                ans += 1
        return ans


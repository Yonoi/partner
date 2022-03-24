#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?tpId=13&tqId=23445&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&sourceUrl=
# 
# @param A int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def multiply(self , A: List[int]) -> List[int]:
        # write code here
        B = []
        for i in range(len(A)):
            num = 1
            for j in range(len(A)):
                if i == j:
                    continue
                else:
                    num = num * A[j]
            B.append(num)
        return B
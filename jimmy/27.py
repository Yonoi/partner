#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=13&tqId=23271&ru=%2Fpractice%2Fef1f53ef31ca408cada5093c8780f44b&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&sourceUrl=
# 
# @param numbers int整型一维数组 
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        # write code here
        result = numbers[0]
        count = 0
        for i in numbers:
            if count == 0:
                result = i
            if i == result:
                count += 1
            else:
                count -= 1
        return result

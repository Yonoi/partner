#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=23269&ru=/practice/3194a4f4cf814f63919d0790578d51f3&qru=/ta/coding-interviews/question-ranking
# 
# @param rotateArray int整型一维数组 
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        # write code here
        num = temp = rotateArray[0]
        for i in range(len(rotateArray)):
            if i == 0:
                continue
            if rotateArray[i-1] > rotateArray[i]:
                temp = rotateArray[i]
                break
        return min(num, temp)
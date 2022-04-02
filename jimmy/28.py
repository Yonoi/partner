#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=23279&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
# 
# @param matrix int整型二维数组 
# @return int整型一维数组
#
class Solution:
    def printMatrix(self , matrix: List[List[int]]) -> List[int]:
        # write code here
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result
                

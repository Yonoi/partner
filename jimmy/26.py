#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型一维数组
#
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/ef1f53ef31ca408cada5093c8780f44b?tpId=13&tqId=1374930&ru=%2Fpractice%2F0e26e5551f2b489b9f58bc83aa4b6c68&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&sourceUrl=
# 
# @param array int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def reOrderArray(self , array: List[int]) -> List[int]:
        # write code here
        if not array:
            return []
        flag = 0
        temp = []
        length = len(array)
        while flag<length:
            if array[flag] % 2 == 1:
                temp.append(array[flag])
            else:
                array.append(array[flag])
            flag += 1
                
        return temp + array[length:]
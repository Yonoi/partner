#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/0c1b486d987b4269b398fee374584fc8?tpId=13&tqId=2221866&ru=/practice/fe6b651b66ae47d7acce78ffdd9a96c7&qru=/ta/coding-interviews/question-ranking
# 
# @param array int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def reOrderArrayTwo(self , array: List[int]) -> List[int]:
        # write code here
        n = len(array)
        # 双指针
        left, right = 0, n - 1
        while left < right:
            # 跳过左边的奇数
            while left < right and array[left] % 2 == 1:
                left += 1
            # 跳过右边的偶数
            while left < right and array[right] % 2 == 0:
                right -= 1
            # 交换条件：左指针指的是偶数且右指针指的是奇数
            while left < right and array[left] % 2 == 0 and array[right] % 2 == 1:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return array

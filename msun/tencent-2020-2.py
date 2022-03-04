#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param heights int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def findBuilding(self , heights ):
        length = len(heights)
        res = [1] * length

        left_stack = []
        right_stack = []
        
        for i in range(length):
            res[i] += len(left_stack)
            while left_stack and left_stack[-1] <= heights[i]:
                left_stack.pop()
            
            left_stack.append(heights[i])
        
        for j in range(length - 1, -1, -1):
            res[j] += len(right_stack)
            while right_stack and right_stack[-1] <= heights[j]:
                right_stack.pop()

            right_stack.append(heights[j])

        return res

if __name__ == '__main__':
    s = Solution()
    heights = [5,3,8,3,2,5]
    print(s.findBuilding(heights))
    
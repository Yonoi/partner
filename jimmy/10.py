# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0?tpId=13&tqId=23454&ru=/practice/91b69814117f4e8097390d107d2efbe0&qru=/ta/coding-interviews/question-ranking
# 
# @param pRoot TreeNode类 
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        ture_to_false = True
        queue = []
        result = []
        queue.append(pRoot)
        while queue:
            num = len(queue)
            tmp = []
            for i in range(num):
                node = queue.pop(0)
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                tmp.append(node.val)
            if tmp:
                if ture_to_false:
                    result.append(tmp)
                else:
                    tmp.reverse()
                    result.append(tmp)
            ture_to_false = not ture_to_false
        return result
            
            
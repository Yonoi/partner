# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#https://www.nowcoder.com/practice/435fb86331474282a3499955f0a41e8b?tpId=13&tqId=23294&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return int整型
#
class Solution:
    def TreeDepth(self , pRoot: TreeNode) -> int:
        # write code here
        if pRoot == None:
            return 0
        left = right = 0
        if pRoot.left:
            left = self.TreeDepth(pRoot.left)
        if pRoot.right:
            right = self.TreeDepth(pRoot.right)
        return max(left, right)+1
            
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return int整型一维数组
#
class Solution:
    def inorderTraversal(self , root: TreeNode) -> List[int]:
        stack, ans = [], []
        if root is None:
            return ans

        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node.right:
                stack.append(cur_node.right)
            
            if cur_node.left:
                stack.append(cur_node.left)
        return ans
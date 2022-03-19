# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root):
            if root is None:
                res.append('()')
                return None
            else:
                res.append('(')
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
                res.append(')')
        preorder(root)
        print(res)
        res = ''.join(res[1:-1]).replace('()()', '').replace('())', ')').replace(')()', ')')
        return res
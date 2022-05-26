# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isUnivalTree(self, root: TreeNode) -> bool:
#         val = root.val
#         queue = deque()
        
#         queue.append(root)

#         while queue:
#             node = queue.popleft()
#             if node.val != val:
#                 return False

#             if node.left != None:
#                 queue.append(node.left)
#             if node.right != None:
#                 queue.append(node.right)
#         return True

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        return self.dfs(root, val)
    
    def dfs(self, root, val):
        if root is None:
            return True
        
        if root.val != val:
            return False

        return self.dfs(root.left, val) and self.dfs(root.right, val)
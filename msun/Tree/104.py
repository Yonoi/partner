# 104. Maximum Depth of Binary Tree
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque()
        queue.append(root)

        if root is None:
            return 0
        
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                cur_node = queue.popleft()
                if cur_node is None:
                    continue
                queue.extend([cur_node.left, cur_node.right])
            ans += 1
        return ans

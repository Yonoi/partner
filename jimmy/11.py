# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/57aa0bab91884a10b5136ca2c087f8ff?tpId=13&tqId=2305268&ru=/practice/91b69814117f4e8097390d107d2efbe0&qru=/ta/coding-interviews/question-ranking
# 
# @param proot TreeNode类 
# @param k int整型 
# @return int整型
#
class Solution:
    def KthNode(self , proot: TreeNode, k: int) -> int:
        # write code here
        if proot == None or k == 0:
            return -1
        queue = []
        tmp = []
        queue.append(proot)
        while queue:
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                if not node:
                    continue
                tmp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if k > len(tmp):
            return -1
        tmp.sort()
        return tmp[k-1]
                  
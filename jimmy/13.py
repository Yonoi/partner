# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/a9d0ecbacef9410ca97463e4a5c83be7?tpId=13&tqId=1374963&ru=/practice/6e196c44c7004d15b1610b9afca8bd88&qru=/ta/coding-interviews/question-ranking
# 
# @param pRoot TreeNode类 
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        if pRoot == None:
            return None
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        pRoot.left = self.Mirror(pRoot.left)
        pRoot.right = self.Mirror(pRoot.right)
        return pRoot
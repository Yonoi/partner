# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=23293&ru=/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6&qru=/ta/coding-interviews/question-ranking
# 
# @param pRoot1 TreeNode类 
# @param pRoot2 TreeNode类 
# @return bool布尔型
#
class Solution:
    def doestree1havetree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.doestree1havetree2(pRoot1.left, pRoot2.left) and self.doestree1havetree2(pRoot1.right, pRoot2.right)
    def HasSubtree(self , pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.doestree1havetree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=23280&ru=/practice/a9d0ecbacef9410ca97463e4a5c83be7&qru=/ta/coding-interviews/question-ranking
# 
# @param root TreeNode类 
# @return int整型一维数组
#
class Solution:
    def PrintFromTopToBottom(self , root: TreeNode) -> List[int]:
        # write code here
        if not root:
            return None
        result = []
        tmp = [root]
        while tmp:
            node = tmp.pop(0)
            result.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        return result

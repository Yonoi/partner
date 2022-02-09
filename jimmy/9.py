# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://www.nowcoder.com/practice/f9f78ca89ad643c99701a7142bd59f5d?tpId=13&tqId=2273171&ru=/practice/fc533c45b73a41b0b44ccba763f866ef&qru=/ta/coding-interviews/question-ranking
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param val int整型 
# @return ListNode类
#
class Solution:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here
        newhead = head
        if head.val == val:
            return head.next
        while head:
            node = head.next
            if node.val == val:
                head.next = node.next
                return newhead
            head = head.next
        return newhead
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=23450&ru=/practice/f836b2c43afc4b35ad6adc41ec941dba&qru=/ta/coding-interviews/question-ranking
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @return ListNode类
#
class Solution:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        # write code here
        p0 = ListNode(None)
        p =p0
        p.next = pHead
        cur = pHead
        while cur and cur.next:
            if cur.val != cur.next.val:
                p = p.next
                cur = cur.next
            else:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                p.next = cur
        return p0.next
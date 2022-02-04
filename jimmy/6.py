# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#https://www.nowcoder.com/practice/886370fe658f41b498d40fb34ae76ff9?tpId=13&tqId=1377477&ru=/practice/6ab1d9a29e88450685099d45c9e31e46&qru=/ta/coding-interviews/question-ranking
class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        fast = pHead
        low = pHead
        for i in range(k):
            if fast == None:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            low = low.next
        return low
        # write code here
#         l = 0
#         current = []
#         if k == 0:
#             return None
#         while pHead:
#             current.append(pHead)
#             pHead = pHead.next
#             l = l+1
#         if l < k:
#             return None
#         return current[-k]

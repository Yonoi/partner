class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param lists ListNode类一维数组 
# @return ListNode类
#
class Solution:
    def mergeKLists(self , lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        list1 = lists[0]
        for list2 in lists[1:]:
            list1 = self.Merge(list1, list2)
        return list1
            
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
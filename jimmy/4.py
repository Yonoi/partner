# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=23257&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
#
# 
# @param pHead1 ListNodeš▒╗ 
# @param pHead2 ListNodeš▒╗ 
# @return ListNodeš▒╗
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        if not pHead1 or not pHead2:
            return None
        list1 = []
        list2 = []
        result = []
        while pHead1:
            list1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            list2.append(pHead2)
            pHead2 = pHead2.next
        while list1 and list2:
            value1 = list1.pop()
            value2 = list2.pop()
            if value1 == value2:
                result.append(value1)
        if result:
            node = result.pop()
            return node

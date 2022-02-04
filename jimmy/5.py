# -*- coding:utf-8 -*-
#https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=23449&ru=/practice/6ab1d9a29e88450685099d45c9e31e46&qru=/ta/coding-interviews/question-ranking
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        current = []
        while pHead:
            if pHead in current:
                return pHead
            current.append(pHead)
            pHead = pHead.next
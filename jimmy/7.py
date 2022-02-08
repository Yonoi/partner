# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
#https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=23254&ru=/practice/886370fe658f41b498d40fb34ae76ff9&qru=/ta/coding-interviews/question-ranking
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        node = RandomListNode(None)
        head = node
        while pHead:
            node.next = RandomListNode(pHead.label)
            node = node.next
            node.next = pHead.next
            node.random = pHead.random
            pHead = pHead.next
        return head.next

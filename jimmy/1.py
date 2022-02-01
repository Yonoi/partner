# -*- coding:utf-8 -*-
#https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=23278&ru=/ta/coding-interviews&qru=/t
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param listNode ListNode类
# @return int整型一维数组
#
class Solution:
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        re = []
        while(listNode):
            re.append(listNode.val)
            listNode = listNode.next
        re.reverse()
        return re
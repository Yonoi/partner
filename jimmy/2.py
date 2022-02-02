#https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=23286&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , Phead):
        if not Phead or not Phead.next:
            return Phead
        else:
            current = ListNode(None)
            while Phead.next != None:
                pre = ListNode(None) #记录下一个表头
                current.val = Phead.val #好像不写这行也行？
                pre.val = Phead.next.val #set up下一个表头的val
                pre.next = current#表头和现有的反转链表连接
                Phead = Phead.next#pHead 往后移动一步，直到最后一个数
                current = pre#更新当前反转链表
            return pre

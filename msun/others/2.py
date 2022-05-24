# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, reminder = (l1.val + l2.val) // 10, (l1.val + l2.val) % 10
        newListNode = ListNode(reminder)
        tmpListNode = newListNode
        while l1.next != None and l2.next != None:
            l1, l2 = l1.next, l2.next
            carry, reminder = (l1.val + l2.val + carry) // 10, (l1.val + l2.val + carry) % 10
            tmpListNode.next = ListNode(reminder)
            tmpListNode = tmpListNode.next
        
        res_list = l2 if l1.next == None else l1
        while res_list.next != None:
            res_list = res_list.next
            carry, reminder = (res_list.val + carry) // 10, (res_list.val + carry) % 10
            tmpListNode.next = ListNode(reminder)
            tmpListNode = tmpListNode.next
            
        if carry != 0:
            tmpListNode.next = ListNode(carry)
        return newListNode
            
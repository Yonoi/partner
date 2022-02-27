class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        if head is None:
            return None
        new_head = head
        tmp_head = head.next
        rear = head
        rear.next = None
        
        while tmp_head != None:
            new_head, tmp_head = tmp_head, tmp_head.next
            new_head.next = rear
            rear = new_head

        return new_head

if __name__ == "__main__":
    s = Solution()
    data = [1, 2, 3]
    head = ListNode(data[0])
    tmp = head
    for i in data[1:]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    
    new_head = s.ReverseList(head)
    
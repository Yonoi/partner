import time
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param m int整型 
# @param n int整型 
# @return ListNode类
#
class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        tmp = head
        i, j = 1, 1
        while tmp != None:
            if i == m - 1:
                pre_head = tmp
            if i == m:
                m_node = tmp
            if j == n:
                n_node = tmp
            tmp = tmp.next
            i += 1
            j += 1
        
        new_head = m_node
        tmp_head = m_node.next
        rear = m_node
        rear.next = n_node.next
        last_rear = m_node

        i = m
        while i < n:
            new_head, tmp_head = tmp_head, tmp_head.next
            new_head.next = rear
            rear = new_head
            i += 1
        
        # m_node.next = n_node.next

        if m == 1:
            return new_head
        else:
            pre_head.next = new_head
            return head

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    tmp = head
    for i in range(2, 6):
        tmp.next = ListNode(i)
        tmp = tmp.next
    m, n = 2, 4
    new_head = s.reverseBetween(head, m, n)
    while new_head != None:
        print(new_head.val)
        new_head = new_head.next
        
        time.sleep(1)



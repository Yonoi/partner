# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head
        start_idx, end_idx = 1, k
        i = 1
        tmp = head
        multi_head = []
        multi_rear = []
        while tmp != None:
            if i % k == 1:
                start_idx = i
                m_node = tmp
                multi_rear.append(m_node)
                tmp = tmp.next
            elif i % k == 0:
                end_idx = i
                n_node = tmp
                tmp = tmp.next
                
                new_head = m_node
                tmp_head = m_node.next
                rear = m_node
                rear.next = None

                while start_idx < end_idx:
                    new_head, tmp_head = tmp_head, tmp_head.next
                    new_head.next = rear
                    rear = new_head
                    start_idx += 1
                multi_head.append(new_head)            
            else: 
                tmp = tmp.next
            i += 1
            if tmp is None and start_idx > end_idx:
                multi_rear.pop()
                multi_rear[-1].next = m_node 
        for pre, after in zip(multi_rear[:-1], multi_head[1:]):
            pre.next = after
        
        return head if  i <= k else multi_head[0]
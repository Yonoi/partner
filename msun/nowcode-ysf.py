class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def ysf(self , n: int, m: int) -> int:
        if m == 1:
            return n
        head = Node(1)
        tmp = head
        for i in range(2, n + 1):
            tmp.next = Node(i)
            tmp = tmp.next
        tmp.next = head 
        pre, cur = head, head

        i = 1
        j = 1
        while i < n:
            if j == m % n:
                pre.next = cur.next
                print(cur.val)
                i += 1
                j = 0
            else:
                pre = cur
            cur = cur.next
            j += 1
        return pre.val

if __name__ == "__main__":
    s = Solution()
    n, m = 5,3
    print(s.ysf(n, m))
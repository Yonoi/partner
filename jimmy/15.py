# -*- coding:utf-8 -*-
#https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=23281&ru=/practice/508378c0823c423baa723ce448cbfd0c&qru=/ta/coding-interviews/question-ranking
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
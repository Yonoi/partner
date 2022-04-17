# 207. Course Schedule
from typing import List
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        sub_one = lambda x : [each - 1 for each in x ]
        for row in prerequisites:
            adjacency[row[1]].append(row[0])
            indegree[row[0]] += 1
        
        queue = deque()
        for idx, degree in enumerate(indegree):
            if degree == 0:
                queue.append(idx)

        while numCourses > 0:
            cur = queue.popleft()
            queue.extend(adjacency[cur])
            numCourses -= 1

        return False if len(queue) == 0 else True

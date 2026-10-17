from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        need_degrees = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for course, preq in prerequisites:
            adj[preq].append(course)
            need_degrees[course]  += 1
        
        queue = deque()
        for course in range(numCourses):
            if need_degrees[course] == 0:
                queue.append(course)
        
        count_processed = 0

        while queue:
            ready = queue.popleft()
            count_processed += 1

            for neighbor in adj[ready]:
                need_degrees[neighbor] -= 1
                if need_degrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return count_processed == numCourses



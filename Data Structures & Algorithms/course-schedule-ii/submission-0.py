from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        num_prereqs = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, preq in prerequisites:
            adj[preq].append(course)
            num_prereqs[course] += 1

        queue = deque()

        for i in range(numCourses):
            if num_prereqs[i] == 0:
                queue.append(i)
        
        order = []

        while queue:
            first = queue.popleft()
            order.append(first)

            for neighbor in adj[first]:
                num_prereqs[neighbor] -= 1

                if num_prereqs[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != numCourses:
            return []
        return order

        

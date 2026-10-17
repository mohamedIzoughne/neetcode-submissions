from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        # 0: not visited, 1: visiting, 2: visited
        state = [0]*numCourses
        needs = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for course, preq in prerequisites:
            needs[course] += 1
            adj[preq].append(course)
        
        starters = []
        for i in range(numCourses):
            if needs[i] == 0:
                starters.append(i)
        order = []


        def is_acycled(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1
            order.append(node)

            for neighbor in adj[node]:
                if not is_acycled(neighbor):
                    return False
                

            state[node] = 2
            return True
            
        
        for starter in starters:
            if state[starter] == 0:
                if not is_acycled(starter):
                    return []
        if len(order) != numCourses:
            return []
        return order




from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Pre-allocate adjacency list using fixed lists instead of dict hashing
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = unvisited, 1 = visiting, 2 = safe
        state = [0] * numCourses

        def has_cycle(node: int) -> bool:
            if state[node] == 1:
                return True   # Back-edge (cycle detected)
            if state[node] == 2:
                return False  # Already confirmed safe

            state[node] = 1   # Mark as visiting

            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True

            state[node] = 2   # Mark as safe
            return False

        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False

        return True
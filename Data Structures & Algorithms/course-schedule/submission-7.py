from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for prerequisite in prerequisites:
            if prerequisite[0] in graph:
                graph[prerequisite[0]].append(prerequisite[1])
            else:
                graph[prerequisite[0]] = [prerequisite[1]]

        visited_roots = set()   # Nodes fully verified to have no cycles (safe)
        visiting = set()        # Nodes currently in the DFS recursion stack

        def check_cycle(node):
            # If the node is currently in our recursion stack, we found a cycle!
            if node in visiting:
                return False
            # If we already verified this node in a previous search, it's safe
            if node in visited_roots:
                return True
            # If the node has no outgoing prerequisites, it's safe
            if node not in graph:
                visited_roots.add(node)
                return True

            # Add to current recursion path
            visiting.add(node)

            for need in graph[node]:
                if not check_cycle(need):
                    return False

            # Backtrack: remove from current path since we are unwinding
            visiting.remove(node)
            # Memoize: this node is now fully verified as safe
            visited_roots.add(node)
            return True

        for node in graph.keys():
            if node not in visited_roots:
                if not check_cycle(node):
                    return False

        return True
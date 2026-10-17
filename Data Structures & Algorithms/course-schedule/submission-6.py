class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for prerequisite in prerequisites:

            if prerequisite[0] in graph:
                graph[prerequisite[0]].append(prerequisite[1])
            else:
                graph[prerequisite[0]] = [prerequisite[1]]

        visited_roots = set()
        def check_cycle(node, checked_paths):
            
            for need in graph[node]:
                if need in graph:
                    if (node, need) in checked_paths:
                        return False
                        
                    if need in visited_roots:
                        continue

                    checked_paths.add((node, need))
                    if not check_cycle(need, set(checked_paths)):
                        return False
                    else:
                        visited_roots.add(need)
            return True
            

        for node in graph.keys():
            checked_paths = set()
            if node not in visited_roots and not check_cycle(node, checked_paths):
                return False
        

        # print(visited_roots)
        
        return True


            

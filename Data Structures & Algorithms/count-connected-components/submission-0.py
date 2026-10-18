class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}

        for a, b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]


        def traverse(node, prev, visited):

            if node in visited:
                return None

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != prev:
                    traverse(neighbor, node, visited)
        
        visited = set()
        components_counter = 0

        for key in graph.keys():

            if key not in visited:
                traverse(key, key, visited)
                components_counter += 1

        return components_counter

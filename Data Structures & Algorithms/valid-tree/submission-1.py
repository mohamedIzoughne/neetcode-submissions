class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree: no cycle, at least 3 nodes right? or not necessarily?
        # what's hard about it : undirected graph
        dic = {}

        if len(edges) == 0:
            return True

        for edge in edges:
            if edge[0] in dic:
                dic[edge[0]].append(edge[1])
            else:
                dic[edge[0]]=[edge[1]]
            
            if edge[1] in dic:
                dic[edge[1]].append(edge[0])
            else:
                dic[edge[1]]=[edge[0]]

        def is_acyclic(node, visited, prev=None):

            if node in visited:
                return False

            visited.add(node)

            for neighbor in dic[node]:
                if prev != neighbor:
                    if not is_acyclic(neighbor, visited, node):
                        return False
            
            return True
        
        visited = set()
        return is_acyclic(edges[0][0], visited) and len(visited) == n
        
            
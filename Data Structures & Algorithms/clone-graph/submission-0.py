"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        if node is None:
            return None
        
        copy = Node(node.val)

        visited = {}
        visited[copy.val] = copy

        def traverse(node, clone):
            for i in node.neighbors:
                if i.val in visited:
                    print('repeated:', i.val)
                    clone.neighbors.append(visited[i.val])
                else:
                    print('non repeated:', i.val)
                    copy = Node(i.val)
                    clone.neighbors.append(copy)
                    visited[i.val] = copy
                    traverse(i, copy)
            return clone

        traverse(node, copy)
        # print(copy.val, copy.neighbors)
        # print(copy.neighbors)
        return copy



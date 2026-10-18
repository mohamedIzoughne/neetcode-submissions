from collections import deque

class Connection:
    def __init__(self):
        self.connection_set = set()
        self.connection_queue = deque()
        self.last_element = None
    
    def add(self, node):
        self.connection_set.add(node)
        self.connection_queue.append(node)
    
    def pop(self):
        ele = self.connection_queue.pop()
        self.connection_set.remove(ele)

    def popleft(self):
        ele = self.connection_queue.popleft()
        self.connection_set.remove(ele)
        return ele
    
    def exists(self, node):
        return node in self.connection_set
    
    def set_last(self, node):
        self.last_element = node

    def remove_uncycled(self):
        element = None
        # print(self.last_element)
        while element != self.last_element:
            element = self.popleft()
        
        self.add(self.last_element)
    
    def edge_exists(self, edge):
        return self.exists(edge[0]) and self.exists(edge[1])


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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
            
        connections = []
        last = None

        def check_cycle(node, prev, connection):
            if connection.exists(node):
                connections.append(connection)
                connection.set_last(node)
                return True
            connection.add(node)
            # visited.add(node)
            # queue.append(node)

            for neighbor in graph[node]:
                if neighbor != prev:
                    if check_cycle(neighbor, node, connection):
                        return True
            # visited.remove(node)
            # queue.pop()
            connection.pop()
            return False
        
        # visited = set()
        # queue = deque()
        connection = Connection()
        check_cycle(edges[0][0], edges[0][0], connection)
        connection.remove_uncycled()

        for index in range(len(edges) -1, -1, -1):
            if connection.edge_exists(edges[index]):
                return edges[index]
        # print(connection.connection_queue)
        # print(connections[0].connection_queue, connections[0].last_element)


        # for 

                
        



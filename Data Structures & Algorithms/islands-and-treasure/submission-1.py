from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]):
        
        INF = 2147483647
        visited = set()
        
        def traverse(queue):
            while queue:
                i, j, distance = queue.popleft()

                if distance < grid[i][j]:
                    grid[i][j] = distance

                # 1. Only check if the neighbor is an empty room (INF)
                # 2. Add to visited IMMEDIATELY before appending to queue
                
                if i > 0 and grid[i - 1][j] == INF and (i-1, j) not in visited:
                    visited.add((i-1, j)) 
                    queue.append((i - 1, j, distance + 1))

                if j > 0 and grid[i][j - 1] == INF and (i, j-1) not in visited:
                    visited.add((i, j-1))
                    queue.append((i, j - 1, distance + 1))
                    
                # Fixed your typo here (removed grid[i + 1][j] != 0)
                if i < len(grid) - 1 and grid[i + 1][j] == INF and (i+1, j) not in visited:
                    visited.add((i+1, j))
                    queue.append((i + 1, j, distance + 1))

                if j < len(grid[0]) - 1 and grid[i][j + 1] == INF and (i, j+1) not in visited:
                    visited.add((i, j+1))
                    queue.append((i, j + 1, distance + 1))

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j)) # Don't forget to mark the starting points as visited!
        
        traverse(queue)
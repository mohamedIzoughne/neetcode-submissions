class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        maximum_area = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()

        def traverse(node):
            if grid[node[0]][node[1]] == 0:
                return 0

            visited.add(node)
            return_value = 1

            for dr in directions:
                newdir = (node[0] + dr[0], node[1] + dr[1])

                if  0 <= newdir[0] < len(grid) and  0 <= newdir[1] < len(grid[0]) and newdir not in visited:
                    return_value += traverse(newdir)
            
            return return_value


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maximum_area = max(maximum_area, traverse((i, j)))
        

        return maximum_area
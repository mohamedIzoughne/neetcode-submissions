class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        islands_num = 0

        def bfs(index):
            i, j = index
            grid[i][j] = "#"
            
            if j < width - 1 and grid[i][j + 1] == "1":
                bfs((i, j + 1))

            if i < height - 1 and grid[i + 1][j] == "1":
                bfs((i + 1, j))

            if i > 0 and grid[i - 1][j] == "1":
                bfs((i - 1, j))

            if j > 0 and grid[i][j - 1] == "1":
                bfs((i, j - 1))
            


        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    bfs((i, j))
                    islands_num += 1
        
        return islands_num


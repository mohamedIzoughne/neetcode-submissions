class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        def traverse(start_r, start_c):
            pacific = False
            atlantic = False

            stack = [(start_r, start_c)]
            visited = set()
            visited.add((start_r, start_c))
            
            # Combine all directions so water can meander freely
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while stack:
                r, c = stack.pop()
                
                # Check if the current cell touches either ocean
                if r == 0 or c == 0:
                    pacific = True
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic = True
                    
                # If we found both, no need to keep searching for this starting cell
                if pacific and atlantic:
                    return True

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check bounds
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        # Check if unvisited and water can flow downhill/flat
                        if (nr, nc) not in visited and heights[nr][nc] <= heights[r][c]:
                            visited.add((nr, nc))
                            stack.append((nr, nc))

            return pacific and atlantic
            
        results = []

        for i in range(ROWS):
            for j in range(COLS):
                if traverse(i, j):
                    results.append([i, j])
        
        return results
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        o_visited = set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        regions = []

        def is_region_surrounded(region):
            for cell in region:
                if cell[0] == 0 or cell[1] == 0 or cell[0] == len(board) - 1 or cell[1] == len(board[0]) - 1:
                    return False
            return True
        
        def fill_with_X(region):
            for cell in region:
                board[cell[0]][cell[1]] = 'X'



        def traverse(source):
            queue = deque([source])
            visited = set()
            visited.add(source)
            region = []
            while queue:
                i, j = queue.popleft()


                if board[i][j] == 'O':
                    o_visited.add((i, j))
                    region.append((i, j))

                    for diri in directions:
                        index = (i + diri[0], j + diri[1])

                        if 0 <= index[0] < len(board) and 0 <= index[1] < len(board[0]) and index not in visited:
                            queue.append(index)
                            visited.add(index)
            
            regions.append(region)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in o_visited:
                    traverse((i, j))


        for region in regions:
            if is_region_surrounded(region):
                fill_with_X(region)

        
        # print(regions)
            
                    


            
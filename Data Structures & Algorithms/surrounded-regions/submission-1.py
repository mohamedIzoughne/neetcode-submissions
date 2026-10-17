class Solution:
    def solve(self, board: List[List[str]]) -> None:
        o_visited = set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        regions = []
        surrounded_set = set()
        
        def fill_with_X(region):
            for cell in region:
                board[cell[0]][cell[1]] = 'X'
        


        def traverse(source):
            queue = deque([source])
            visited = set()
            visited.add(source)
            region = []
            surrounded = True

            while queue:
                i, j = queue.popleft()

                


                if board[i][j] == 'O':
                    o_visited.add((i, j))
                    region.append((i, j))

                    if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                        surrounded = False

                    for diri in directions:
                        index = (i + diri[0], j + diri[1])

                        if 0 <= index[0] < len(board) and 0 <= index[1] < len(board[0]) and index not in visited:
                            queue.append(index)
                            visited.add(index)
            
            if surrounded:
                surrounded_set.add(len(regions))

            regions.append(region)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in o_visited:
                    traverse((i, j))

        print(surrounded_set)

        for i in range(len(regions)):
            
            if i in surrounded_set:
                fill_with_X(regions[i])

        
        # print(regions)
            
                    


            
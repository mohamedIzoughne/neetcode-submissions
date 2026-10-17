class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        first_indexes = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    index = (i, j)
                    first_indexes.append(index)


        def bfs(index, visited, found = 1):
            i = index[0]
            j = index[1]


            if found == len(word):
                return True

            visited.add(index)
            letter = word[found]
            width = len(board[0]) - 1
            height = len(board) - 1

            first, second, third, fourth = False, False, False, False

            if j < width and letter == board[i][j+1] and (i, j+1) not in visited:
                first= bfs((i, j + 1), visited, found + 1)

            if i < height and letter == board[i + 1][j] and (i + 1, j) not in visited:
                second = bfs((i + 1, j), visited, found + 1)

            if i > 0 and letter == board[i - 1][j] and (i - 1, j) not in visited:
                third = bfs((i - 1, j), visited, found + 1)
            
            if j > 0 and letter == board[i][j - 1] and (i, j-1) not in visited:
                fourth = bfs((i, j - 1), visited, found + 1)

            is_complete = first or second or third or fourth

            if not is_complete:
                visited.remove(index)
            
            return first or second or third or fourth

        for i in first_indexes:
            does_ex = bfs(i, set())
            if does_ex:
                return True

        return False
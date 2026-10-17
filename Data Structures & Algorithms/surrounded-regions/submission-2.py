from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        queue = deque()

        # Step 1: Collect all 'O' cells along the 4 borders
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == 'O':
                    board[r][c] = 'E'
                    queue.append((r, c))

        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == 'O':
                    board[r][c] = 'E'
                    queue.append((r, c))

        # Step 2: BFS to mark all cells connected to the border as 'E'
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'E'
                    queue.append((nr, nc))

        # Step 3: Flip surrounded 'O's to 'X', and restore 'E's back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
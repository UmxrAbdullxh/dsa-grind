class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visitedSet = set()
        
        def dfs(r, c, visited):
            if(r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visited or board[r][c] == "X"):
                return

            visited.add((r,c))

            dfs(r-1, c, visited)
            dfs(r+1, c, visited)
            dfs(r, c-1, visited)
            dfs(r, c+1, visited)

            return

            

        
        for r in range(ROWS):
            dfs(r, 0, visitedSet)
            dfs(r, COLS - 1, visitedSet)

        for c in range(COLS):
            dfs(0, c, visitedSet)
            dfs(ROWS - 1, c, visitedSet)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visitedSet:
                    board[r][c] = "X"
         

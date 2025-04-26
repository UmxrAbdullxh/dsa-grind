class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        res = []
        board = [["."] * n for i in range(n) ]
        
        def dfs(r):
            # Reached base condition that r = n
            if r == n:
                copy = ["".join(b) for b in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                # possible solution
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)

                # cleanup
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        dfs(0)
        return res
        

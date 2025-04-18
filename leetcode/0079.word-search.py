class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res = [False]

        hashMap = {}

        def dfs(m,n,char):
            if m < 0 or n < 0 or m >= len(board) or n >= len(board[m]) or char >= len(word):
                return
            if tuple((m,n)) in hashMap:
                return
            if board[m][n] != word[char]:
                return
            if board[m][n] == word[char]:
                visited = tuple((m, n))
                hashMap[visited] = 1
            if char == len(word) -1:
                res[0] = True
                return
            
            # Above
            dfs(m-1, n, char+1)
            # Right
            dfs(m, n+1, char+1)
            # Down
            dfs(m+1, n, char+1)
            # Left
            dfs(m, n-1, char+1)

            #delete from hashmap
            del hashMap[tuple((m,n))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    hashMap = {}
                    dfs(i, j, 0)

        return res[0]

        

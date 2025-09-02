class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for j in range(n+1)] for i in range(m + 1)]
        table[1][1] = 1
        for i in range(m+1):
            for j in range(n+1):
                current = table[i][j] 
                if i+1 <= m:
                    table[i+1][j] += current
                if j + 1 <= n:
                    table[i][j+1] += current
        return table[m][n]
        

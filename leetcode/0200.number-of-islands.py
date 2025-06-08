class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visitSet = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                val = self.dfs(grid, row, col, visitSet)
                if val == True:
                    res += 1
        return res

    def dfs(self, grid, r, c, visited):
        if r < 0 or r > len(grid) - 1:
            return False
        if c < 0 or c > len(grid[r]) - 1:
            return False
        if grid[r][c] == "0":
            return False
        pos = str(r) + "," + str(c)
        if pos in visited:
            return False
        visited.add(pos)

        # explore all sides
        self.dfs(grid, r-1, c, visited)
        self.dfs(grid, r+1, c, visited)
        self.dfs(grid, r, c-1, visited)
        self.dfs(grid, r, c+1, visited)

        return True
    

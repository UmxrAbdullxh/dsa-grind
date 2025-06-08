class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visitSet = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                val = self.dfs(grid, row, col, visitSet)
                if val > res:
                    res = val
        return res

    def dfs(self, grid, r, c, visited):
        if r < 0 or r > len(grid) - 1:
            return 0
        if c < 0 or c > len(grid[r]) - 1:
            return 0
        if grid[r][c] == 0:
            return 0
        pos = str(r) + "," + str(c)
        if pos in visited:
            return 0
        visited.add(pos)

        # explore all sides
        temp = self.dfs(grid, r-1, c, visited) + self.dfs(grid, r+1, c, visited)+ self.dfs(grid, r, c-1, visited) + self.dfs(grid, r, c+1, visited)

        return temp + 1
    

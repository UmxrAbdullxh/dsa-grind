class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    rows, cols = r + dr, c + dc
                    if(rows<0 or rows == ROWS or cols<0 or cols==COLS or grid[rows][cols] != 1):
                        continue
                    grid[rows][cols] = 2
                    q.append([rows, cols])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

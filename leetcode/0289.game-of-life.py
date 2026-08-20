class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        if (i, j)
        left = [i, j-1]
        right = [i, j+1]
        top = [i-1, j]
        bottom = [i+1, j]
        top_left = [i-1, j-1]
        top_right = [i-1, j+1]
        bottom_left = [i+1, j-1]
        bottom_right = [i+1, j+1]
        """
        rows, cols = len(board), len(board[0])
        temp = [[0]*cols for _ in range(rows)]
        deltas = [(-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0),  (1,1)]

        for i in range(rows):
            for j in range(cols):
                count = 0
                for di, dj in deltas:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        count += board[ni][nj]
                if board[i][j] == 1:
                    if count < 2:
                        temp[i][j] = 0
                    elif count > 3:
                        temp[i][j] = 0
                    else:
                        temp[i][j] = 1
                else:
                    if count == 3:
                        temp[i][j] = 1
                    else:
                        temp[i][j] = 0
        for i in range(rows):
            for j in range(cols):
                board[i][j] = temp[i][j]

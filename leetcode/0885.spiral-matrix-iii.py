class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = rStart, cStart
        result = [[r, c]]
        i = 0

        while len(result) < rows * cols:
            dr, dc = directions[i%4]
            length = i // 2 + 1
            for _ in range(length):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            i += 1
        return result
        
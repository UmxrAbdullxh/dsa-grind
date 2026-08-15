class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def transpose(matrix):
            for i in range(n):
                for j in range(i + 1, n):   # note: starts at i+1, not 0
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        transpose(matrix)
        for i in matrix:
            reverse(i, 0, len(i)-1)
        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            i = 0
            j = len(row) - 1
            while(i <= j):
                mid = (i + j) // 2
                if( row[mid] == target ):
                    return True
                elif( row[mid] < target ):
                    i += 1
                else:
                    j -= 1
        return False
        

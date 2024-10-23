class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCounter = defaultdict(list)
        columnCounter = defaultdict(list)
        gridCounter = defaultdict(list)
        for i, n in enumerate(board):
            for j, m in enumerate(n):
                if m != ".":
                    if( m in rowCounter[i] or m in columnCounter[j] or m in gridCounter[(i//3, j//3)] ):
                        return False
                    else:
                        rowCounter[i].append(m)
                        columnCounter[j].append(m)
                        gridCounter[(i//3, j//3)].append(m)
        return True

        

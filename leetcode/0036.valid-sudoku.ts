function isValidSudoku(board: string[][]): boolean {
    const row = {}
    const column = {}
    const grid = {}

    const ROW = 9;
    const COLUMN = 9;

    for(let i=0; i<ROW;i++) {
        for(let j=0;j<COLUMN;j++) {
            let num = board[i][j]
            let tuple = `${Math.floor(i/3)},${Math.floor(j/3)}`
            if(num != ".") {
                if((row[i] != undefined && row[i].includes(num))
                    || (column[j] !== undefined && column[j].includes(num))
                    || (grid[tuple] !== undefined && grid[tuple].includes(num))
                ) {
                    return false
                }
                else {
                    (row[i] === undefined) ? row[i] = [num] : row[i].push(num);
                    (column[j] === undefined) ? column[j] = [num] : column[j].push(num);
                    (grid[tuple] === undefined) ? grid[tuple] = [num] : grid[tuple].push(num);
                }
            }
        }
    }
    return true
    
};
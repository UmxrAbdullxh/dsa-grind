function searchMatrix(matrix: number[][], target: number): boolean {
    const r = matrix.length;
    const c = matrix[0].length;

    let low = 0;
    let high = (r * c) - 1;

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const midR = Math.floor(mid / c);
        const midC = mid % c;

        if (matrix[midR][midC] === target) return true;
        else if (matrix[midR][midC] < target) low = mid + 1;
        else high = mid - 1;
    }

    return false;
};
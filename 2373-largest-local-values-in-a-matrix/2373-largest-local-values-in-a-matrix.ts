function largestLocal(grid: number[][]): number[][] {
    const n = grid.length
    const ans: number[][] = []
    for (let i=1; i<n-1; i++) {
        const temp = []
        for (let j=1; j<n-1; j++) {
            temp.push(
                Math.max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1],
                )
            )
        }
        ans.push(temp)
    }
    return ans
};
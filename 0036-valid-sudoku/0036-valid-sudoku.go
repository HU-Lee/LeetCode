func isValidSudoku(board [][]byte) bool {
    rows := [9][9]int{}
    cols := [9][9]int{}
    squares := [9][9]int{}

    for i, row := range board {
        for j, val := range row {
            if val == '.' {
                continue
            }
            idx := val - '1'
            square := (j/3)*3 + i/3
            if rows[i][idx] != 0 {
                return false
            }
            if cols[j][idx] != 0 {
                return false
            }
            if squares[square][idx] != 0 {
                return false
            }
            rows[i][idx] = 1
            cols[j][idx] = 1
            squares[square][idx] = 1
        }
    }
    return true
}
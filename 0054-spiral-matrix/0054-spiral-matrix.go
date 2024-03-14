func spiralOrder(matrix [][]int) []int {
    i,j := 0,-1
    m,n := len(matrix[0]), len(matrix)

    visited := make([][]int, n)
    for i := range visited {
        visited[i] = make([]int, m)
    }
    sum := m*n
    direction := 0
    var arr []int 
    for sum > 0 {
        var x,y int
        switch direction {
                case 0:
                    x,y = 0,1
                case 1:
                    x,y = 1,0
                case 2:
                    x,y = 0,-1
                case 3:
                    x,y = -1,0
        }
        if (i+x >= n || j+y >= m || i+x < 0 || j+y < 0 || visited[i+x][j+y] == 1) {
            direction = (direction+1)%4
        } else {
            i += x
            j += y
            arr = append(arr, matrix[i][j])
            visited[i][j] = 1
            sum--
        }
        
    }
    return arr
}
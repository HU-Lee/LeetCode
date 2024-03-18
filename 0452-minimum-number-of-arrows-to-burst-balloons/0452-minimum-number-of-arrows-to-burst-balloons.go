func findMinArrowShots(points [][]int) int {
    sort.Slice(points, func (x int,y int) bool {
        if points[x][0] == points[y][0] {
            return points[x][1] < points[y][1]
        } else {
            return points[x][0] < points[y][0]
        }
    })

    tmp := []int{points[0][0],points[0][1]}
    cnt := 1
    for _, point := range points {
        if point[0] > tmp[1] {
            cnt++
            tmp = []int{point[0], point[1]}
        } else {
            tmp[0] = point[0]
            if tmp[1] > point[1] {
                tmp[1] = point[1]
            }
        }
    }
    return cnt
}
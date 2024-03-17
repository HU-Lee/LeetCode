func insert(intervals [][]int, newInterval []int) [][]int {
    if len(intervals) == 0 {
        return [][]int{newInterval}
    }
    var ans [][]int
    tmp := []int{newInterval[0],newInterval[1]}
    tmpEnd := false
    for _, interval := range intervals {
        if interval[1] < tmp[0] {
            ans = append(ans, interval)
        } else if interval[0] > tmp[1] {
            if !tmpEnd {
                tmpEnd = true
                ans = append(ans, tmp)
            }
            ans = append(ans, interval)
        } else {
            mi := interval[0]
            mx := interval[1]
            if mi < tmp[0] {
                tmp[0] = mi
            }
            if mx > tmp[1] {
                tmp[1] = mx
            }
        }
    }
    if !tmpEnd {
        tmpEnd = true
        ans = append(ans, tmp)
    }
    return ans
}
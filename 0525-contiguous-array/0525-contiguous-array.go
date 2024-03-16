func findMaxLength(nums []int) int {
    sum_start := make(map[int]int) 
    sum := 0
    sum_start[0] = -1
    k := 0
    for i, num := range(nums) {
        if num == 1 {
            sum++
        } else {
            sum--
        }
        if val, ok := sum_start[sum]; !ok {
            sum_start[sum] = i
        } else {
            if k < i-val {
                k = i - val
            }
        }
    }
    return k
}
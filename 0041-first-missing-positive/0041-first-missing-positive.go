func firstMissingPositive(nums []int) int {
    n := len(nums)
    exists := make([]int, n)
    for i:=0; i < n; i++ {
        exists[i] = 0
    }
    for _, num := range nums {
        if num > 0 && num <= n {
            exists[num-1] = 1
        }
    }
    for idx, val := range exists {
        if val == 0 {
            return idx + 1
        }
    } 
    return n+1
}
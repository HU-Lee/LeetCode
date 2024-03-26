func firstMissingPositive(nums []int) int {
    // without additional array
    n := len(nums)
    i := 0
    for i < n {
        num := nums[i]
        if num > 0 && num <= n && nums[num-1] != num {
            nums[i], nums[num-1] = nums[num-1], nums[i]
        } else {
            i++
        }
    }
    for idx, val := range nums {
        if val != idx+1 {
            return idx+1
        }
    } 
    return n+1
}
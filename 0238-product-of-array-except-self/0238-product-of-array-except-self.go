func productExceptSelf(nums []int) []int {
    l := len(nums)
    res := make([]int, l)
    res[0] = 1
    val := 1
    for i := 1; i < l; i++ {
        val *= nums[i-1]
        res[i] = val
    }
    val = 1
    for i := l-2; i>=0; i-- {
        val *= nums[i+1]
        res[i] *= val
    } 
    return res
}
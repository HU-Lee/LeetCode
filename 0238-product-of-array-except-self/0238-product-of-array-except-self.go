func productExceptSelf(nums []int) []int {
    l := len(nums)
    res := make([]int, l)
    after := make([]int, l)
    res[0] = 1
    for i := 1; i < l; i++ {
        res[i] = res[i-1]*nums[i-1]
    }
    after[l-1] = 1
    for i := l-2; i>=0; i-- {
        after[i] = after[i+1]*nums[i+1]
    } 
    
    for i := 0; i < l; i++ {
        res[i] *= after[i]
    }
    return res
}
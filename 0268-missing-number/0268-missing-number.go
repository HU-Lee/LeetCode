func missingNumber(nums []int) int {
    n := len(nums)
    val := n*(n+1)/2
    for _, num := range nums {
        val -= num
    }
    return val
}
func numSubarrayProductLessThanK(nums []int, k int) int {
    ans := 0
    l := len(nums)
    left := 0
    cur := 1
    for i := 0; i < l; i++ {
        cur *= nums[i]
        for cur >= k && left <= i {
            cur /= nums[left]
            left++
        }

        ans += i - left +1
    }
    return ans
}
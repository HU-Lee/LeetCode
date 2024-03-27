func numSubarrayProductLessThanK(nums []int, k int) int {
    ans := 0
    l := len(nums)
    for i := 0; i < l; i++ {
        if nums[i] >= k {
            continue
        }

        c := 0
        cur := nums[i]
        for j := i+1; j < l; j++ {
            cur *= nums[j]
            if cur >= k {
                break
            } else {
                c++
            }
        }
        ans += c+1
    }
    return ans
}
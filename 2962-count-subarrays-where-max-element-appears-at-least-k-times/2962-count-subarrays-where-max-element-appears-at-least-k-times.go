func countSubarrays(nums []int, k int) int64 {
    l := len(nums)
    m := nums[0]
    for _, num := range nums {
        if num > m {
            m = num
        }
    }
    count, left, right, ans := 0, 0, 0, 0 
    for right < l {
        if nums[right] == m {
            count++
        }
        right++
        for count >= k {
            if nums[left] == m {
                count--
            }
            left++
        }
        ans += left
    }
    return int64(ans)
}
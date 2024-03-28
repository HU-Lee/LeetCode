func maxSubarrayLength(nums []int, k int) int {
    left := 0
    ans := 0
    dic := make(map[int]int)
    for right := 0; right < len(nums); right++ {
        if _, ok := dic[nums[right]]; !ok {
            dic[nums[right]] = 1
        } else {
            dic[nums[right]] += 1
        }
        for dic[nums[right]] > k && left <= right {
            dic[nums[left]] -= 1
            left++
        }
        ans = max(ans, right-left+1)
    }
    return ans
}
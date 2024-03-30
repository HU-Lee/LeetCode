func atLeastK(nums []int, k int) int {
    dic := make(map[int]int)
    ans, left, right := 0,0,0
    for right < len(nums) {
        if _, ok := dic[nums[right]]; !ok {
            dic[nums[right]] = 1
        } else {
            dic[nums[right]] += 1
        }
        right++
        for len(dic) >= k {
            if val, _ := dic[nums[left]]; val == 1 {
                delete(dic, nums[left])
            } else {
                dic[nums[left]] -= 1
            }
            left++
        }
        ans += left
    }
    return ans
}

func subarraysWithKDistinct(nums []int, k int) int {
    return atLeastK(nums, k) - atLeastK(nums, k+1)
}
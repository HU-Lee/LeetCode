func countSubarrays(nums []int, minK int, maxK int) int64 {
    left, right, dead := 0,0,0
    ans := 0
    dic := make(map[int]int)
    for right < len(nums) {
        x := nums[right]
        dic[x]++
        right++
        if x > maxK || x < minK {
            left = right
            dead = right
            dic = make(map[int]int)
        } else {
            for dic[minK] != 0 && dic[maxK] != 0 && left < right {
                y := nums[left]
                if val, _ := dic[y]; val > 1 {
                    dic[y]--
                } else {
                    delete(dic, y)
                }
                left++
            } 
        }
        ans += left-dead
    }
    return int64(ans)
}
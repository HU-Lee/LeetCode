func sum(nums []int) int {
    sum := 0
    for _, num := range nums {
        sum += num
    }
    return sum
}

func numSubarraysWithSum(nums []int, goal int) int {
    l := len(nums)
    if sum(nums) < goal {
        return 0
    }
    arr := []int{-1}
    for i, num := range nums {
        if num == 1 {
            arr = append(arr, i)
        }
    }
    arr = append(arr, l)

    ans := 0
    if goal == 0 {
        for i:=0; i+1 < len(arr); i++ {
            s := arr[i+1] - arr[i]
            ans += s*(s-1)/2
        }
    } else {
        for i:=1; i+goal-1 < len(arr)-1; i++ {
            ans += (arr[i]-arr[i-1])*(arr[i+goal]-arr[i+goal-1])
        }
    }
    return ans
}
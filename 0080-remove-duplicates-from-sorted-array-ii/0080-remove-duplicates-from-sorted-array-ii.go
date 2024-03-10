func removeDuplicates(nums []int) int {
    dic := make(map[int]int)
    
    k := 0
    i := 0
    for i < len(nums) {
        num := nums[i]
        if num > 10000 {
            break
        }
        if val,ok := dic[num]; !ok {
            dic[num] = 1
            k++
            i++
        } else if val < 2 {
            dic[num] += 1
            k++
            i++
        } else {
            for n := i; n < len(nums) - 1; n++ {
                nums[n] = nums[n+1]
            }
            nums[len(nums)-1] = 10001
        }
    }
    return k
}
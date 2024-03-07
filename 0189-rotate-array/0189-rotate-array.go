func rotate(nums []int, k int)  {
    l := len(nums)
    s := k%l
    new_nums := append(nums[l-s:l], nums[0:l-s]...)
    for i, _ := range nums {
        nums[i] = new_nums[i] 
    }
}
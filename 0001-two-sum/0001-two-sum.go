func twoSum(nums []int, target int) []int {
    dic := make(map[int]int)

    for idx, num := range nums {
        if val, exists := dic[target-num]; exists {
            return []int{val, idx};
        }
        dic[num] = idx;
    }
    return []int{0,0}
}
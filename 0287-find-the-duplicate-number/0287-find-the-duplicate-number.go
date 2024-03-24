func findDuplicate(nums []int) int {
    d := make(map[int]int)

    for _, num := range nums {
        if _, ok := d[num]; !ok {
            d[num] = 1
        } else {
            return num
        }
    }
    return -1
}
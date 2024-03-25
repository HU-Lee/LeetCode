func findDuplicates(nums []int) []int {
    d := make(map[int]bool)

    var arr []int
    for _, num := range nums {
        if _, ok := d[num]; !ok {
            d[num] = true
        } else {
            arr = append(arr, num)
        }
    }
    return arr
}
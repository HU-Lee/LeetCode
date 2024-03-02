import "sort"

func sortedSquares(nums []int) []int {
    var arr []int
    for _, num := range nums {
        arr = append(arr, num*num)
    }
    sort.Ints(arr)

    return arr
}
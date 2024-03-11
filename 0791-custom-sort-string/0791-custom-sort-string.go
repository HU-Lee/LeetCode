import "sort"

func customSortString(order string, s string) string {
    ord := make(map[rune]int)
    for i, val := range order {
        ord[val] = i
    }
    arr := []rune(s)
    sort.Slice(arr, func (x,y int) bool {
        return ord[arr[x]] < ord[arr[y]]
    })
    return string(arr)
}
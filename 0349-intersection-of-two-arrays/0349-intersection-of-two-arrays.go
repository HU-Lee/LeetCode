import "sort"

func intersection(nums1 []int, nums2 []int) []int {
    sort.Ints(nums1)
    sort.Ints(nums2)
    i,j := 0,0
    tmp := -1
    var arr []int
    for i < len(nums1) && j < len(nums2) {
        m,n := nums1[i], nums2[j]
        if m == n && m != tmp {
            arr = append(arr, m)
            tmp = m
        } else if m > n {
            j++
        } else {
            i++
        }
    }
    return arr
}
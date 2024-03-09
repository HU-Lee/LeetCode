func getCommon(nums1 []int, nums2 []int) int {
    i,j := 0,0
    for i < len(nums1) && j < len(nums2) {
        d := nums1[i] - nums2[j]
        if d == 0 {
            return nums1[i]
        } else if d > 0 {
            j++
        } else {
            i++
        }
    }
    return -1
}
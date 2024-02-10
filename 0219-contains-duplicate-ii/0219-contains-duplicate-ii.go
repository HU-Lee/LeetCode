func containsNearbyDuplicate(nums []int, k int) bool {
	numMap := make(map[int]int)
    for i, num := range nums {
        idx, exists := numMap[num]; if exists {
            if i - idx <= k {
                return true;
            }
        }
        numMap[num] = i;
    }
	return false;
}
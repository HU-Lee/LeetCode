func containsNearbyDuplicate(nums []int, k int) bool {
	numMap := make(map[int]int)
    for i:=0; i<len(nums); i++ {
        idx, exists := numMap[nums[i]]; if exists {
            if i - idx <= k {
                return true;
            }
        }
        numMap[nums[i]] = i;
    }
	return false;
}
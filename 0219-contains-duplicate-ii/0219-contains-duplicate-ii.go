func containsNearbyDuplicate(nums []int, k int) bool {
	for i := 0; i < len(nums); i++ {
		for j := i+1; j < len(nums); j++ {
            if j - i > k {
                break;
            }
            if nums[i] == nums[j] {
                return true;
            }
        }
    }
	return false;
}
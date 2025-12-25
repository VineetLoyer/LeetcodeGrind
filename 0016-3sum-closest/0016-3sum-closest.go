import (
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	n := len(nums)

	// 1. Initialize result with the first possible triplet
	closestSum := nums[0] + nums[1] + nums[2]

	for i := 0; i < n-2; i++ {
		// Optional: Skip duplicates for 'i' to speed up
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		left, right := i+1, n-1

		for left < right {
			currSum := nums[i] + nums[left] + nums[right]

			// 2. Exact match check (distance is 0)
			if currSum == target {
				return currSum
			}

			// 3. Update closestSum if the new difference is smaller
			if abs(target-currSum) < abs(target-closestSum) {
				closestSum = currSum
			}

			// 4. Move pointers based on comparison with target
			if currSum < target {
				left++
			} else {
				right--
			}
		}
	}
	return closestSum
}

// Helper function for integer absolute value
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
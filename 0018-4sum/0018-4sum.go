import (
	"sort"
)

func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	var res [][]int

	// 1. First number (i)
	for i := 0; i < n-3; i++ {
		// Skip duplicates for i
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		// 2. Second number (j)
		for j := i + 1; j < n-2; j++ {
			// Skip duplicates for j. Note: j > i+1 ensures we don't skip the first valid j
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}

			// 3. Remaining two numbers (Two-Pointer approach)
			left := j + 1
			right := n - 1

			for left < right {
				// Use simple addition. Go's 'int' on 64-bit systems handles this, 
                // but strictly speaking, for very large constraints, you might cast to int64.
				sum := nums[i] + nums[j] + nums[left] + nums[right]

				if sum < target {
					left++
				} else if sum > target {
					right--
				} else {
					// Found a quadruplet
					res = append(res, []int{nums[i], nums[j], nums[left], nums[right]})

					// Skip duplicates for left and right
					for left < right && nums[left] == nums[left+1] {
						left++
					}
					for left < right && nums[right] == nums[right-1] {
						right--
					}

					left++
					right--
				}
			}
		}
	}
	return res
}
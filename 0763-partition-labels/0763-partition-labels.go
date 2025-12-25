func partitionLabels(s string) []int {
    lastIndex := [26]int{}
	for i, char := range s {
		lastIndex[char-'a'] = i
	}

	var res []int
	start := 0
	end := 0

	// 2. Iterate to find partitions
	for i, char := range s {
		// Update the end of the current partition to be the furthest 
		// last occurrence seen so far.
		if lastIndex[char-'a'] > end {
			end = lastIndex[char-'a']
		}

		// 3. If we reach the end, the partition is complete
		if i == end {
			// Size is end - start + 1
			res = append(res, end - start + 1)
			start = i + 1
		}
	}

	return res
}

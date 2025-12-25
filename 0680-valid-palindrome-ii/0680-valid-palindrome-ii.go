func validPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	for left < right {
		// If characters match, just keep moving inward
		if s[left] == s[right] {
			left++
			right--
		} else {
			// Mismatch found! We use our "one deletion" chance here.
			// We check if the substring is valid by skipping 'left' OR skipping 'right'.
			return isPalindromeRange(s, left+1, right) || isPalindromeRange(s, left, right-1)
		}
	}
	return true
}

// Helper function to check if a specific range of the string is a palindrome
func isPalindromeRange(s string, left, right int) bool {
	for left < right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse from the last digit backwards
        for i in range(len(digits) - 1, -1, -1):
            # If current digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If it is 9, set to 0 and continue to propagate carry
            digits[i] = 0

        # If loop completes, all digits were 9, so we need an extra digit
        return [1] + digits
        


/*
 * Problem #125: Valid Palindrome
 * Difficulty: Easy
 * Submission: Try 2
 * status: Accepted
 * Language: python
 * Date: 10/16/2026, 2:14:07 PM
 * Link: https://leetcode.com/problems/valid-palindrome/
 */

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna

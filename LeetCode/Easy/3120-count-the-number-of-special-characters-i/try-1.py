/*
 * Problem #3120: Count the Number of Special Characters I
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 10/19/2026, 8:48:53 PM
 * Link: https://leetcode.com/problems/count-the-number-of-special-characters-i/
 */


class Solution(object):
    def numberOfSpecialChars(self, word):
        count = 0

        for ch in set(word):
            if ch.islower() and ch.upper() in word:
                count += 1

        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna

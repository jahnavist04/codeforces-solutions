/*
 * Problem #6: Zigzag Conversion
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 10/30/2026, 6:51:47 PM
 * Link: https://leetcode.com/problems/zigzag-conversion/
 */


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currRow = 0
        direction = 1

        for char in s:
            rows[currRow] += char

            if currRow == 0:
                direction = 1
            elif currRow == numRows - 1:
                direction = -1

            currRow += direction

        return "".join(rows)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna

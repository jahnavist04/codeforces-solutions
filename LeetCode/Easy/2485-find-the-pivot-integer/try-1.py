/*
 * Problem #2485: Find the Pivot Integer
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 11/5/2026, 9:04:46 PM
 * Link: https://leetcode.com/problems/find-the-pivot-integer/
 */

class Solution(object):
    def pivotInteger(self, n):

        for x in range(1, n + 1):
            left = sum(range(1, x + 1))
            right = sum(range(x, n + 1))

            if left == right:
                return x

        return -1

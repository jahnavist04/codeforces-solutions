/*
 * Problem #1502: Can Make Arithmetic Progression From Sequence
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 11/5/2026, 9:03:57 PM
 * Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
 */

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()

        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False

        return True
        

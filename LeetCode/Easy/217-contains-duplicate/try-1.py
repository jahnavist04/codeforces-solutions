/*
 * Problem #217: Contains Duplicate
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 4/5/2026, 9:52:05 AM
 * Link: https://leetcode.com/problems/contains-duplicate/
 */

class Solution:
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

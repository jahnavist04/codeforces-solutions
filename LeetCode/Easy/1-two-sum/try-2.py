/*
 * Problem #1: Two Sum
 * Difficulty: Easy
 * Submission: Try 2
 * status: Accepted
 * Language: python
 * Date: 7/4/2026, 6:49:02 PM
 * Link: https://leetcode.com/problems/two-sum/
 */

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

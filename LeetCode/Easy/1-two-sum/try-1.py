/*
 * Problem #1: Two Sum
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 4/5/2026, 9:01:40 AM
 * Link: https://leetcode.com/problems/two-sum/
 */

class Solution(object):
    def twoSum(self, nums, target):
        d = {}  # value : index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in d:
                return [i, d[complement]]
            
            d[num] = i
        

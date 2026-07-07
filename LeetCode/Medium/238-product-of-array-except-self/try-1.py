/*
 * Problem #238: Product of Array Except Self
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 4/5/2026, 11:41:26 AM
 * Link: https://leetcode.com/problems/product-of-array-except-self/
 */

class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
        

/*
 * Problem #462: Minimum Moves to Equal Array Elements II
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 11/2/2026, 7:06:42 PM
 * Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
 */


class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        
        median = nums[len(nums) // 2]
        
        moves = 0
        for num in nums:
            moves += abs(num - median)
        
        return moves


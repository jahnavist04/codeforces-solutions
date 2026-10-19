/*
 * Problem #2089: Find Target Indices After Sorting Array
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 10/19/2026, 8:05:07 PM
 * Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/
 */

class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna

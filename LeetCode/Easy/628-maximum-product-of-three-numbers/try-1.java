/*
 * Problem #628: Maximum Product of Three Numbers
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: java
 * Date: 7/26/2026, 7:50:08 PM
 * Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
 */

import java.util.Arrays;

class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);

        int n = nums.length;

        int product1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
        int product2 = nums[0] * nums[1] * nums[n - 1];

        return Math.max(product1, product2);
    }
}

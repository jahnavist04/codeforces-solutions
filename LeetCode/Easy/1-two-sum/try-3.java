/*
 * Problem #1: Two Sum
 * Difficulty: Easy
 * Submission: Try 3
 * status: Accepted
 * Language: java
 * Date: 7/8/2026, 3:33:08 PM
 * Link: https://leetcode.com/problems/two-sum/
 */

class Solution {
    public int[] twoSum(int[] a, int target) {
        for (int i = 0; i < a.length; i++) {
            for (int j = i + 1; j < a.length; j++) {
                if (a[i] + a[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}
   

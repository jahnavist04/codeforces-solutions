/*
 * Problem #11: Container With Most Water
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: java
 * Date: 8/6/2026, 7:39:21 PM
 * Link: https://leetcode.com/problems/container-with-most-water/
 */

class Solution {
    public int maxArea(int[] height) {

        int left = 0;
        int right = height.length - 1;
        int max = 0;

        while (left < right) {

            int h = Math.min(height[left], height[right]);
            int w = right - left;
            int area = h * w;

            max = Math.max(max, area);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return max;
    }
}

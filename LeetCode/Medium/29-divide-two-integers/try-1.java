/*
 * Problem #29: Divide Two Integers
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: java
 * Date: 7/28/2026, 7:27:18 PM
 * Link: https://leetcode.com/problems/divide-two-integers/
 */

class Solution {
    public int divide(int dividend, int divisor) {

        // Handle overflow case
        if (dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;

        // Determine sign
        boolean negative = (dividend < 0) ^ (divisor < 0);

        // Convert to long to avoid overflow
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);

        int ans = 0;

        while (dvd >= dvs) {
            long temp = dvs;
            int multiple = 1;

            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }

            dvd -= temp;
            ans += multiple;
        }

        return negative ? -ans : ans;
    }
}

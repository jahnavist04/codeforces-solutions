/*
 * Problem #3754: Concatenate Non-Zero Digits and Multiply by Sum I
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: java
 * Date: 7/7/2026, 7:30:58 PM
 * Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
 */

class Solution {
    public long sumAndMultiply(int n) {
        String s = Integer.toString(n);
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c != '0') sb.append(c);
        }
        long x = sb.length() == 0 ? 0 : Long.parseLong(sb.toString());
        long sum = 0;
        long temp = x;
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        return x * sum;
    }
}
    

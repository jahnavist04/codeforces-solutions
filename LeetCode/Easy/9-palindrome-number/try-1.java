/*
 * Problem #9: Palindrome Number
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: java
 * Date: 7/8/2026, 7:31:33 PM
 * Link: https://leetcode.com/problems/palindrome-number/
 */

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        int temp = x;
        int rev = 0;
        while (x != 0) {
            int ld = x % 10;
            rev = rev * 10 + ld;
            x = x / 10;
        }
        return temp == rev;
    }
}

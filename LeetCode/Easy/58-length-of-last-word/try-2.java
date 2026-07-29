/*
 * Problem #58: Length of Last Word
 * Difficulty: Easy
 * Submission: Try 2
 * status: Accepted
 * Language: java
 * Date: 7/15/2026, 1:56:59 PM
 * Link: https://leetcode.com/problems/length-of-last-word/
 */

class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr = s.trim().split(" ");

        return arr[arr.length - 1].length();
    }
}

   

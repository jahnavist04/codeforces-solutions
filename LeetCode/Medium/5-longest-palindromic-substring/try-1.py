/*
 * Problem #5: Longest Palindromic Substring
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 11/3/2026, 9:04:54 PM
 * Link: https://leetcode.com/problems/longest-palindromic-substring/
 */


class Solution(object):
    def longestPalindrome(self, s):
        res = ""

        for i in range(len(s)):
            # Odd length palindrome
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

            # Even length palindrome
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res


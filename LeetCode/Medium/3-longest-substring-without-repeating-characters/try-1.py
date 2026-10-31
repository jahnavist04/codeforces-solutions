/*
 * Problem #3: Longest Substring Without Repeating Characters
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 10/31/2026, 8:55:34 PM
 * Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */


class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans


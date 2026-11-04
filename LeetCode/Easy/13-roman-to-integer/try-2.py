/*
 * Problem #13: Roman to Integer
 * Difficulty: Easy
 * Submission: Try 2
 * status: Accepted
 * Language: python
 * Date: 11/4/2026, 8:15:39 PM
 * Link: https://leetcode.com/problems/roman-to-integer/
 */


class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]

        return result


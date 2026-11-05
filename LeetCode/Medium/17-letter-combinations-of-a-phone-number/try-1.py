/*
 * Problem #17: Letter Combinations of a Phone Number
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 11/5/2026, 9:06:30 PM
 * Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 */

class Solution(object):
    def letterCombinations(self, digits):

        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return

            letters = phone[digits[index]]

            for ch in letters:
                backtrack(index + 1, path + ch)

        backtrack(0, "")

        return result
